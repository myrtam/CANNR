"""
CANNR TM analytics container building tool launcher.
Launches the tool from the user's desktop.
Copyright 2021 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import docker
import os
import platform
import sys
import json
import time
import subprocess as sp
from docker.types import Mount
from tkinter import *
from PIL import ImageTk, Image  

# Main window class
class Launcher(Frame):

    def __init__(self,parent=None):
        Frame.__init__(self,parent)
        self.parent = parent
        self.loadWidgets()

    def loadWidgets(self):

        # Add the window title
        self.winfo_toplevel().title("CANNR Tool Launcher")


# Initialize the Launcher window
window = Tk()
window.configure(background='#254D93')
window.minsize(400, 250)
window.columnconfigure([0,1], minsize=5)
window.rowconfigure([0, 7], minsize=50)

launcher = Launcher(window)

titleSpace = Label(text=' ', background='#254D93')
titleSpace.grid(row=0, column=0, sticky="w")

# Add the title line to the frame.
titleLabel = Label(
    text='Launch the CANNR\u2122 Web Based Tool', 
    font=('Arial', 20), 
    background='#254D93', 
    foreground='white'
    )
titleLabel.grid(row=0, column=1, sticky="w")

# Launch button
launchBtn = Button(
    window, 
    text="Launch", 
    font=('Arial', 16),
    width=15
    )
launchBtn.grid(row=1, column=1, sticky="w")

buttonSpace1 = Label(text=' ', font=('Arial', 5), background='#254D93')
buttonSpace1.grid(row=2, column=1)

# Shut down button
shutDownBtn = Button(
    window,
    text="Shut Down", 
    font=('Arial', 16),
    width=15
    )
shutDownBtn.grid(row=3, column=1, sticky="w")

buttonSpace2 = Label(text=' ', font=('Arial', 5), background='#254D93')
buttonSpace2.grid(row=4, column=1)

# Settings button
settingsBtn = Button(
    window,
    text="Settings...", 
    font=('Arial', 16),
    width=15
    )
settingsBtn.grid(row=5, column=1, sticky="w")

buttonSpace3 = Label(text=' ', font=('Arial', 5), background='#254D93')
buttonSpace3.grid(row=6, column=1)

# Status line
statusLine = Label(
    text=' ', 
    font=('Arial', 14),
    anchor="w",
    justify=LEFT,
    background='#254D93', 
    foreground='white',
    wraplength=350
    )
statusLine.grid(row=7, column=1, sticky="w")

statusLine['text'] = ' '


# Update the status line.
def updateStatus(statusText):
    statusLine['text'] = statusText
    statusLine.update()


# Launch event handler
def onLaunch(event):

    if startup():

        # Delay 5 seconds to give container time to start
        updateStatus('Launching.  Please wait...')
        time.sleep(5)

        # Launch the tool and exit
        os.system('open http://localhost:8080/web/webtool/index.html')
        sys.exit(0)
    
launchBtn.bind('<Button-1>', onLaunch)

# Launch event handler
def onShutDown(event):
    # TODO: IMPLEMENT THIS!
    shutdown()
    #statusLine['text'] = 'Shut down!'
    #print('Shut down!')

shutDownBtn.bind('<Button-1>', onShutDown)

# Launch event handler
def onSettings(event):
    # TODO: IMPLEMENT THIS!
    print('Settings!')

settingsBtn.bind('<Button-1>', onSettings)


# Get the status of the Web tool.
def getStatus(containerID, dockerURL):

    if not containerID:
        return {
            'succeeded': False,
            'status': 'noContainerID',
            'detail': 'No container ID'
        }

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
        if os.path.isfile('config.json'):
            with open('config.json', 'r') as configFile:
                config = json.loads(configFile.read())
    
        if not config:
            config = {}
    
        externalPath = config.get('externalPath', None)
        if not externalPath or not os.path.isdir(externalPath):
            config['containerID'] = 'cannr-web'
            externalPath = 'external'
            config['externalPath'] = externalPath
            os.mkdir(externalPath)
            configPath = os.path.join(externalPath, 'config')
            os.mkdir(configPath)
            context = {
                'dockerURL': getDockerURL()                
                }
            with open(os.path.join(configPath, 'context.json'), 'w') as contextFile:
                contextFile.write(json.dumps(context, indent=2))
        
            saveConfig(config)
        
        return config
        
    except Exception as err:
        updateStatus('Error:  Unable to get configuration.\n' + str(err))
        return None


# Saves the configuration
def saveConfig(config):

    with open('config.json', 'w') as configFile:
        configFile.write(json.dumps(config, indent=2))


# Returns the URL of the local Docker daemon.
def getDockerURL():
    
    if platform.system()=='Windows':
        return 'tcp://localhost:2375'
    else:
        return 'unix://var/run/docker.sock'


# Check container status, try to start if not running.
# Returns True if container running, False otherwise.
def startup():

    try:
        
        config = getConfig()
        if not config:
            return False
        
        externalPath = config.get('externalPath')
        externalPath = os.path.abspath(externalPath)
        containerID = config.get('containerID', 'cannr-web')

        # Get the image name
        image = config.get('image', None)
        if not image:
            image = 'cannr/cannr-web:latest'
            config['image'] = image
            
        # Get the local port  
        localPort = config.get('port', 8080)
        if not localPort:
            localPort = 8080
            config['localPort'] = localPort

        ports = {'80/tcp': localPort}

        status = getStatus(containerID, getDockerURL())
        succeeded = status.get('succeeded', False)
        if not succeeded:
            if  status.get('error', 'unableToConnect')=='unableToConnect':
                updateStatus('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
                print('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
            else:
                error = status.get('errorMsg', '')
                detail = status.get('detail', '')
                message = error + ':  ' + detail if (error and detail) else error + detail
                message = message if message else 'Error getting container status'
                updateStatus(message)
                print(message)
                
            return False
        
        else:
            statusMsg = status.get('status', 'notFound')
            
            if statusMsg in ('notFound', 'exited'):

                # Try to connect to the Docker daemon
                client = docker.DockerClient(base_url=getDockerURL())
    
                if statusMsg=='notFound':
                    
                    # External directory to mount
                    mount = Mount(
                        source=externalPath,
                        target='/external',
                        type='bind',
                    )
                    
                    updateStatus('Starting the container.  Please wait...')
                    # Start the container, and get the result.
                    if platform.system()=='Windows':
                        container = client.containers.run(
                            image, 
                            name = 'cannr-web',
                            mounts=[mount],
                            detach = True, 
                            remove = False, 
                            ports = ports
                            )

                    else:
                        
                        # Volume dictionary for mapping Docker port (OSX/Linux)
                        volumes = {
                            '/var/run/docker.sock': {
                                'bind': '/var/run/docker.sock', 'mode': 'rw'}
                            }
                    
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
                    updateStatus('Container started.')
                    print('Container started.')
    
                elif statusMsg=='exited':
                    containerID = config['containerID']
                    container = client.containers.get(containerID)
                    updateStatus('Restarting the container.  Please wait...')
                    container.start()
                    updateStatus('Container restarted.')
                    
                client.close()

            elif statusMsg=='running':
                updateStatus('Container is running.')
                
            saveConfig(config)

            return True
    
    except Exception as err:
        updateStatus(str(err))
        print(str(err))


# Shuts down the container.
def shutdown():

    try:
        
        config = getConfig()
        if not config:
            return False
        
        containerID = config.get('containerID', 'cannr-web')

        # Get the image name
        image = config.get('image', 'cannr/cannr-web:latest')
        localPort = config.get('port', 8080)
        ports = {str(localPort) + '/tcp': 80}

        status = getStatus(containerID, getDockerURL())
        succeeded = status.get('succeeded', False)
        if not succeeded:
            if  status.get('error', 'unableToConnect')=='unableToConnect':
                updateStatus('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
                print('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
            else:
                error = status.get('errorMsg', '')
                detail = status.get('detail', '')
                message += error + ':  ' + detail if (error and detail) else error + detail
                message = message if message else 'Error getting container status'
                updateStatus(message)
                print(message)
                
            return False
        
        else:

            statusMsg = status.get('status', 'notFound')
            
            if statusMsg=='running':

                # Try to connect to the Docker daemon
                client = docker.DockerClient(base_url=getDockerURL())

                container = client.containers.get(containerID)
                updateStatus('Stopping the container.  Please wait...')
                container.stop()
                updateStatus('Container stopped.')
                    
                client.close()                    

            return True
    
    except Exception as err:
        updateStatus(str(err))
        print(str(err))


# Try to start the container.
try:
    
    startup()

except Exception as err:
    updateStatus(str(err))
    print(str(err))

# Start the event loop
window.mainloop()


