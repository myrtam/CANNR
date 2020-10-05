"""
CANNR TM analytics container building tool build functions.
Module that generates Web service code from source files.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""


import cannrcore as cc
import json
import os
from pathlib import Path
from datetime import datetime
import shutil


# Returns the Dockerfile template
def getDockerfile():
    libPathLen = __file__.rfind(os.path.sep)
    libPath = os.path.sep
    if libPathLen > 0:
        libPath = __file__[:libPathLen]
    with open(libPath + os.path.sep + 'Dockerfile', "r") as dockerFile:
        return dockerFile.read()

# Generate a line of code given the indent and list of terms
def buildCodeLine(indent, content):
    
    codeLine = indent*'\t'
    for term in content:
        codeLine += term
        
    return codeLine + '\n'

# Generates the Python file for a Python folder.
# Usage is 
# $ python app.py <port>
def buildPyFolder(folderName, project):
    
    # TODO: ADD ERROR HANDLING.  LOG?
    
    # Get the copyright/license notice for the project.
    projectNotice = project.get("notice", None)
    
    # Get the folder from the folder name.
    folder = cc.getFolder(folderName, project)
    if not folder:
        return None
    
    # Get all the module names.
    moduleNames = cc.getModuleNames(folder)
    if not moduleNames:
        return None
    
    # Start with empty module.
    moduleText = ''

    # Add the file header.
    moduleText += buildCodeLine(0, ['"""'])
    # TODO: NEED TO HANDLE CASE THAT THERE ARE LINE BREAKS IN THE NOTICE.
    if projectNotice:
        moduleText += buildCodeLine(0, [projectNotice])
    moduleText += buildCodeLine(0, ['Generated ', datetime.now().isoformat(sep=' ', timespec='seconds')])
    moduleText += buildCodeLine(0, ['"""'])
    
    # Add basic imports that are always included.
    moduleText += buildCodeLine(0, ['import json'])
    moduleText += buildCodeLine(0, ['import os'])
    moduleText += buildCodeLine(0, ['import sys'])
    moduleText += buildCodeLine(0, ['import logging'])
    moduleText += buildCodeLine(0, ['import uuid'])
    moduleText += buildCodeLine(0, ['import pandas'])
    moduleText += buildCodeLine(0, ['from flask import Flask, render_template, request'])

    # Import utilities.
    #moduleText += 'sys.path.append("/usr/local/cannr/lib")\n'
    moduleText += buildCodeLine(0, ['import cannrcore as cnr'])
    #moduleText += buildCodeLine(0, ['import cannrshut'])
    #moduleText += buildCodeLine(0, ['import cannrmet'])

    # Change to the folder home.
    moduleText += '\n'
    
    # Add paths to search for dependent modules.
    # Loop through paths, add.
    folderPath = '/folders/' + folderName
    relativePath = cc.getRelativePath(folder['source']['sourcePath'].replace(os.path.sep, '/'))
    paths = folder.get('paths', None)
    if paths:
        for path in paths:
            moduleText += buildCodeLine(0, ['sys.path.append("',  folderPath, '/', relativePath, '/', path, '")'])

    # Change to the folder home.
    moduleText += '\n'
    moduleText += buildCodeLine(0, ['os.chdir("', cc.getHome(folderName, folder), '")'])
    
    # Build imports of modules. 
    # Add the imports.
    # Loop through modules, add import for each one.
    # TODO: THIS CAN CREATE A NAME COLLISION IF THE NAME OF A MODULE CONFLICTS WITH AN EXISTING PACKAGE
    # USE APPROACH IN https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    # INSTEAD
    moduleShortNames = {}
    moduleNum = 1
    for moduleName in moduleNames:
        module = cc.getModule(moduleName, folder)
        fileName = module.get('sourceFile', None)
        moduleFileName = folderPath + '/' + relativePath + '/' + fileName
        moduleShortName = 'm_' + str(moduleNum)
        moduleText += buildCodeLine(0, [moduleShortName, ' = ','cnr.importPackage("', moduleShortName, '", "', moduleFileName, '")'])
        moduleShortNames[moduleName] = moduleShortName
        moduleNum += 1
        # TODO: If no source file, error.
        # TODO: CHECK FOR LEGAL MODULE NAME.
        #importName = getModuleNameFromFile(fileName)
        # TODO: If no import name, error.
        #moduleText += buildCodeLine(0, ['import ', importName])

    # Create the Flask app object.
    moduleText += '\n'
    moduleText += buildCodeLine(0, ['app = Flask(__name__)'])
    moduleText += buildCodeLine(0, ['workerID = str(uuid.uuid4())'])
    moduleText += buildCodeLine(0, ['credentials = None'])
    moduleText += buildCodeLine(0, ['lastUpdateID = None'])
    moduleText += '\n'
    
    # Dispatcher to shut down the worker.
    moduleText += buildCodeLine(0, ['# Shut down the worker'])
    moduleText += buildCodeLine(0, ['@app.route("/shutdown/', folderName, '", methods=["POST"])'])
    moduleText += buildCodeLine(0, ['def shutdown():'])
    moduleText += buildCodeLine(1, ['shutdown.shutdown()'])
    moduleText += buildCodeLine(1, ['return "Shutting down..."'])

    # Build the wrappers.
    moduleText += '\n'
    functionNumber = 1
    moduleNumber = 1
    for moduleName in moduleNames:
        module = cc.getModule(moduleName, folder)
        serviceNames = cc.getServiceNames(module)
        
        
        for serviceName in serviceNames:
            service = cc.getService(serviceName, module)
            method = service.get('method', 'POST')
            function = service.get('function', 'POST')
            moduleText += buildCodeLine(0, ['# Service ', serviceName, ' in module ', moduleName])
            moduleText += buildCodeLine(0, ['@app.route("/services/', folderName, '/', moduleName, '/', serviceName, '", methods=["', method , '"])'])
            moduleText += buildCodeLine(0, ['def s_', str(functionNumber), '():'])
            functionNumber += 1
            # TODO: ADD METRICS.
            # TODO: ADD LOGGING.
            # TODO: THE FOLLOWING JUST PARSES THE QUERY PARAMETERS AND BODY TO AND FROM DICTIONARIES.  NEED TO HANDLE OTHER CASES.
            # TODO: CHECK FOR CAPACITY.  ONLY FOR Pandas DATAFRAMES.
            # TODO: json PACKAGE DOESN'T PARSE NUMPY DATA TYPES.  NEED TO SPECIFY NUMPY TO JSON TYPE CONVERTER AS default PARAMETER OF json.dumps.
            # SEE https://stackoverflow.com/questions/50916422/python-typeerror-object-of-type-int64-is-not-json-serializable/50916741
            # AND https://docs.python.org/3/library/json.html
            moduleText += buildCodeLine(1, ['parsedParams = request.args.to_dict()'])
            functionText = moduleShortNames[moduleName] + '.' + function
            if not service.get('includeParams', False):
                if method == 'POST':
                    #moduleText += buildCodeLine(1, ['parsedBody = json.loads(request.get_json())'])
                    moduleText += buildCodeLine(1, ['output = ', functionText, '(request.get_json())'])
                else:
                    moduleText += buildCodeLine(1, ['output = ', functionText, '()'])
            else:
                if method == 'POST':
                    #moduleText += buildCodeLine(1, ['parsedBody = json.loads(request.get_json())'])
                    moduleText += buildCodeLine(1, ['output = ', functionText, '(parsedParams, request.get_json())'])
                else:
                    moduleText += buildCodeLine(1, ['output = ', functionText, '(parsedParams)'])
            moduleText += buildCodeLine(1, ['parsedOutput = json.dumps(output)'])
            moduleText += buildCodeLine(1, ['return(parsedOutput)'])

        # Stub for refreshing objects in the module
        moduleText += '\n'
        moduleText += buildCodeLine(0, ['# Refresh objects in module ', moduleName])
        moduleText += buildCodeLine(0, ['@app.route("/refreshObjects/', folderName, '/', moduleName, '", methods=["POST"])'])
        moduleText += buildCodeLine(0, ['def refresh_', str(moduleNumber), '():'])
        moduleText += buildCodeLine(1, ['# TODO: STUB - TO BE ADDED'])
        moduleText += buildCodeLine(1, ['# TODO: PASS BACK workerID IN THE RESPONSE'])
        moduleText += buildCodeLine(1, ['return({})'])

        # Update credentials (e.g., for object store)
        moduleText += '\n'
        moduleText += buildCodeLine(0, ['# Update credentials in module ', moduleName])
        moduleText += buildCodeLine(0, ['@app.route("/updateCredentials/', folderName, '/', moduleName, '", methods=["POST"])'])
        moduleText += buildCodeLine(0, ['def updateCred_', str(moduleNumber), '():'])
        moduleText += buildCodeLine(1, ['parsedBody = json.loads(request.get_json())'])
        moduleText += buildCodeLine(1, ['updateID = parsedBody.get("updateID", None)'])
        moduleText += buildCodeLine(1, ['if updateID and updateID != lastUpdateID:'])
        moduleText += buildCodeLine(2, ['lastUpdateID = updateID'])
        moduleText += buildCodeLine(2, [''])
        moduleText += buildCodeLine(1, ['return({"workerID": workerID})'])
        moduleText += '\n'

        moduleNumber += 1

    moduleText += '\n'
    
    moduleText += buildCodeLine(0, ['# Run the app.'])
    moduleText += buildCodeLine(0, ['if __name__ == "__main__":'])
    # TODO: MODIFY TO ENABLE TLS ACCORDING TO argv[2]
    moduleText += buildCodeLine(1, ['app.run(host="0.0.0.0", port=int(sys.argv[1]))'])

    return moduleText


