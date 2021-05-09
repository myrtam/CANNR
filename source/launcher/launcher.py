"""
CANNR TM analytics container building tool launcher.
Launches the tool from the user's desktop.
Copyright 2021 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import os
import platform
import sys
import json
import time
import subprocess as sp
import tkinter as tk
from tkinter import messagebox
import docker
from docker.types import Mount
import pathlib

# Main window class
class Launcher(tk.Frame):

    def __init__(self,parent=None):
        tk.Frame.__init__(self,parent)
        self.parent = parent
        self.winfo_toplevel().title("CANNR Tool Launcher")
        self.winfo_toplevel().minsize(400, 250)
        self.winfo_toplevel().configure(background='#254D93')
        self.winfo_toplevel().columnconfigure([0,1], minsize=5)
        self.winfo_toplevel().rowconfigure([0, 7], minsize=50)

        self.titleSpace = tk.Label(text=' ', background='#254D93')
        self.titleSpace.grid(row=0, column=0, sticky="w")
        
        # Add the title line to the frame.
        self.titleLabel = tk.Label(
            text='Launch the CANNR\u2122 Web Based Tool', 
            font=('Arial', 20), 
            background='#254D93', 
            foreground='white'
            )
        self.titleLabel.grid(row=0, column=1, sticky="w")
        
        # Launch button
        self.launchBtn = tk.Button(
            window, 
            text="Launch", 
            font=('Arial', 16),
            width=15,
            command=self.onLaunch
            )
        self.launchBtn.grid(row=1, column=1, sticky="w")
        
        self.buttonSpace1 = tk.Label(text=' ', font=('Arial', 5), background='#254D93')
        self.buttonSpace1.grid(row=2, column=1)
        
        # Shut down button
        self.shutDownBtn = tk.Button(
            window,
            text="Shut Down", 
            font=('Arial', 16),
            width=15,
            command=self.onShutDown
            )
        self.shutDownBtn.grid(row=3, column=1, sticky="w")
        
        self.buttonSpace2 = tk.Label(text=' ', font=('Arial', 5), background='#254D93')
        self.buttonSpace2.grid(row=4, column=1)
        
        # Settings button
        self.settingsBtn = tk.Button(
            window,
            text="Settings...", 
            font=('Arial', 16),
            width=15,
            command=self.onSettings
            )
        self.settingsBtn.grid(row=5, column=1, sticky="w")
        
        self.buttonSpace3 = tk.Label(text=' ', font=('Arial', 5), background='#254D93')
        self.buttonSpace3.grid(row=6, column=1)
        
        # Status line
        self.statusLine = tk.Label(
            text=' ', 
            font=('Arial', 14),
            anchor="w",
            justify=tk.LEFT,
            background='#254D93', 
            foreground='white',
            wraplength=350
            )
        self.statusLine.grid(row=7, column=1, sticky="w")
        
        self.statusLine['text'] = ' '
        
        self.settingsTop = None


    # Launch event handler
    def onLaunch(self):
    
        if startup(False):
    
            # Delay 5 seconds to give container time to start
            self.updateStatus('Launching.  Please wait...')
            time.sleep(5)
    
            # Launch the tool and exit
            os.system('open http://localhost:8080/web/webtool/index.html')
            sys.exit(0)
        
    # Shutdown event handler
    def onShutDown(self):

        shutdown()
    
    # Settings button event handler
    def onSettings(self):

        if not self.settingsTop:
            self.settingsTop = tk.Toplevel(self.master)
            self.settings = Settings(self.settingsTop)
        else:
            self.settingsTop.deiconify()
    
    # Update the status line.
    def updateStatus(self, statusText):
        self.statusLine['text'] = statusText
        self.statusLine.update()


# Setting window class
class Settings:
    def __init__(self, master):
        
        oneTimeSetup = not hasConfig()
        
        self.master = master
        settingsTitle = 'CANNR Tool One Time Setup' if oneTimeSetup else 'CANNR Tool Settings'
        self.master.title(settingsTitle)
        self.master.minsize(650, 250)
        self.master.configure(background='#254D93')
        self.master.protocol('WM_DELETE_WINDOW', self.close)

        self.inputFrame = tk.Frame(self.master, width=150, background='#254D93')

        self.titleSpace = tk.Label(
            self.inputFrame,
            text='', 
            font=('Arial', 5), 
            background='#254D93')
        self.titleSpace.grid(row=0, column=0, sticky="w")
        
        
        # Add the title line to the frame.
        self.titleLabel = tk.Label(
            self.inputFrame,
            text='Settings', 
            font=('Arial', 20), 
            justify=tk.LEFT,
            background='#254D93', 
            foreground='white'
            )
        self.titleLabel.grid(row=1, column=1, sticky="w")
        
        if oneTimeSetup:
            self.tempConfig = makeConfig()
        else:
            self.tempConfig = getConfig()
       
        # Space between rowse
        self.space1 = tk.Label(
            self.inputFrame,
            text=' ', 
            font=('Arial', 5), 
            background='#254D93')
        self.space1.grid(row=2, column=1, sticky="w")
        
        # Label for container version.
        self.versionLabel = tk.Label(
            self.inputFrame,
            text='Version:', 
            font=('Arial', 16), 
            background='#254D93', 
            foreground='white'
            )
        self.versionLabel.grid(row=3, column=1, sticky="w")
        
        # Version pulldown
        #getVersions(getDockerURL())
        #self.versions = ['0.1.0', '0.1.1', 'latest']

        if oneTimeSetup:
            self.versions = ['latest']
        else:
            self.versions = getVersions(getDockerURL())
        
        #self.versions = getVersions(getDockerURL())
        self.version = tk.StringVar(self.master)
        configVersion = self.tempConfig.get('version')
        configVersion = configVersion if configVersion in self.versions else 'latest'
        self.version.set(configVersion)        
        self.versionMenu = tk.OptionMenu(self.inputFrame, self.version, *self.versions)
        self.versionMenu.grid(row=3, column=2, sticky="w")
        
        # Space between rows
        self.space2 = tk.Label(
            self.inputFrame,
            text=' ', 
            font=('Arial', 5), 
            background='#254D93')
        self.space2.grid(row=4, column=1, sticky="w")
        
        # Label for projects directory.
        self.projectsLabel = tk.Label(
            self.inputFrame,
            text='Projects Location:', 
            font=('Arial', 16), 
            background='#254D93', 
            foreground='white'
            )
        self.projectsLabel.grid(row=5, column=1, sticky="w")
        
        # Projects directory textbox.
        self.projectsPath = tk.Entry(self.inputFrame, width=40)
        self.projectsPath.grid(row=5, column=2, sticky="w")
        self.projectsPath.insert(0, self.tempConfig.get('projectsPath'))
        
        # TODO:  ADD BUTTON FOR FILE PICKER
        
        # Space between rows
        self.space3 = tk.Label(
            self.inputFrame,
            text=' ', 
            font=('Arial', 5), 
            background='#254D93')
        self.space3.grid(row=6, column=1, sticky="w")
        
        # Label for projects directory.
        self.workingLabel = tk.Label(
            self.inputFrame,
            text='Working Location:', 
            font=('Arial', 16), 
            background='#254D93', 
            foreground='white'
            )
        self.workingLabel.grid(row=7, column=1, sticky="w")
        
        # Projects directory textbox.
        self.workingDir = tk.Entry(self.inputFrame, width=40)
        self.workingDir.grid(row=7, column=2, sticky="w")
        self.workingDir.insert(0, self.tempConfig.get('workingDirectory'))
        
        # TODO:  ADD BUTTON FOR FILE PICKER

        self.inputFrame.pack()

        # Define buttons
        self.buttonFrame = tk.Frame(self.master, width=150, background='#254D93')
        
        # Space between rows
        self.space4 = tk.Label(
            self.buttonFrame,
            text='', 
            font=('Arial', 16), 
            background='#254D93')
        self.space4.grid(row=0, column=1, sticky="w")
        
        self.saveButton = tk.Button(self.buttonFrame, text = 'Save', width = 8, command=self.save)
        self.saveButton.grid(row=1, column=0)
        
        # Space between buttons
        self.space5 = tk.Label(
            self.buttonFrame,
            text='  ', 
            background='#254D93')
        self.space5.grid(row=1, column=1, sticky="w")
        
        self.cancelButton = tk.Button(self.buttonFrame, text = 'Cancel', width = 8, command=self.close)
        self.cancelButton.grid(row=1, column=2)
                
        self.buttonFrame.pack()
    
    
    # Compare the inputs with the original configuration
    def compare(self):
        
        return (self.tempConfig['version'] != self.version.get() or
            self.tempConfig['projectsPath'] != self.projectsPath.get() or
            self.tempConfig['workingDirectory'] != self.workingDir.get())
    
    # Save settings
    def save(self):

        global window
        global launcher
        if self.master==window:
            messagebox.showinfo('Container Start',
                'The CANNR Web image will be downloaded and the container will be started for the first time.\nThis may take a while.')
            saveConfig(self.tempConfig)
            self.master.destroy()
            window = tk.Tk()
            launcher = Launcher(window)
            startup(True)
            window.mainloop()
            pass
        
        elif (self.compare() and     
            messagebox.askokcancel('Restart', 'The container will be restarted.  Proceed?')):
            
                launcher.updateStatus('Restarting the container.  Please wait...')
                self.master.withdraw()
            
                if self.version.get():
                    self.tempConfig['version'] = self.version.get()
                if self.projectsPath.get():
                    self.tempConfig['projectsPath'] = self.projectsPath.get()
                if self.workingDir.get():
                    self.tempConfig['workingDirectory'] = self.workingDir.get()
                
                saveConfig(self.tempConfig)
        
                containerState = getContainerState(self.tempConfig)
                
                if containerState=='running':
                    shutdown()
                    
                if containerState in ['running', 'exited']:
                    rmContainer()
                    
                startup(False)
     
    # Close the settings window   
    def close(self):
        if self.master==window:
            sys.exit()
        else:
            self.master.withdraw()


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


# Returns whether the container exists and is running
def getContainerState(config):

    containerID = config.get('containerID', 'cannr-web')

    status = getStatus(containerID, getDockerURL())
    succeeded = status.get('succeeded', False)
    if not succeeded:
        return 'failed'
    else:
        return status.get('status', 'notFound')


# Get the available versions of the tool.
def getVersions(dockerURL):

    # Try to connect to the Docker daemon
    client = docker.DockerClient(base_url=dockerURL)
    images = client.images.list(name='cannr/cannr-web')
    imageNames = images[0].tags
    
    tags = []
    for imageName in imageNames:
        tags.append(imageName[16:])
    
    client.close()

    return tags


# Returns the CANNR home directory
def getCannrPath():
    
    osPlatform = getPlatform()
    homePath = str(pathlib.Path.home())
    
    if osPlatform=='Darwin':
        return os.path.join(homePath, 'Library', 'CannR')
    elif osPlatform=='Windows':
        return os.path.join(homePath, 'Documents', 'CannR')
    elif osPlatform in ['Linux']:
        return os.path.join(homePath, '.config', 'CannrR')
    
    else:
        # TODO:  THIS IS AN ERROR!
        return None


# Returns the path of the config file.
def getCannrConfigPath():
    
    cannrPath = getCannrPath()
    if cannrPath:
        return os.path.join(cannrPath, 'config.json')
    else:
        # TODO:  THIS IS AN ERROR!
        return None


# Returns whether there is a CANNR configuration file.
def hasConfig():

    return os.path.isfile(getCannrConfigPath())


def getHomePath():

    osPlatform = getPlatform()
    homePath = str(pathlib.Path.home())
    
    if osPlatform in ['Windows', 'Darwin']:
        return os.path.join(homePath, 'Documents', 'CannR')
    elif osPlatform in ['Linux']:
        return os.path.join(homePath, 'CannR')
    
    else:
        return None    


# Returns the standard context path
def getContextPath():
        
    homePath = getHomePath()
    
    if homePath:
        return os.path.join(homePath, 'config')
    else:
        return None    


# Returns the standard projects path
def getProjectsPath():
        
    homePath = getHomePath()
    
    if homePath:
        return os.path.join(homePath, 'projects')
    else:
        return None    


# Returns the standard working directory
def getWorkingDirectory():
        
    homePath = getHomePath()
    
    if homePath:
        return os.path.join(homePath, 'working')
    else:
        return None    


# Create a blank configuration file, figures out what projects and working directories should be.
def makeConfig():

    try:
        
        config = {}
        config['contextPath'] = getContextPath()        
        config['projectsPath'] = getProjectsPath()        
        config['workingDirectory'] = getWorkingDirectory()
        config['version'] = 'latest'
        config['containerID'] = 'cannr-web'
        
        return config
    
    except Exception as err:
        return None
    

# Gets the configuration.
def getConfig():
    
    try:
        
        if not hasConfig():
            raise Exception('No configuration available.')            

        config = None
        with open(getCannrConfigPath(), 'r') as configFile:
            config = json.loads(configFile.read())
    
        if not config:
            config = {}
            
        return config

    except Exception as err:
        launcher.updateStatus('Error:  Unable to get configuration.\n' + str(err))
        return None


# Saves the configuration
def saveConfig(config):

    try:
        
        contextPath = config.get('contextPath', None)
        if not contextPath:
            raise Exception('Context directory not specified.')

        contextPath = os.path.abspath(contextPath)
        config['contextPath'] = contextPath
        
        projectsPath = config.get('projectsPath', None)
        if not projectsPath:
            raise Exception('Projects directory not specified.')

        projectsPath = os.path.abspath(projectsPath)
        config['projectsPath'] = projectsPath
        
        workingDirectory = config.get('workingDirectory', None)
        if not workingDirectory:
            raise Exception('Working directory not specified.')
        
        workingDirectory = os.path.abspath(workingDirectory)
        config['workingDirectory'] = workingDirectory
        
        # Create paths if they don't exist
        if not os.path.isdir(contextPath):
            os.makedirs(contextPath)
            #config['contextPath'] = contextPath
            
        if not os.path.isdir(projectsPath):
            os.makedirs(projectsPath)
            #config['projectsPath'] = projectsPath
            
        if not os.path.isdir(workingDirectory):
            os.makedirs(workingDirectory)
            #config['workingDirectory'] = workingDirectory
    
        cannrPath = getCannrPath()
        if not os.path.isdir(cannrPath):
            os.makedirs(cannrPath)

        with open(getCannrConfigPath(), 'w') as configFile:
            configFile.write(json.dumps(config))

        return config
            
    except Exception as err:
        launcher.updateStatus('Error:  Unable to save configuration.\n' + str(err))
        return None


# Returns the name of the platform (OS).
def getPlatform():
    
    return platform.system()


# Returns the URL of the local Docker daemon.
def getDockerURL():
    
    osPlatform = getPlatform()
    
    if osPlatform=='Windows':
        return 'tcp://localhost:2375'
    elif osPlatform in ['Linux', 'Darwin']:
        return 'unix://var/run/docker.sock'
    
    else:
        return None


# Check container status, try to start if not running.
# Returns True if container running, False otherwise.
def startup(firstRun):

    try:
        
        launcher.updateStatus('Getting container status.  Please wait...')

        config = getConfig()
        if not config:
            return False
        
        contextPath = config.get('contextPath')
        contextPath = os.path.abspath(contextPath)
        projectsPath = config.get('projectsPath')
        projectsPath = os.path.abspath(projectsPath)
        workingDirectory = config.get('workingDirectory')
        workingDirectory = os.path.abspath(workingDirectory)
        
        containerID = config.get('containerID', 'cannr-web')

        # Get the image name
        version = config.get('version', 'latest')
        image = 'cannr/cannr-web:' + version
            
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
                launcher.updateStatus('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
                print('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
            else:
                error = status.get('errorMsg', '')
                detail = status.get('detail', '')
                message = error + ':  ' + detail if (error and detail) else error + detail
                message = message if message else 'Error getting container status'
                launcher.updateStatus(message)
                print(message)
                
            return False
        
        else:
            statusMsg = status.get('status', 'notFound')
            
            if statusMsg in ('notFound', 'exited'):

                # Try to connect to the Docker daemon
                client = docker.DockerClient(base_url=getDockerURL())
    
                if statusMsg=='notFound':
 
                    # External directories to mount
                    configMount = Mount(
                        source=contextPath,
                        target='/config',
                        type='bind',
                    )
                    
                    projectsMount = Mount(
                        source=projectsPath,
                        target='/projects',
                        type='bind',
                    )
                    
                    workingMount = Mount(
                        source=workingDirectory,
                        target='/working',
                        type='bind',
                    )

                    #mounts=[configMount, projectsMount, workingMount]
                    mounts=[configMount, projectsMount, workingMount]
                    
                    if oneTimeSetup:
                        launcher.updateStatus('Downloading the image and starting the container.\nPlease wait...')
                    else:
                        launcher.updateStatus('Starting the container.  Please wait...')

                    # Start the container, and get the result.
                    if platform.system()=='Windows':
                        container = client.containers.run(
                            image, 
                            name = 'cannr-web',
                            mounts=mounts,
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
                            mounts=mounts,
                            #mounts=[mount],
                            volumes=volumes,
                            detach = True, 
                            remove = False, 
                            ports = ports
                            )

                    config['containerID'] = container.id
                    launcher.updateStatus('Container started.')
                    print('Container started.')
    
                elif statusMsg=='exited':
                    containerID = config['containerID']
                    container = client.containers.get(containerID)
                    launcher.updateStatus('Restarting the container.  Please wait...')
                    container.start()
                    launcher.updateStatus('Container restarted.')
                    
                client.close()

            elif statusMsg=='running':
                launcher.updateStatus('Container is running.')
                
            saveConfig(config)

            return True
    
    except Exception as err:
        launcher.updateStatus(str(err))
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
                launcher.updateStatus('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
                print('Unable to connect to Docker.  Please check to make sure Docker is running and configured to accept connections.')
            else:
                error = status.get('errorMsg', '')
                detail = status.get('detail', '')
                message += error + ':  ' + detail if (error and detail) else error + detail
                message = message if message else 'Error getting container status'
                launcher.updateStatus(message)
                print(message)
                
            return False
        
        else:

            statusMsg = status.get('status', 'notFound')
            
            if statusMsg=='running':

                # Try to connect to the Docker daemon
                client = docker.DockerClient(base_url=getDockerURL())

                container = client.containers.get(containerID)
                launcher.updateStatus('Stopping the container.  Please wait...')
                container.stop()
                launcher.updateStatus('Container stopped.')
                    
                client.close()                    

            return True
    
    except Exception as err:
        launcher.updateStatus(str(err))
        print(str(err))


# Removes the container.
def rmContainer():

    try:
        
        config = getConfig()
        if not config:
            return False
        
        containerID = config.get('containerID', 'cannr-web')

        # Try to connect to the Docker daemon
        client = docker.DockerClient(base_url=getDockerURL())

        container = client.containers.get(containerID)
        launcher.updateStatus('Removing the container.  Please wait...')
        container.remove()
        launcher.updateStatus('Container removed.')
            
        client.close()                    

        return True
    
    except Exception as err:
        launcher.updateStatus(str(err))
        print(str(err))


# Try to start the container.
launcher = None
window = None
try:
    
    # Initialize the Launcher window
    window = tk.Tk()
    
    if not hasConfig():
        settings = Settings(window)
    else:
        launcher = Launcher(window)
        startup(False)
    
    #startup()

except Exception as err:
    if launcher:
        launcher.updateStatus(str(err))
    print(str(err))

# Start the event loop
window.mainloop()


