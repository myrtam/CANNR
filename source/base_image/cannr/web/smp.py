"""
CANNR TM analytics container building tool system management process functions.
Module of supporting functions for the Service Management Process (SMP).
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import json
from datetime import datetime
from datetime import timedelta
import sys
import os
from os import path
import pathlib
import time
import subprocess
import logging
import requests

import cannrcore as cnr

# Event handlers
handlers = {}

# Open a process
def openProcess(processInfo, args):
    
    # Open the process
    process = subprocess.Popen(args,
        stdin =subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        universal_newlines=True,
        bufsize=0)        

    # Record the information about the process
    processDict = {
        'processInfo': processInfo,
        'process': process
        }
    
    return processDict

# Count the number of ports required by the project
def countPorts(project):
    
    ports = 0
    folders = project.get('folders', None)
    
    if folders:
        for folder in folders.values():
            if folder.get('language', 'Python') == 'R' and folder.get('modules', None):
                modules = folder.get('modules', None)
                for module in modules.values():
                    ports += module.get('workers', 1)
            else:
                ports += folder.get('workers', 1)
                
    return ports

# Starts all workers
def startWorkers(context):
    
    projectFilePath = context.get('projectFilePath','/project.json')
    cannrHome = context.get('cannrHome', '/cannr')
    foldersPath = '/'
    
    try:
    
        project = cnr.readJSONFile(projectFilePath)
        if project:            
            
            # Get port info
            portRange = project.get('portRange', [5000,10000])
            port = portRange[0]
            maxPort = portRange[1]
            numPorts = maxPort - port

            # Check if there are enough ports
            if countPorts(project) > numPorts:
                logging.error('Not enough ports:', numPorts)
                return False
            
            # Go through the folders and start worker processes
            rProcesses = context.get('rProcesses')
            pProcesses = context.get('pProcesses')
            folders = project.get('folders', None)
            for folderName in folders:
                folder = folders.get('folderName', {})
                folderPath = cnr.getFolderPath(foldersPath, folderName)
                if folder.get('language', 'Python') == 'R' and folder.get('modules', None):
                    modules = folder.get('modules', None)
                    for moduleName in modules:
                        try:
                            module = modules.get(moduleName)
                            path = folderPath + os.path.sep + moduleName + '.R'
                            
                            # Add workers
                            workers = folder.get('workers', 1)
                            for workerNum in range(workers):
                                processInfo = {
                                    'path': path,
                                    'port': port,
                                    'folder': folderName,
                                    'module': moduleName,
                                    'workerNum': workerNum
                                    }
                                # Record the information about the process and save it in the context
                                rProcess = openProcess(processInfo,
                                    ['Rscript', '--vanilla', cannrHome + os.path.sep + 'runApp.R', path, str(port), str(workerNum)])
                                rProcesses.append(rProcess)
                                port += 1
                
                                # Log that the process was started
                                logging.info('R worker for module ' + moduleName + ' in folder '
                                    + folderName + ' started on port ' + str(port))
                        
                        except Error as err:
                            # Log error
                            logging.exception('Error starting R worker for module ' + moduleName + ' in folder '
                                + folderName + ' on port ' + str(port) + ':', err)
                        
                else:
                    try:
                        
                        path = folderPath + os.path.sep + folderName + ".py"
                            
                        # Add workers
                        workers = folder.get('workers', 1)
                        for workerNum in range(workers):
                            processInfo = {
                                'path': path,
                                'port': port,
                                'folder': folderName,
                                'workerNum': workerNum
                                }
    
                            # Record the information about the process and save it in the context
                            pProcess = openProcess(processInfo, ['python', path, str(port), str(workerNum)])
                            context.get('pProcesses').append(pProcess)                        
                
                            port += 1
                
                            # Log that the process was started
                            logging.info('Python worker for folder ' + folderName
                                + ' started on port ' + str(port))
                    
                    except Error as err:
                        # Log error
                        logging.exception('Error starting Python worker for folder '
                            + folderName + ' on port ' + str(port) + ':', err)
            
            return True
            
        else:
            # Log error
            logging.error('Unable to start workers: Missing configuration')
     
    except Error as err:
        # Log error
        logging.exception('Error starting workers:', err)

    return False


# Start the service management interface
def startSMI(processInfo, context):
    
    try:
    
        if processInfo:    
        
            # TODO: ADD FLAG FOR TLS BASED ON THE smiTLS PARAMETER
            # Record the information about the SMI process and save it in the context
            smiProcess = openProcess(processInfo, ['python', processInfo.get('path'), processInfo.get('port')])
            context['smiProcess'] = smiProcess
            
            return True
            
        else:
            # Log error
            logging.error('Unable to start SMI process: Missing configuration')
     
    except:
        # Log error
        logging.exception('Error starting SMI process')

    return False

# Start NGINX    
def startNGINX(context):

    try:
    
        # Log that the process was started
        logging.info('Starting load balancer')

        # Record the information about the NGINX process and save it in the context
        nginxProcess = openProcess(processInfo, ['nginx'])
        context['nginxProcess'] = nginxProcess
        
        return True
        
    except:
        # Log error
        logging.exception('Error starting load balancer process')

    return False


# Handler for event that starts workers and NGINX
def startup(calendarEntry, context):
    return startWorkers(context) and startNGINX(context)


# Check whether a process has terminated.  If not, returns False.  If so, logs event and returns True.
# Logs both stdout and stderr as appropriate.
def checkProcess(process, message):
    
    if process:
        code = process.poll()
        if code is not None:
            logMessage = message + '\n'
            for output in process.stdout.readlines():
                logMessage += output.strip() + '\n'
            for output in process.stderr.readlines():
                logMessage += output.strip() + '\n'
            if code != 0:
                logging.error(logMessage)
            else:
                logging.info(logMessage)
    
            return True
    
    return False

# Monitor processes to see if they have terminated.  If so, logs stdout & stderr and returns True.
def monitor(calendarEntry, context):
    
    cnr.setLogFile(context)
    
    rProcesses = context.get('rProcesses')
    pProcesses = context.get('pProcesses')
    smiProcess = context.get('smiProcess', None)
    nginxProcess = context.get('nginxProcess', None)
    
    stopped = True
    
    if smiProcess:
        if checkProcess(smiProcess, 'SMI process has terminated.'):
            context['smiProcess'] = None
        else:
            stopped = False            
    
    if nginxProcess:
        if checkProcess(nginxProcess, 'NGINX process has terminated.'):
            context['nginxProcess'] = None
        else:
            stopped = False            

    for rProcess in rProcesses:
        process = rProcess.get('process', None)
        if checkProcess(process, 'R worker for module ' + object.get('module', 'unknown')
            + ' in folder ' + object.get('folder', 'unknown') + ' on port '
            + str(object.get('port',0)) + ' has terminated.'):
            rProcess['process'] = None
        else:
            stopped = False            
    
    for pProcess in pProcesses:
        process = pProcess.get('process', None)
        if checkProcess(process, 'Python worker for folder ' + object.get('folder', 'unknown')
            + ' on port ' + str(object.get('port',0)) + ' has terminated.'):
            pProcess['process'] = None
        else:
            stopped = False            
    
    # Schedule the next monitor event to be one second in the future.
    if not stopped:
        eventCalendar = context.get('eventCalendar')
        monitorInterval = context.get('monitorInterval', 1)
        eventCalendar.addEntry(datetime.now() + timedelta(seconds=monitorInterval), 'monitor', None, 1)
    
    return stopped

# Stop NGINX    
def stopNGINX(calendarEntry, context):

    stopped = False
    try:
    
        # Log that the load balancer is being stopped
        logging.info('Stopping the load balancer...')

        # Length of time we're willing to wait for process to exit
        nginxStopInterval = context.get('nginxStopInterval', 10)

        # Tell NGINX to stop gracefully
        quitProcess = openProcess(calendarEntry, ['nginx', '-s', 'quit'])

        # Wait for NGINX to quit, up to a max of say 10 seconds 
        stopTime = datetime.now() + timedelta(seconds=nginxStopInterval)
        while datetime.now() < stopTime:
            # Sleep to reduce CPU
            time.sleep(0.05)
            if checkProcess(quitProcess, 'Load balancer exited normally.'):
                stopped = True
                break
        
        if not stopped:
            # If not stopped, tell NGINX to stop immediately
            quitProcess = openProcess(calendarEntry, ['nginx', '-s', 'stop'])
    
            # Wait for NGINX to quit, up to a max of say 10 seconds 
            stopTime = datetime.now() + timedelta(seconds=nginxStopInterval)
            while datetime.now() < stopTime:
                # Sleep to reduce CPU
                time.sleep(0.05)
                if checkProcess(quitProcess, 'Load balancer forced to exit.'):
                    stopped = True
                    break
                    
        # Log any final output of the NGINX process.
        if stopped:
            nginxProcess = context.get('nginxProcess', None)
            process = nginxProcess.get('process', None)
            if process:
                while not checkProcess(process, 'Load balancer stopped.'):
                    # Sleep to reduce CPU
                    time.sleep(0.05)
                nginxProcess['process'] = None
        
    except:
        # Log error
        logging.exception('Error stopping the load balancer.')

    if not stopped:
        logging.warning('Unable to shut down the load balancer.')

    return stopped

# Stop all plumber workers. Returns True if all workers stopped, False otherwise.
def stopPlumber(calendarEntry, context):
    
    stopped = True
    rProcesses = context.get('rProcesses', [])
    for rProcess in rProcesses:
        try:
            calendarEntry = rProcess.get('calendarEntry', {})
            object = calendarEntry.get('object', {})
            logging.info('Stopping R worker for module ' + object.get('module', 'unknown') + ' in folder '
                + object.get('folder', 'unknown') + ' on port ' + str(object.get('port',0)))
            process = rProcess.get('process', None)
            if process:
                outs = None
                errs = None
                try:
                    # Send <ESC> character (\x1b) to Plumber.
                    outs, errs = process.communicate('\x1b', timeout=2)
                # If don't get response in 2 seconds, kill the process.
                except TimeoutExpired:
                    process.kill()
                    outs, errs = process.communicate()
                # Log output
                if outs:
                    logging.info(outs)
                # Log errors
                if errs:
                    logging.error(outs)

                logging.info('R worker for module ' + object.get('module', 'unknown') + ' in folder '
                    + object.get('folder', 'unknown') + ' on port ' + str(object.get('port',0)) + ' stopped.')
        
        except:
            logging.error('Error stopping R worker for module ' + object.get('module', 'unknown') + ' in folder '
                + object.get('folder', 'unknown') + ' on port ' + str(object.get('port',0)))
            stopped = False

    return stopped    

# Stop all Flask workers. Returns True if all workers stopped, False otherwise.
def stopFlask(calendarEntry, context):
    
    stopped = True
    pProcesses = context.get('pProcesses', [])
    for pProcess in pProcesses:
        try:
            calendarEntry = pProcess.get('calendarEntry', {})
            object = calendarEntry.get('object', {})
            folderName = object.get('folder', 'unknown')
            logging.info('Stopping Python worker for folder '
                + folderName + ' on port ' + str(object.get('port',0)))
            process = pProcess.get('process', None)
            if process:
                response = requests.post(
                    'http://localhost:' + str(object.get('port',0)) + '/shutdown/' + folderName,
                    data={}, timeout=10)
                logging.info('Python worker for folder '
                    + folderName + ' on port ' + str(object.get('port',0)) + ' stopped.')

        except:
            logging.error('Error stopping Python worker for folder '
                + object.get('folder', 'unknown') + ' on port ' + str(object.get('port',0)))
            stopped = False

    return stopped    

# Shuts down everything.  Returns True if everything shut down normally, False otherwise.
def shutDown(calendarEntry, context):
    
    stopped = True
    
    if not stopNGINX(calendarEntry, context):
        stopped = False
    
    if not stopPlumber(calendarEntry, context):
        stopped = False
    
    if not stopFlask(calendarEntry, context):
        stopped = False
    
    return stopped

# Refresh objects in a module given the module name, folder name, object store info, and context.
def refreshModule(moduleName, folderName, objectStoreInfo, context):
    
    # Get the folders
    folders = project.get('folders')
    if not folders:
        return False
    
    # Get the folder and module
    folder = folders.get(folderName, {})
    modules = folder.get('modules', {})
    module = modules.get(moduleName, {})
    
    objectStoreName = module.get('objectStoreName', None)
    if not objectStoreName:
        return False
    
    # Get the applicable objectStoreInfo info, add the node number if applicable
    storeInfo = module.get('objectStoreInfo', None)
    if storeInfo:
        storeInfo['nodeNumber'] = module.get('nodeNumber', 1)
    else:
        storeInfo = objectStoreInfo

    # Get the list of processes to use
    if folder.get('language', 'Python') == 'Python':
        processes = context.get('pProcesses')
    else:
        processes = context.get('rProcesses')
    
    # Loop through processes, refresh those that match the folder and module
    for process in processes:
        processInfo = process.get('processInfo')
        if processInfo.get('folder') == folderName and processInfo.get('module') == moduleName:
            data = {
                'objectStoreInfo': storeInfo,
                'objectStoreName': objectStoreName
                }
            portString = str(processInfo.get('port',0))
            response = requests.post(
                'http://localhost:' + portString + '/refreshObjects/' + folderName + '/' + moduleName,
                data=data)
            logging.info('Objects in module ' + moduleName + ' in folder '
                + folderName + ' on port ' + portString + ' refreshed.')

    return True

# Refresh objects in a folder given the folder name, object store info, and context.
def refreshFolder(folderName, objectStoreInfo, context):

    # Get the folders
    folders = project.get('folders')
    if not folders:
        return False
    
    # Get the folder and module
    folder = folders.get(folderName, {})

    # Loop through the modules in the folder and refresh them.
    modules = folder.get('modules', {})
    for moduleName in modules:
        refreshModule(moduleName, folderName, storeInfo, context)
        
    return True


# Refreshes objects
# Object contains elements that describe its scope:
# * folderName - specifies that the scope is limited to a folder
# * moduleName - If folder is specified, specifies that the scope is limited to a module within the folder
# * If no folder or module are specified, scope is entire project
def refreshObjects(calendarEntry, context):
    
    project = context.get('project')
    if not project:
        return False
    
    objectStoreInfo = project.get('objectStoreInfo', None)
    if objectStoreInfo:
        objectStoreInfo['nodeNumber'] = project.get('nodeNumber', 1)
    object = calendarEntry.get('object', {})
    folderName = object.get('folderName', None)
    moduleName = object.get('moduleName', None)
    
    if folderName:
        storeInfo = folder.get('objectStoreInfo', None)
        if storeInfo:
            storeInfo['nodeNumber'] = folder.get('nodeNumber', 1)
        else:
            storeInfo = objectStoreInfo
        if moduleName:
            folders = project.get('folders', {})
            folder = folders.get(folderName, {})
            refreshModule(moduleName, folderName, storeInfo, context)
        else:
            refreshFolder(folderName, storeInfo, context)
    else:
        folders = project.get('folders', {})
        for folderName in folders:
            refreshFolder(folderName, objectStoreInfo, context)
            
    return True
    

# Event handlers
handlers = {}
#handlers['startPlumber'] = startPlumber
#handlers['startFlask'] = startFlask
#handlers['stopPlumber'] = stopPlumber
#handlers['stopFlask'] = stopFlask
#handlers['startSMI'] = startSMI
handlers['startup'] = startup
#handlers['startNGINX'] = startNGINX
#handlers['stopNGINX'] = stopNGINX
handlers['shutDown'] = shutDown
handlers['monitor'] = monitor
handlers['refreshObjects'] = refreshObjects

# Process an event calendar entry
def processEntry(calendarEntry, context):
    
    # Get the event type
    eventType = calendarEntry.get('action', None)
    
    # Try to match the event type to a handler
    if eventType:
        handler = handlers.get(eventType, None)
        # If a handler is found, execute it and return the result
        if handler:
            return handler(calendarEntry, context)
            
    return False

# Process events in the event calendar
def processContext(context):

    # Get the event calendar from the context
    eventCalendar = context.get('eventCalendar')

    # Loop through the calendar until caught up or done.
    nextEventTime = eventCalendar.getNextEventTime()
    while nextEventTime and nextEventTime <= datetime.now():

        # Get the next entry
        calendarEntry = eventCalendar.getNextEvent()
        print(calendarEntry.get('time', None))
        
        # Process the entry
        done = processEntry(calendarEntry, context)
        
        # If done, stop
        if done:
            return True

        nextEventTime = eventCalendar.getNextEventTime()


# Returns a list of calendar file names, ordered by file timestamp
def getCalendarFiles(eventCalendarDir):

    fileList = []
    
    # Get the file names and timestamps
    dir = pathlib.Path(eventCalendarDir)
    for filePath in dir.iterdir():
        print(filePath)
        newFile = {'filePath': filePath, 'timestamp': os.path.getmtime(filePath)}
        fileList.append(newFile)

    # Sort the files by timestamp, increasing
    sortedList = sorted(fileList, key = lambda t: t['timestamp'])
    
    # Put the filenames in a list, in order
    files = []
    for file in sortedList:
        files.append(file.get('filePath', None))
    
    # Return the sorted list of filenames
    return files
        

# Deletes files in a given list of filenames
def delFiles(eventCalendarDir, files):
    for filePath in files:
        os.remove(filePath)
    
    
# Main program.

# Read command line arguments:
# 1. Project file path
# 2. Event calendar directory
#projectFilePath = sys.argv[1]
#eventCalendarDir = sys.argv[2]

'''
Initialization:
1. Read project file and initialize context
2. Check whether SMI should be started.  If yes
    a. Start SMI
    b. Check whether startup should be delayed pending initial configuration
    c. If yes to b
        i.    Wait until configuration complete
        ii.   Reload project file
        iii.  Check if refresh of objectstores required
        iv.   Start workers
        v.    If yes to iii, refresh objects
       else
        i.    Start workers
3.  Start NGINX
4.  Start monitoring
5.  Start main loop

Initial configuration:
* Performed before service startup
* Specify number of workers per folder or module
* Change SMI username/password
* Specify location information for objectstores
* Specify credentials for objectstores

Runtime reconfiguration:
* Available after service startup
* Change SMI username/password
* Specify location information for objectstores
* Specify credentials for objectstores
'''

"""
#projectFilePath = '/project.json'
projectFilePath = '/Users/ptendick/open-source-workspace/MyRTAM Service/working/project1/project.json'