# Generates the R file for an R module.
def buildRModuleEpilogue(folderName, moduleName, project):
    
    # TODO: ADD ERROR HANDLING.  LOG?

    # Get the copyright/license notice for the project.
    projectNotice = project.get("notice", None)
    
    # Get the folder from the folder name.
    folder = cc.getFolder(folderName, project)
    if not folder:
        return None
    
    # Get all the module names.
    module = cc.getModule(moduleName, folder)
    if not module:
        return None
    
    # Start with empty module.
    moduleText = ''

    # Add the file header.
    moduleText += buildCodeLine(0, ['#'*80])
    # TODO: NEED TO HANDLE CASE THAT THERE ARE LINE BREAKS IN THE NOTICE.
    if projectNotice:
        moduleText += buildCodeLine(0, ['# ', projectNotice])
    moduleText += buildCodeLine(0, ['# Generated ', datetime.now().isoformat(sep=' ', timespec='seconds')])
    moduleText += buildCodeLine(0, ['#'*80])
    moduleText += '\n'
    
    moduleText += buildCodeLine(0, ['library(jsonlite)'])
    moduleText += buildCodeLine(0, ['library(urltools)'])
    moduleText += '\n'
    moduleText += buildCodeLine(0, ['workerID <- Sys.getenv("WORKER_ID")'])
    moduleText += buildCodeLine(0, ['credentials <- NULL'])
    moduleText += buildCodeLine(0, ['lastUpdateID <- NULL'])
    moduleText += '\n'
    
    # Build the wrappers.
    module = cc.getModule(moduleName, folder)
    serviceNames = cc.getServiceNames(module)
    for serviceName in serviceNames:
        service = cc.getService(serviceName, module)
        method = service.get('method', 'POST')
        function = service.get('function', 'ERROR')
        moduleText += buildCodeLine(0, ['# Service ', serviceName, ' in module ', moduleName, ' in folder ', folderName])
        moduleText += buildCodeLine(0, ["#' @", method.lower(), " /services/", folderName, "/", moduleName, "/", serviceName])
        moduleText += buildCodeLine(0, ['function(req) {'])
        
        if method == 'POST':
            moduleText += buildCodeLine(1, ['rawJSON <- req$postBody'])
            # TODO: THE FOLLOWING JUST PARSES THE QUERY PARAMETERS AND BODY TO AND FROM DATAFRAMES.  NEED TO HANDLE OTHER CASES.
            # TODO: CHECK FOR CAPACITY.  ONLY FOR DATAFRAMES.
            moduleText += buildCodeLine(1, ['listFromJSON <- fromJSON(rawJSON)'])
            moduleText += buildCodeLine(1, ['bodyInput <- as.data.frame(listFromJSON)'])
            input = service.get('input', {})
            capacity = input.get('capacity', None)
            if capacity:
                moduleText += buildCodeLine(1, ['if (nrow(bodyInput) > ', str(capacity),') {'])
                moduleText += buildCodeLine(2, ['return(data.frame(error = "Capacity exceeded"))'])            
                moduleText += buildCodeLine(1, ['}'])

        if not service.get('includeParams', False):
            if method == 'GET':
                moduleText += buildCodeLine(1, ['output <- ', function, '()'])
            else:
                moduleText += buildCodeLine(1, ['output <- ', function, '(bodyInput)'])
        else:
            moduleText += buildCodeLine(1, ['queryParams <- param_get(paste0("http://x.com/x", req$QUERY_STRING))'])

            if method == 'GET':
                moduleText += buildCodeLine(1, ['output <- ', function, '(queryParams)'])
            else:
                moduleText += buildCodeLine(1, ['output <- ', function, '(queryParams, bodyInput)'])
        moduleText += buildCodeLine(1, ['return(output)'])
        moduleText += buildCodeLine(0, ['}'])

    moduleText += '\n'    
    moduleText += buildCodeLine(0, ['# Refresh objects in module ', moduleName])
    moduleText += buildCodeLine(0, ["#' @post /refreshObjects/", folderName, '/', moduleName])
    moduleText += buildCodeLine(0, ['function(req) {'])
    moduleText += buildCodeLine(1, ['# TODO:  STUB'])
    moduleText += buildCodeLine(1, ['return'])
    moduleText += buildCodeLine(0, ['}'])

    # Update credentials (e.g., for object store)
    moduleText += '\n'    
    moduleText += buildCodeLine(0, ['# Update credentials in module ', moduleName])
    moduleText += buildCodeLine(0, ["#' @post /updateCredentials/", folderName, '/', moduleName])
    moduleText += buildCodeLine(0, ['function(req) {'])
    moduleText += buildCodeLine(1, ['rawJSON <- req$postBody'])
    moduleText += buildCodeLine(1, ['listFromJSON <- fromJSON(rawJSON)'])
    moduleText += buildCodeLine(1, ['updateID <- listFromJSON[["updateID"]]'])
    moduleText += buildCodeLine(1, ['if (updateID != lastUpdateID) {'])
    moduleText += buildCodeLine(2, ['lastUpdateID <- updateID'])
    moduleText += buildCodeLine(2, ['credentials <- listFromJSON[["credentials"]]'])
    moduleText += buildCodeLine(1, ['}'])
    moduleText += buildCodeLine(1, ['return(list("workerID" = workerID))'])
    moduleText += buildCodeLine(0, ['}'])

    return moduleText


