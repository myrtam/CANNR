"""
CANNR TM tool core functions.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import json
import os
import sys
import importlib.util
import traceback
from datetime import datetime
import re
import shutil
import tempfile
import hashlib
import uuid
import logging

# TODO:  NEED TO NOTE IN DOCS THAT THIS PKG HAS TO BE INSTALLED.
from stdlib_list import stdlib_list


# Error messages & codes
noDirectorySpecMsg = "No working directory specified"
noDirectorySpecCode = 1001
        
noDirectoryMsg = "Working directory does not exist"
noDirectoryCode = 1002

noProjectNameMsg = "No project name specified"
noProjectNameCode = 1003

invalidProjectMsg = "Invalid or missing project"
invalidProjectCode = 1004

invalidContextMsg = "Invalid context"
invalidContextCode = 1005

noBaseImageMsg = "No base image"
noBaseImageCode = 1006

noFolderMsg = "No folder"
noFolderCode = 1007

noSourceInfoMsg = "No source information"
noSourceInfoCode = 1008

badSourceTypeMsg = "Invalid source type"
badSourceTypeCode = 1009

noSourcePathMsg = "No source path"
noSourcePathCode = 1010

errorCopyingSourceMsg = "Error copying source files"
errorCopyingSourceCode = 1011

folderPathErrorMsg = "Error creating folder path"
folderPathErrorCode = 1012

calendarLoadErrorMsg = "Error loading event calendar"
calendarLoadErrorCode = 1013

calendarWriteErrorMsg = "Error writing event calendar"
calendarWriteErrorCode = 1014

missingSourceFileNameMsg = "Missing source file"
missingSourceFileNameCode = 1015

invalidEventCalendarDirMsg = "Missing or invalid event calendar directory"
invalidEventCalendarDirCode = 1016

portOutOfRangeMsg = "Port out of range"
portOutOfRangeCode = 1017

# Base class for exceptions
class Error(Exception):
    pass

# Exception class for generation and processing related errors
# Attributes:
# message -- Explanation of the error
# errorCode -- Numeric code associated with the error
class RTAMError(Error):

    def __init__(self, message, errorCode):
        self.message = message
        self.errorCode = errorCode


# Represents the event calendar used to manage services
class EventCalendar():
    
    # Creates an empty calendar
    def __init__(self):
        self.calendar = []
    
    # Creates a calendar from a JSON string
    def __init__(self, **kwargs):
        try:
            self.calendar = []
            jsonString = kwargs.get('jsonString', None)
            if jsonString:
                self.calendar = json.loads(jsonString).get('calendar', [])
        except:
            raise RTAMError(calendarLoadErrorMsg, calendarLoadErrorCode)
    
    # Returns a dictionary containing the calendar
    def getCalendar(self):
        return self.calendar
    
    # Returns a JSON version of the calendar
    def toString(self):
        return json.dumps({"calendar": self.calendar})
    
    # Adds a new entry to the calendar
    def addEntry(self, time, action, object, priority):
        self.calendar.append({
            "time": time,
            "action": action,
            "object": object,
            "priority": priority
            })

    # Merges another calendar into the calendar
    def merge(self, calendar):
        self.calendar.extend(calendar.getCalendar())
        # Events with no time get the current time.
        now = datetime.now()
        for event in self.calendar:
            if not event.get('time', None):
                event['time'] = now
    
    # Reads a file containing a calendar and merges it into the calendar.
    def read(self, filePath):
        try:
            with open(filePath, "r") as calendarFile:
                self.merge(EventCalendar(jsonString=calendarFile.read()))
        except:
            raise RTAMError(calendarLoadErrorMsg, calendarLoadErrorCode)
        
    # Writes the calendar into a temp file in a directory.
    def write(self, directoryPath):
        try:
            fd, temp_path = tempfile.mkstemp(suffix='.json', dir=directoryPath, text=True)
            os.write(fd, self.toString().encode('utf-8'))
            os.close(fd)
        except:
            raise RTAMError(calendarWriteErrorMsg, calendarWriteErrorCode)
    
    # Returns the next calendar event to be processed and removes it from the calendar.
    def getNextEvent(self):
        
        # Events with no time get the current time.
        now = datetime.now()
        
        # Search through the events to find the one with the earliest time, with ties broken by priority
        minTimestamp = None
        maxPriority = 1000000
        nextEvent = None
        for event in self.calendar:
            timestamp = event.get('time', None)
            if not timestamp:
                timestamp = now
                event['time'] = timestamp
            if not minTimestamp or timestamp < minTimestamp:
                minTimestamp = timestamp
                maxPriority = event.get('priority', 1)
                nextEvent = event
            elif timestamp == minTimestamp and event.get('priority', 1) > maxPriority:
                maxPriority = event.get('priority', 1)
                nextEvent = event

        if nextEvent:
            self.calendar.remove(nextEvent)

        return nextEvent

    # Returns the earliest timestamp in the event calendar.  Does not return the event from the calendar.
    def getNextEventTime(self):

        minTimestamp = None
        now = datetime.now()
        for event in self.calendar:
            timestamp = event.get('time', None)
            if not timestamp:
                timestamp = now
                event['time'] = timestamp
            if not minTimestamp or timestamp < minTimestamp:
                minTimestamp = timestamp
                
        return minTimestamp


# Import a module from its file path
# Returns the module, which must be assigned to a variable to be used.
def importPackage(packageName, filePath):

    packageSpec = importlib.util.spec_from_file_location(packageName, filePath.replace('/', os.path.sep))
    module = importlib.util.module_from_spec(packageSpec)
    packageSpec.loader.exec_module(module)
    return module


# Tests whether a package is one of the standard packages provided with Python.
stdPkgSet = frozenset(stdlib_list(str(sys.version_info[0]) + '.' + str(sys.version_info[1])))
def isStdPkg(packageName):
    
    return packageName in stdPkgSet


# Returns the library path
def getLibPath():
    libPathLen = __file__.rfind(os.path.sep)
    libPath = os.path.sep
    if libPathLen > 0:
        libPath = __file__[:libPathLen]
    return libPath


# Tests whether a Python package is installed in the base image
jsonText = None
with open(getLibPath() + os.path.sep + 'packageList.json','r') as jsonFile:
    jsonText = jsonFile.read()
instPkgSet = set(json.loads(jsonText).get('packages', []))
def isInstPkg(packageName):
    
    return packageName in instPkgSet


# Tests whether an R package has already been installed
jsonText = None
with open(getLibPath() + os.path.sep + 'rPackageList.json','r') as jsonFile:
    jsonText = jsonFile.read()
rInstPkgSet = set(json.loads(jsonText).get('packages', []))
def isRInstPkg(packageName):
    
    return packageName in rInstPkgSet


# Resets the timestamp
def setLogFile(context):
    
    now = datetime.now()
    lastLogTime = context.get('lastLogTime', None)
    if not lastLogTime or lastLogTime < now:
        lastLogTime = now
        context['lastLogTime'] = lastLogTime
        logDirectoryName = context.get('logDirectoryName', 'logs')
        logFilePath = logDirectoryName + os.path.sep + datetime.now().isoformat(sep='_').replace(':','.') + '.log'
        loggingLevel = context.get('loggingLevel', 'INFO')
        logging.basicConfig(filename=logFilePath, filemode='w', level=loggingLevel,
            format='%(asctime)s %(levelname)s: %(message)s')

# Cryptographically hash a password
def hashPassword(password, salt, hashAlgorithm):
    
    h = hashlib.sha256()
    salted = salt + password
    h.update(salted.encode('utf-8'))

    return h.hexdigest().upper()
    
# Cryptographically hash a password
def buildHash(password, hashAlgorithm):
    
    salt = str(uuid.uuid4())
    hash = hashPassword(password, salt, hashAlgorithm)
    
    return {"hashAlgorithm": hashAlgorithm, "salt": salt, "hash": hash}
    
# Authenticate the user by checking their password against a given hash,
# password, hash algorithm and salt.  Currently, SHA256 is the only supported algorithm.
def authenticate(password, hashAlgorithm, hash, salt):
    
    return hashPassword(password, salt, hashAlgorithm)==hash
    
# Reads a project file, returns a dictionary for the project.
def readJSONFile(filePath):
    
    # Get the reference data
    with open(filePath,'r') as jsonFile:
        jsonText = jsonFile.read()
    return json.loads(jsonText)

# Returns the folders in the project.
def getFolders(project):
    return project.get("folders", None)

# Returns the folder with name folderName.
def getFolder(folderName, project):
    folders = getFolders(project);
    if not folders:
        return None
    return (folders.get(folderName, None))

# Returns the folder names (keys) of the folders in a project.
def getFolderNames(project):
    folders = getFolders(project);
    if not folders:
        return None
    return folders.keys()

# Returns the modules in a folder.
def getModules(folder):
    return folder.get("modules", None)
    
# Returns a module from a folder.
def getModule(moduleName, folder):
    modules = getModules(folder)
    if not modules:
        return None
    return modules.get(moduleName, None)

# Returns the module names (keys) of the modules in a folder.
def getModuleNames(folder):
    modules = getModules(folder)
    if not modules:
        return None
    return modules.keys()

# Returns the services in a module.
def getServices(module):
    return module.get("services", None)
    
# Returns the service names (keys) of the services in a module.
def getServiceNames(module):
    services = getServices(module)
    if not services:
        return None
    return services.keys()
    
# Returns the services in a module.
def getService(serviceName, module):
    services = getServices(module)
    if not services:
        return None
    return services.get(serviceName, None)

# Extracts the module name from the file name.
# TODO:  REMOVE!  NO LONGER USED
comp = None
def getModuleNameFromFile(fileName):

    global comp
    if not comp:
        comp = re.compile('^.*(?=\.\w+$)')
    result = comp.match(fileName)
    if result:
        return comp.match(fileName).group(0)
    return fileName

# Get port to use.
def getPort():
    return int(sys.argv[1])

# Get relative folder name from full path.
def getRelativePath(filePath):
    folders = filePath.split(os.path.sep)
    if len(folders) > 1:
        return folders[len(folders)-1]
    if len(folders) == 1:
        return folders[0]
    return None

# Get the home directory of the folder in the container.
# TODO: HANDLE OTHER TYPES OF STORAGE (Web, S3, etc.)
def getHome(folderName, folder):
    source = folder.get("source", None)
    folderPath = os.path.sep + 'folders' + os.path.sep + folderName + os.path.sep
    if not source:
        return folderPath + 'home'
    path = source.get("sourcePath", None)
    if not path:
        return folderPath + 'home'
    return folderPath + getRelativePath(path.replace('/', os.path.sep))

# Saves the project to the specified file path.
# If a password is specified, populates the password hash/salt and deletes the password.
# Returns True if saved successfully, False otherwise.
# Fails if insufficient authentication information:
# * Project must contain an authentication object.
# * authentication object must have either a password or password salt.
# * If password specified, it will be omitted from the saved project and hash/salt will be populated.
# * Password will be checked against regex authPolicy, save will fail if no match.
# Return codes:
# 0 - OK
# 1 - No authentication object
# 2 - No password or salt
# 3 - Password violates policy
# 4 - Problem saving project
def saveProject(project, filePath, authPolicyLen, authPolicyChars):

    try:
        
        # Check for authentication object.
        authentication = project.get('authentication', None)
        if not authentication:
            return 1
        
        # Check for password or salt.
        password = authentication.get('password', None)
        salt = authentication.get('salt', None)
        if not password and not salt:
            return 2
    
        # Validate password
        # * Length sufficient
        # * No whitespace
        # * Contains one of each set of chars in authPolicy array
        if password:
            # Check for length and whitespace
            if len(password) < authPolicyLen or re.search('\s', password):
                return 3
            for pattern in authPolicyChars:
                if not re.search(pattern, password):
                    return 3
        
        # Hash the password and update the project object.
        hashInfo = buildHash(password, 'SHA256')
        project['authentication'] = {
            'adminID': authentication.get('adminID', 'admin'),
            'hashAlgorithm': 'SHA256',
            'hash': hashInfo.get('hash', None),
            'salt': hashInfo.get('salt', None)
            }
        
        print(filePath)
        # Write out project file to the project directory
        with open(filePath, 'w') as projectFile:
            projectFile.write(json.dumps(project))

    # If anything else goes wrong.                
    except:
        return 4
    
    return 0

"""
project = readJSONFile('../../../../examples/project1/project.json')
context = readJSONFile('../../../runtime/context.json')
authPolicy = context.get('authPolicy')
authPolicyLen = authPolicy.get('authPolicyLen')
authPolicyChars = authPolicy.get('authPolicyChars')
authentication = {
    'password': '123456',
    'adminID': 'IRule'
    }
project['authentication'] = authentication
result = saveProject(project, '/Users/ptendick/Documents/GitHub/CANNR/test/project1.json', authPolicyLen, authPolicyChars)
"""


