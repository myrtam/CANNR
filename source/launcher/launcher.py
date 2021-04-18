"""
CANNR TM analytics container building tool launcher.
Launches the tool from the user's desktop.
Copyright 2021 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

#import tkinter as tk
import docker
import os
import sys
import json
import subprocess as sp
from docker.types import Mount
from tkinter import *  
from PIL import ImageTk, Image  

# Define functions

# Get the status of the Web tool.
def getStatus(containerID, dockerURL):

    client = None

    try:
    
        # Try to connect to the Docker daemon
        client = docker.DockerClient(base_url=dockerURL)
    
    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'unableToConnect',
            'errorMsg': 'Unable to connect to Docker',
            'detail': str(err)
            }

    try:

        # Get the container and return status.
        container = client.containers.get(containerID)
        client.close()
        return {
            'succeeded': True, 
            'status': container.status,
            'detail': 'Container found'
            }

    except Exception as err:
        client.close()
        if err.__class__.__name__ == 'NotFound':
            return {
                'succeeded': True,
                'status': 'notFound',
                'detail': 'Container not found'
            }
        else:
            return {
                'succeeded': False, 
                'error': 'errorGettingStatus',
                'errorMsg': 'Error getting container status',
                'detail': str(err)
                }


# Checks to make sure the configuration has the right information.
# Returns True if yes, False if no.
def getConfig():
    
    try:

        config = None
        with open('config.json', 'r') as configFile:
            config = json.loads(configFile.read())
    
        if not config:
            return None
    
        externalPath = config.get('externalPath', None)
        if not externalPath or not os.path.isdir(externalPath):
            return None
        
        return config
        
    except Exception as err:
        return None


# Saves the configuration
def saveConfig(config):

    with open('config.json', 'w') as configFile:
        configFile.write(json.dumps(config))


# Check container status, try to start if not running.
# Returns True if container running, False otherwise.
def startup():

    try:
        
        config = getConfig()
        if not config:
            return False
        
        externalPath = config.get('externalPath')
        externalPath = os.path.abspath(externalPath)
        dockerURL = config.get('dockerURL', 'unix://var/run/docker.sock')
        containerID = config.get('containerID', 'cannr-web')

        # Get the image name
        image = config.get('image', 'cannr/cannr-web:latest')
        localPort = config.get('port', 8080)
        #ports = {str(localPort) + '/tcp': 80}
        ports = {'80/tcp': localPort}

        status = getStatus(containerID, dockerURL)
        succeeded = status.get('succeeded', False)
        if not succeeded:
            if  status.get('error', 'unableToConnect')=='unableToConnect':
                print('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
            else:
                error = status.get('errorMsg', '')
                detail = status.get('detail', '')
                message += error + ':  ' + detail if (error and detail) else error + detail
                message = message if message else 'Error getting container status'
                print(message)
                
            return False
        
        else:
            statusMsg = status.get('status', 'notFound')
            
            if statusMsg in ('notFound', 'exited'):

                # Try to connect to the Docker daemon
                client = docker.DockerClient(base_url=dockerURL)
    
                if statusMsg=='notFound':
                    
                    # External directory to mount
                    mount = Mount(
                        source=externalPath,
                        target='/external',
                        type='bind',
                    )
                    
                    # Volume dictionary for mapping Docker port (OSX/Linux)
                    volumes = {
                        '/var/run/docker.sock': {
                            'bind': '/var/run/docker.sock', 'mode': 'rw'}
                        }
                    
                    print('Starting the container...')
                    # Start the container, and get the result.
                    container = client.containers.run(
                        image, 
                        name = 'cannr-web',
                        mounts=[mount],
                        volumes=volumes,
                        detach = True, 
                        remove = False, 
                        ports = ports
                        )
                    config['containerID'] = container.id
                    print('Container started.')
    
                elif statusMsg=='exited':
                    containerID = config['containerID']
                    container = client.containers.get(containerID)
                    print('Restarting the container...')
                    container.start()
                    print('Container restarted.')
                    
                client.close()

            elif statusMsg=='running':
                print('Container is running.')
                
            saveConfig(config)

            return True
    
    except Exception as err:
        print(str(err))


# Shuts down the container.
def shutdown():

    try:
        
        config = getConfig()
        if not config:
            return False
        
        dockerURL = config.get('dockerURL', 'unix://var/run/docker.sock')
        containerID = config.get('containerID', 'cannr-web')

        # Get the image name
        image = config.get('image', 'cannr/cannr-web:latest')
        localPort = config.get('port', 8080)
        ports = {str(localPort) + '/tcp': 80}

        status = getStatus(containerID, dockerURL)
        succeeded = status.get('succeeded', False)
        if not succeeded:
            if  status.get('error', 'unableToConnect')=='unableToConnect':
                print('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
            else:
                error = status.get('errorMsg', '')
                detail = status.get('detail', '')
                message += error + ':  ' + detail if (error and detail) else error + detail
                message = message if message else 'Error getting container status'
                print(message)
                
            return False
        
        else:

            statusMsg = status.get('status', 'notFound')
            
            if statusMsg=='running':

                # Try to connect to the Docker daemon
                client = docker.DockerClient(base_url=dockerURL)

                container = client.containers.get(containerID)
                print('Stopping the container...')
                container.stop()
                print('Container stopped.')
                    
                client.close()                    

            return True
    
    except Exception as err:
        print(str(err))


# Check container status, try to start if not running.
# Returns True if container running, False otherwise.
def launch():

    try:
        
        # Get the configuration.
        config = getConfig()
        if not config:
            return False
        
        # Get the local port
        localPort = config.get('port', 8080)

        # Launch the Web tool in the default browser
        os.system('open http://localhost:' + str(localPort) + '/web/webtool/index.html')
        print('Launched!')
        sys.exit(0)

    except Exception as err:
        print(str(err))


# Window
window = Tk()

# Title
titleLabel = Label(text="CANNR Tool Launcher")
titleLabel.pack()

'''
Buttons:
* Launch - Launches the tool in the user's default browser, first checking that
  Docker and the web tool are running.  (Re)starts the Web tool as needed.
* Shut down - Shuts down the Web tool.
* Settings - Enables editing of Web tool settings, include
  - External directory
  - Base image
  - Maintainer
  - Docker URL
* Quit - Closes the launcher
* Status line/bar
'''
launchBtn = Button(text="Launch")
launchBtn.pack()

shutDownBtn = Button(text="Shut Down")
shutDownBtn.pack()

settingsBtn = Button(text="Settings...")
settingsBtn.pack()

'''
canvas = Canvas(window, width = 300, height = 300)
canvas.pack()
image = PhotoImage(file="Spinner-3.gif")
canvas.create_image(20, 20, anchor=NW, image=image)
'''

# Status line
statusLine = Label(text="")
statusLine.pack()


'''
Event handlers
'''

# Launch event handler
def onLaunch(event):
    # TODO: IMPLEMENT THIS!
    if startup():
        # TODO:  Launch the URL, close the launcher
        #sp.run('open', 'http://localhost:8080/web/webtool/index.html')
        os.system('open http://localhost:8080/web/webtool/index.html')
        print('Launched!')
        sys.exit(0)
    
launchBtn.bind('<Button-1>', onLaunch)

# Launch event handler
def onShutDown(event):
    # TODO: IMPLEMENT THIS!
    shutdown()
    print('Shut down!')

shutDownBtn.bind('<Button-1>', onShutDown)

# Launch event handler
def onSettings(event):
    # TODO: IMPLEMENT THIS!
    print('Settings!')

settingsBtn.bind('<Button-1>', onSettings)


'''
Startup:
* Load config.json
* Load configuration
* Check that Docker is running, if not, display message.
  - Ask the user to check that Docker is running.
  - For Windows, ask the user to check that docker is running on tcp://...
* Check whether Web tool container has been created:
  - If so, check whether container is running.
* Display Web tool status.
'''
# Try to start the container.
try:
    
    startup()

except Exception as err:
    print(str(err))


'''
Launch:
* If can't connect to Docker, disabled.
* If container not running, start the container.
* If container not created, run it.
* Save the container ID in config.json
* Launch the Web tool URL
'''

'''
Shut Down:
* If Web tool not running, disabled.
* Display message telling user to close browser window.
* Stop the container.
* Disable the button.
'''

'''
Settings:
* Bring up screen to edit settings.
* On save:
  - Save the settings in config.json
  - Prompt the user to restart the container.
* On restart:
  - Prompt the user to close their browser
  - Restart
  - Launch Web tool URL
'''

'''
Event Loop
'''
window.mainloop()