# Checks whether the tool has a working directory.  Returns True if yes, throws exception otherwise.
def checkWorkingDirectory(context):
    # Check whether the tool has a working directory
    workingDirectory = context.get("workingDirectory", None)
    if not workingDirectory or not workingDirectory.get("path", None):
        raise cc.RTAMError(noDirectorySpecMsg, noDirectorySpecCode)
        
    path = workingDirectory.get("path")
    if not existsDirectory(path):
        raise cc.RTAMError(cc.noDirectoryMsg, cc.noDirectoryCode)

    return os.path.abspath(path)


# Test whether a directory exists.
def existsDirectory(path):
    return True if os.path.isdir(path) else False

# Returns the folder path.
def getFolderPath(foldersPath, folderName):
    try:
        return foldersPath.replace('/', os.path.sep) + os.path.sep + folderName
    except:
        raise cc.RTAMError(cc.folderPathErrorMsg, cc.folderPathErrorCode)

# Initializes the build by checking the context and project and creating the working directory,
def initBuild(project, context):

    # Check project & context.
    if not project or not isinstance(project,dict):
        raise cc.RTAMError(cc.invalidProjectMsg, cc.invalidProjectCode)

    if not context or not isinstance(context,dict):
        raise cc.RTAMError(cc.invalidContextMsg, cc.invalidContextCode)

    projectName = project.get("name", None)
    if not projectName:
        raise cc.RTAMError(cc.noProjectNameMsg, cc.noProjectNameCode)

    # Check whether the base image has been specified.
    baseImage = context.get("baseImage", None)
    if not baseImage:
        raise cc.RTAMError(cc.noBaseImageMsg, cc.noBaseImageCode)

    path = checkWorkingDirectory(context)
    
    # Get the project path and delete it if it exists
    projectPath = path + os.path.sep + projectName
    if existsDirectory(projectPath):
        shutil.rmtree(projectPath)
        
    os.makedirs(projectPath)
    
    return projectPath