#eventCalendarDir = '/eventCalendar'
eventCalendarDir = '/Users/ptendick/open-source-workspace/MyRTAM Service/working/project1/eventCalendar'

# cannrHome = '/cannr'
cannrHome = '/Users/ptendick/open-source-workspace/MyRTAM Service/cannr'

#if not cannr.existsDirectory(eventCalendarDir):
#    raise RTAMError(invalidEventCalendarDirMsg + (': ' + eventCalendarDir if eventCalendarDir else ''),
#        cannr.invalidEventCalendarDirCode)

# Initialize the event calendar
eventCalendar = cannr.EventCalendar()

try:
    # Read project file
    project = cannr.readJSONFile(projectFilePath)
except Error as err:
    # If error, we're done
    logging.exception(err)
    sys.exit(1)
    
if not project:
    # If no project, we're done
    logging.error(cannr.invalidProjectMsg)
    sys.exit(1)

# R processes that have been started
rProcesses = []

# Python processes that have been started
pProcesses = []

# Context of the SMP
context = {
    'eventCalendar': eventCalendar,
    'projectFilePath': projectFilePath,
    'project': project,
    'eventCalendarDir': eventCalendarDir,
    'cannrHome': cannrHome,
    'rProcesses': rProcesses,
    'pProcesses': pProcesses,
    'monitorInterval': 1
    }


# Handle case that SMI is enabled
enableSMI = project.get('enableSMI', False)
configOnStartup = project.get('configOnStartup', False)
if enableSMI:
    processInfo = {
        'path': cannrHome + '/usr/local/cannr/web/smi.py',
        'port': project.get('smiPort', 8080)
        }
    startSMI(processInfo, context)

# If SMI not enabled or configuration on startup not enabled, start
# workers and NGINX immediately.  Otherwise, have to wait for event
# from SMI.
if not enableSMI or not configOnStartup:
    if not startup({}, context):
        logging.error('Startup failed')
        sys.exit(1)


# Main loop
done = False
while not done:
    
    # Get list of json files in eventCalendar directory ordered by file timestamp.
    files = getCalendarFiles(context.get('eventCalendarDir'))
    
    # Loop through json files.
    for filePath in files:
        
        try:
            eventCalendar.read(filePath)
            done = processContext(context)
        except:
            # TODO: LOG ERROR
            pass
    
    # Delete the calendar files
    delFiles(context.get('eventCalendarDir'), files)
    
    # Wait
    print('Sleeping...')
    time.sleep(0.05)

"""