# Copy the source directory into the current directory
def copySource(folder, foldersPath, folderName):
    print(60*'!')
    print(os.getcwd())
    # Check that folder object exists
    if not folder:
        raise cc.RTAMError(cc.noFolderMsg, cc.noFolderCode)

    # Check for source info
    source = folder.get("source", None)
    if not source:
        raise cc.RTAMError(cc.noSourceInfoMsg, cc.noSourceInfoCode)

    # Check for valid source type
    sourceType = source.get("sourceType", None)
    if not sourceType or sourceType!='file':
        raise cc.RTAMError(cc.badSourceTypeMsg, cc.badSourceTypeCode)

    # Check for source path
    sourcePath = source.get("sourcePath", None)
    if not sourcePath:
        raise cc.RTAMError(cc.noSourcePathMsg, cc.noSourcePathCode)
    
    copySourceFromPath(sourcePath, foldersPath, folderName)

    return

def copySourceFromPath(sourcePath, foldersPath, folderName):
    
    # Copy the source tree
    try:
        sourcePath = os.path.abspath(sourcePath)
        os.mkdir(foldersPath + os.path.sep + folderName)
        folderPath = getFolderPath(foldersPath, folderName)
        baseName = os.path.basename(sourcePath)
        shutil.copytree(sourcePath, folderPath + os.path.sep + baseName)
    except:
        raise cc.RTAMError(cc.errorCopyingSourceMsg, cc.errorCopyingSourceCode)
    
    return

# Get the port range.
def getPortRange(project):
    
    # Check project.
    if not project or not isinstance(project,dict):
        raise cc.RTAMError(invalidProjectMsg, invalidProjectCode)

    # Get the port range.
    portRange = project.get("portRange", [5000,5500])
    return portRange

# Walks the project tree, numbers the nodes (project, folders, modules)
def walkNumber(project):
    
    # Check if the project exists
    if project is not None:
        nodeNumber = 1
        project['nodeNumber'] = nodeNumber
        nodeNumber += 1
        folders = project.get('folders', {})
        for folder in folders.values():
            folder['nodeNumber'] = nodeNumber
            nodeNumber += 1            
            modules = folder.get('modules', {})
            for module in modules.values():
                module['nodeNumber'] = nodeNumber
                nodeNumber += 1            
            
    return project

# Builds the project
# Arguments:
# * project - The project dictionary
# * basePath - The base directory path to which the source directories are relative
# * context - The context dictionary of the tool
def buildProject(project, basePath, context):
    
    # TODO: CONFIGURE TLS FOR NGINX BASED ON THE serviceTLS PARAMETER
    
    # Initialize the build
    projectPath = initBuild(project, context)
    #servicePath = projectPath + os.path.sep + 'services'
    #os.makedirs(servicePath)
    #foldersPath = servicePath + os.path.sep + 'folders'
    foldersPath = projectPath + os.path.sep + 'folders'
    os.makedirs(foldersPath)
    #webPath = projectPath + os.path.sep + 'web'
    #os.makedirs(webPath)
    logPath = projectPath + os.path.sep + 'logs'
    os.makedirs(logPath)
    os.makedirs(logPath + os.path.sep + 'smp')
    os.makedirs(logPath + os.path.sep + 'smi')
    
    cannrHome = '/usr/local/cannr'
    
    # Dictionary for results
    result = {}
    
    # String for Dockerfile
    dockerText = getDockerfile()
    
    # Main script for static startup
    mainText = buildCodeLine(0, ['# Startup script', '\n'])
    mainText += buildCodeLine(0, ['# Start workers'])
    
    # Create container
    
    # Add FROM to import base runtime image and label with maintainer
    baseImage = project.get("baseImage", 'cannr')
    dockerText = dockerText.replace('<base image>', baseImage)
    #dockerText += "FROM " + baseImage + '\n'

    maintainerEmail = context.get("maintainerEmail", None)
    if maintainerEmail:
        dockerText = dockerText.replace('#<maintainer>', 'LABEL maintainer="' + maintainerEmail + '"')
        #dockerText += 'LABEL maintainer="' + maintainerEmail + '"\n'
    else:
        dockerText = dockerText.replace('#<maintainer>', '# No maintainer information')
    
    #dockerText += '\n'
    
    # R and Python packages to import, respectively.
    rPackageNames = []
    pPackageNames = []

    # Get the port range and first port.
    portRange = getPortRange(project)
    port = portRange[0]
    
    # Create the event calendar for the SMP and add events to start the SMI and NGINX.
    smiPath = project.get('smiPath', '/web/smi.py')
    nginxPath = project.get('nginxPath', '/etc/nginx')
    smiPort = project.get("smiPort", 8080)
    nginxPort = project.get("nginxPort", 80)
    #eventCalendar = EventCalendar()
    #eventCalendar.addEntry(None, "startSMI", {"path": smiPath, "port": smiPort}, 3)
    #eventCalendar.addEntry(None, "startNGINX", {"path": nginxPath, "port": nginxPort}, 1)
    
    # NGINX config.
    ngnixHttpBlock = 'http {\n'
    
    # NGINX servers
    nginxServerBlock =  '\t' + 'server {\n'
    
    # Loop through folders in the project, add to project.  Main loop!
    folderNames = cc.getFolderNames(project)
    for folderName in folderNames:
        
        # Get the folder and copy the source files to the new folder
        folder = cc.getFolder(folderName, project)

        # Check for source info
        source = folder.get("source", None)
        if not source:
            raise cc.RTAMError(cc.noSourceInfoMsg, cc.noSourceInfoCode)
    
        # Check for valid source type
        sourceType = source.get("sourceType", None)
        if not sourceType or sourceType!='file':
            raise cc.RTAMError(cc.badSourceTypeMsg, cc.badSourceTypeCode)
    
        # Check for source path
        sourcePath = source.get("sourcePath", None)
        if not sourcePath:
            raise cc.RTAMError(cc.noSourcePathMsg, cc.noSourcePathCode)

        # Adjust if not absolute path
        sp = Path(sourcePath)
        if not sp.is_absolute():
            str(Path(basePath).resolve())
            sp = Path(str(Path(basePath).resolve()) + os.path.sep + sourcePath)
            sourcePath = str(sp.resolve())
        
        # copySource(folder, foldersPath, folderName)
        copySourceFromPath(sourcePath, foldersPath, folderName)
        timeout = folder.get('timeout', 5)
        queueSize = folder.get('queueSize', 10)
        ##source = folder.get('source', None)
        ##sourcePath = source.get("sourcePath", None)
        folderLogPath = logPath + os.path.sep + 'workers' + os.path.sep + folderName
                
        # If Python
        if folder.get("language", "Python")=="R":
            
            # Loop through modules in the folder
            moduleNames = cc.getModuleNames(folder)
            for moduleName in moduleNames:
                module = cc.getModule(moduleName, folder)

                # Generate runtime file for the module and copy to service home
                sourceFileName = module.get("sourceFile", None)
                if not sourceFileName:
                    raise cc.RTAMError(missingSourceFileNameMsg, missingSourceFileNameCode)
                
                # TODO: PREFIX THIS WITH THE FOLLOWING
                # 'setwd("' + cc.getHome(folderName, folder) + ")'
                sourceText = '# Change to the source directory\n'
                sourceText += buildCodeLine(0, ['setwd("', cc.getHome(folderName, folder), '")\n'])
                
                with open(sourcePath + os.path.sep + sourceFileName, "r") as sourceFile:
                    sourceText += sourceFile.read()

                moduleText = sourceText + 2*'\n' + buildRModuleEpilogue(folderName, moduleName, project)
                folderPath = getFolderPath(foldersPath, folderName)
                modulePath = folderPath + os.path.sep + moduleName + ".R"
                
                with open(modulePath, "w") as moduleFile:
                    moduleFile.write(moduleText)
                
                # Add to NGINX config file and startup event calendar of SMP
                upstreamName = folderName + '_' + moduleName
                ngnixHttpBlock += '\t' + 'upstream ' + upstreamName + ' {\n'
                
                # Add workers
                workers = module.get('workers', 1)
                workerID = 1
                path = '/folders/' + folderName + '/' + moduleName + '.R'
                for worker in range(workers):
                    ngnixHttpBlock += 2*'\t' + 'server localhost:' + str(port) + ' max_conns=1;\n'
                    #eventCalendar.addEntry(None, "startPlumber", {"folder": folderName, "module": moduleName, "path": modulePath, "port": port}, 1)
                    # TODO: THROW EXCEPTION IF PORT OUT OF RANGE
                    #mainText += buildCodeLine(0, ['Rscript', ' --vanilla ', cannrHome + '/runApp.R', ' ', path, ' ', cc.getHome(folderName, folder), ' ', str(port), ' ', str(workerID), ' &'])
                    mainText += buildCodeLine(0, ['Rscript', ' --vanilla ', cannrHome + '/runApp.R', ' ', path, ' ', str(port), ' ', str(workerID), ' &'])
                    port += 1
                    workerID += 1
    
                # FEATURE ONLY AVAILABLE IN NGINX PLUS!
                # ngnixHttpBlock += 2*'\t' + 'queue ' + str(queueSize) + ' timeout=' + str(timeout) + ';\n'
                ngnixHttpBlock += '\t' + '}\n'
                
                # Add location to NGINX server block.
                nginxServerBlock += 2*'\t' + 'location /services/' + folderName + '/' + moduleName + ' {\n'
                nginxServerBlock += 3*'\t' + 'proxy_pass http://' + upstreamName + ';\n'
                nginxServerBlock += 2*'\t' + '}\n'
           
                # Add packages to list of Python packages
                packages = module.get("packages", None)
                if packages:
                    rPackageNames.extend(packages)

                os.makedirs(folderLogPath + os.path.sep + moduleName)

                # TODO:      
                # Add help for module
            
        else:
        
            # Generate runtime file for the folder and copy to service home
            moduleText = buildPyFolder(folderName, project)
            folderPath = getFolderPath(foldersPath, folderName)
            modulePath = folderPath + os.path.sep + folderName + ".py"
            
            with open(modulePath, "w") as moduleFile:
                moduleFile.write(moduleText)
                
            # Add to NGINX config file and startup event calendar of SMP
            ngnixHttpBlock += '\t' + 'upstream ' + folderName + ' {\n'
            
            # Add workers
            workers = folder.get('workers', 1)
            #workerNum = 0
            path = '/folders/' + folderName + '/' + folderName + '.py'
            for worker in range(workers):
                # TODO: REMOVE max_conns=1.  NOT NEEDED!
                ngnixHttpBlock += 2*'\t' + 'server localhost:' + str(port) + ' max_conns=1;\n'
                #eventCalendar.addEntry(None, "startFlask", {"folder": folderName, "path": modulePath, "port": port}, 1)
                # TODO: THROW EXCEPTION IF PORT OUT OF RANGE
                #mainText += buildCodeLine(0, ['python ', path, ' ', str(port), ' ', str(workerNum), ' &'])
                mainText += buildCodeLine(0, ['python ', path, ' ', str(port), ' &'])
                port += 1
                #workerNum += 1

            # FEATURE ONLY AVAILABLE IN NGINX PLUS!
            # ngnixHttpBlock += 2*'\t' + 'queue ' + str(queueSize) + ' timeout=' + str(timeout) + ';\n'
            ngnixHttpBlock += '\t' + '}\n'
            
            # Add location to NGINX server block.
            nginxServerBlock += 2*'\t' + 'location /services/' + folderName + ' {\n'
            nginxServerBlock += 3*'\t' + 'proxy_pass http://' + folderName + ';\n'
            nginxServerBlock += 2*'\t' + '}\n'
           
            # Loop through modules in the folder
            moduleNames = cc.getModuleNames(folder)
            for moduleName in moduleNames:
                module = cc.getModule(moduleName, folder)

                # Add packages to list of Python packages
                packages = module.get("packages", None)
                if packages:
                    pPackageNames.extend(packages)
               
            os.makedirs(folderLogPath)

                # TODO:      
                # Add help for module

    # Close NGINX http server block and add it to the http block.                
    nginxServerBlock += '\t' + '}\n'
    ngnixHttpBlock += nginxServerBlock
    ngnixHttpBlock += '}'
    
    # Save NGINX http block to conf.d/http
    nginxConfPath = nginxPath + os.path.sep + 'conf.d'
    nginxProjectConfPath = projectPath + os.path.sep + 'conf.d'
    try:
        os.makedirs(nginxProjectConfPath)
    except:
        pass
    nginxProjectHttpPath = nginxProjectConfPath + os.path.sep + 'http'
    
    with open(nginxProjectHttpPath, "w") as nginxFile:
        nginxFile.write(ngnixHttpBlock)

    #dockerText += "COPY " + './conf.d/http' + ' ' + nginxConfPath + '\n'
    #dockerText += '\n'
    # TODO: IN DOCKER API, COPY NGINX HTTP CONFIG FILE
    
    # Add imports of R packages to container and Dockerfile
    installText = ''
    rPackageSet = set(rPackageNames)
    if len(rPackageSet):
        for pkg in rPackageSet:
            #dockerText += 'RUN R -e "install.packages(\'' + pkg + '\')"\n'
            #dockerText += 'RUN install2.r ' + pkg + '\n'
            if not cc.isRInstPkg(pkg):
                installText += 'RUN install2.r ' + pkg + '\n'
            # TODO: ADD PACKAGE INSTALL USING API
        #dockerText += '\n'
        dockerText = dockerText.replace('#<R Packages>', installText)
    else:
        dockerText = dockerText.replace('# No packages to install', installText)
    
    # Add imports of Python packages to container and Dockerfile
    installText = ''
    pPackageSet = set(pPackageNames)
    if len(rPackageSet):
        for pkg in pPackageSet:
            #dockerText += 'RUN pip install ' + pkg + '\n'
            if not cc.isStdPkg(pkg) and not cc.isInstPkg(pkg):
                installText += 'RUN pip3 install ' + pkg + '\n'
            # TODO: ADD PACKAGE INSTALL USING API
        #dockerText += '\n'
        dockerText = dockerText.replace('#<P Packages>', installText)
    else:
        dockerText = dockerText.replace('# No packages to install', installText)
    
    # Number the nodes in the project
    project = walkNumber(project)        

    # Copy project file to project directory
    with open(projectPath + os.path.sep + 'project.json', "w") as projectFile:
        projectFile.write(json.dumps(project))    

    # Add command to start NGINX
    mainText += buildCodeLine(0, [])
    mainText += buildCodeLine(0, ['# Start NGINX'])
    mainText += buildCodeLine(0, ["nginx -g 'daemon off;'"])
    # nginx -g 'daemon off;'
    
    # Copy startup script to project directory
    with open(projectPath + os.path.sep + 'main.sh', "w") as mainFile:
        mainFile.write(mainText)
    
    # Write initial event calendar to file.
    #os.chdir(projectPath)
    #os.mkdir('eventCalendar')
    #eventCalendar.write(projectPath + os.path.sep + 'eventCalendar')

    # Copy project directory to container
    # Don't need to do this.
    #dockerText += 'COPY ' + projectPath + '/ /projectHome/\n'
    # TODO: COPY PROJECT DIRECTORY TO THE CONTAINER
    
    # TODO: ADD CMD/ENTRYPOINT TO DOCKERFILE
    
    # Write out Dockerfile to the project directory
    with open(projectPath + os.path.sep + 'Dockerfile', "w") as dockerFile:
        dockerFile.write(dockerText)
        
    return

# Builds the project from a project file.
# 
def buildFromFile(path, context):
    
    # projectFilePath = os.path.abspath('../examples/project1/project.json')
    project = cc.readJSONFile(path)
    basePath = os.path.dirname(path)
    
    buildProject(project, basePath, context)

    return