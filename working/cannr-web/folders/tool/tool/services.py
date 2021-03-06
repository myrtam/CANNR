
'''
Services to support the CANNR TM Web build tool.
These services take an unconverted input and possibly a dictionary containing
query parameters and return a dictionary.
'''

import cannrcore as cc
import cannrio as ci
import cannrbuild as cb
import os
import json
import sys
import traceback
import re
import shutil
import docker
from flask import request
from werkzeug.utils import secure_filename
#from werkzeug.datastructures import ImmutableMultiDict


# Try to read the context
context = None
projectsPath = None
if os.path.exists('context.json'):
    context = cc.readJSONFile('context.json')
if os.path.exists('/config/context.json'):
    context = cc.readJSONFile('/config/context.json')
elif os.path.exists('/external/config/context.json'):
    context = cc.readJSONFile('/external/config/context.json')

# Try to define the projects folder
if context:
    projectsPath = context.get('projectsPath', None)
    workingDirectory = context.get('workingDirectory', None)
    
# Define the projects and working folders
projectsPath = projectsPath if projectsPath else ('/external/projects' if os.path.exists('/external/projects') else None)
workingDirectory = workingDirectory if workingDirectory else ('/external/working' if os.path.exists('/external/working') else None)

      
# Set the context for testing purposes
def setContext(newContext):
    context = newContext
    global projectsPath
    projectsPath = context.get('projectsPath', None)
    

# Returns the projects path
def getProjectsPath():
    return projectsPath


# Parses the source file and returns a list of functions in the file.
def parseSource(source, language):

    # Get the matches
    if (language=='R'):
        return re.findall('[ \t]*([\w]*)[ \t]*<-[ \t]*function[ \t]*\([^\(\)\{\}]*\)[ \t]*{', source, re.M)
    else:
        return re.findall('^[ \t]*def[ \t]*([\w]*).*$', source, re.M)
        

# Creates a new project folder in the container's work area.
def createProject_(input):
    
    try:
    
        # Get the project from the input, return error if no project
        project = input.get('project', None)
        if not project:
            return {'succeeded': False, 'error': 'noProjectInfo', 'errorMsg': 'No project information specified'}
        
        # Get the overwrite flag and project name, check project name
        overwrite = input.get('overwrite', False)
        projectName = project.get('projectName', None)
        if not projectName:
            return {'succeeded': False, 'error': 'noProjectName', 'errorMsg': 'No project name'}
        
        # Check for legal project name
        if not cc.legalName(projectName):
            return {'succeeded': False, 'error': 'badProjectName', 'errorMsg': 'Bad project name'}
        
        # Check to make sure /projects exists
        if not projectsPath:
            return {'succeeded': False, 'error': 'noProjectsDir', 'errorMsg': 'No projects directory'}
        
        # Check to see if the project exists already
        projectPath = projectsPath + '/' + projectName
        projectPath = os.path.abspath(projectPath)
        if os.path.isdir(projectPath):
            if overwrite:
                # Remove the project and its subfolders
                shutil.rmtree(projectPath)
            else:
                return {'succeeded': False, 'error': 'projectExists', 'errorMsg': 'Project exists'}
        
        # Create the project directory
        os.mkdir(projectPath)
       
        # Write the project file to the project directory
        with open(projectPath + '/project.json', 'w') as projectFile:
            projectFile.write(json.dumps(project, indent=2))    
        
        # Return the 
        return {'succeeded': True, 'project': project}

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorCreatingProject',
            'errorMsg': 'Error creating project',
            'detail': str(err)
            }


# Version of createProject_ that takes the project name as a resource.
def createProject(resourceNames, input):
    
    try:
    
        # Get the project from the input, return error if no project
        project = input.get('project', None)
        if not project:
            return {'succeeded': False, 'error': 'noProjectInfo', 'errorMsg': 'No project information specified'}
        
        projectName = resourceNames.get('projectname', None)
        project['projectName'] = projectName
        
        return createProject_(input)


    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorCreatingProject',
            'errorMsg': 'Error creating project',
            'detail': str(err)
            }


# Deletes the project from the container's work area.
def deleteProject_(input):

    try:
    
        # Get the project from the input, return error if no project
        projectName = input.get('projectName', None)
        if not projectName:
            return {'succeeded': False, 'error': 'noProjectName', 'errorMsg': 'No project specified'}
        
        # Check to make sure /projects exists
        if not projectsPath:
            return {'succeeded': False, 'error': 'noProjectsDir', 'errorMsg': 'No projects directory'}
        
        # Check to see if the project exists already
        projectPath = projectsPath + '/' + projectName
        if not os.path.isdir(projectPath):
            return {'succeeded': False, 'error': 'projectNotExist', 'errorMsg': 'Project does not exist'}

        # Remove the project and its subfolders
        shutil.rmtree(projectPath)
            
        # Return the 
        return {'succeeded': True}

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorDeletingProject',
            'errorMsg': 'Error deleting project',
            'detail': str(err)
            }


# Deletes the project from the container's work area.
def deleteProject(resourceNames):

    try:
    
        # Get the project from the input, return error if no project
        projectName = resourceNames.get('projectname', None)
        
        return deleteProject_({'projectName': projectName})

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorDeletingProject',
            'errorMsg': 'Error deleting project',
            'detail': str(err)
            }


# Returns a dictionary of all projects.
def getProjectsDict():

        # Get the collection of projects
        projects = {}

        # List the contents of the projects directory
        for projectName in os.listdir(projectsPath):
            # Check that the item is a directory
            projectDir = os.path.join(projectsPath, projectName)
            if os.path.isdir(projectDir):
                # Get the project file path and check that the file exists
                filePath = os.path.join(projectDir, 'project.json')
                if os.path.isfile(filePath):
                    # Read the file and add it to the collection
                    project = cc.readJSONFile(filePath)
                    projects[projectName] = project

        return projects


# Returns the project document for a project given the project name or timestamp.
def getProject(resourceNames):

    try:
    
        # Check to make sure /projects exists
        if not projectsPath:
            return {'succeeded': False, 'error': 'noProjectsDir', 'errorMsg': 'No projects directory'}

        # Get all of the projects
        projects = getProjectsDict()

        # Retrieve the project name and timestamp
        projectName = resourceNames.get('projectname', None)
        timestamp = resourceNames.get('timestamp', None)

        # Try retrieving by project name
        if projectName and projectName != '~':
            project = projects[projectName]
            if project:
                return {'succeeded': True, 'project': project}
            else:
                return {'succeeded': False, 'error': 'projectNotExist', 'errorMsg': 'Project does not exist'}

        # Try retrieving by timestamp
        elif timestamp:
            # Go through the projects
            for projectName in projects:
                project = projects[projectName]
                # If timestamp matches, we're done
                if project.get('timestamp', '0')==timestamp:
                    return {'succeeded': True, 'project': project}

            # No project found
            return {'succeeded': True, 'project': None}

        # Error if no project name or timestamp specified
        else:
            return {'succeeded': False, 'error': 'noProjectName', 'errorMsg': 'No project name or timestamp specified'}

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorRetrievingProject',
            'errorMsg': 'Error retrieving project',
            'detail': str(err)
            }


# Returns a collection of all project documents.
def getProjects():

    try:            
        # Return the result
        return {
            'succeeded': True,
            'projects': getProjectsDict()}

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorRetrievingProjects',
            'errorMsg': 'Error retrieving projects',
            'detail': str(err)
            }


# Handles upload of folder contents.
# * resourceNames - Dictionary containing project and folder names
# * request - Flask request for the upload
# * webUpload - If True, then uploaded data is assumed to be a Web multipart form data directory upload,
#   otherwise it is assumed to be a zip file.
def upload(resourceNames, data, uploadType = 'folder'):
    
    # Get project name and folder name from resourceNames
    projectName = resourceNames.get('projectname', None)
    folderName = resourceNames.get('foldername', None)
    fileName = resourceNames.get('filename', None)

    # Check that project name and folder name are OK
    if not (projectName and cc.legalName(projectName) and folderName and cc.legalName(folderName)):
        return {
            'succeeded': False, 
            'error': 'badProjectFolderName',
            'errorMsg': 'Missing or invalid project or folder name',
            'detail': 'Project name: ' + (projectName if projectName else '') + '\n'
                + 'Folder name: ' + (folderName if folderName else '')
            }

    # Check that project directory and project exist
    projectPath = projectsPath + '/' + projectName
    filePath = projectPath + '/project.json'
    if not (os.path.isdir(projectPath) and os.path.isfile(filePath)):
        return {'succeeded': False, 'error': 'projectNotExist', 'errorMsg': 'Project does not exist'}

    # Get the project object from the project directory
    project = cc.readJSONFile(filePath)
    if not project:
        return {'succeeded': False, 'error': 'projectNotExist', 'errorMsg': 'Project does not exist'}

    # Get the data from the request
    #data = request.get_data()

    # Write out the files
    newFileNames = []
    fullFolderName = projectPath + '/' + folderName + '/'
    uploadType = uploadType.lower()
    try:
        if uploadType == 'file':
            newFileName = ci.writeFile(data, fullFolderName, fileName)
            if newFileName:
                newFileNames.append(newFileName)
        elif uploadType == 'zipfile':
            newFileNames = ci.writeZipFiles(data, fullFolderName)
        else:           
            newFileNames = ci.writeFiles(data, fullFolderName)

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorWritingFiles',
            'errorMsg': 'Error writing files',
            'detail': str(err)
            }

    # Get existing folder, if any, add if none
    folders = project.get('folders', None)
    if not folders:
        folders = {}
        project['folders'] = folders
        
    folder = folders.get(folderName, None)
    if not folder:
        folder = {}
        folders[folderName] = folder

    # Get the list of new file names in the top level directory of the folder
    newFileNames = ci.regexFilter([s[len(fullFolderName):] for s in newFileNames], '^[^/]*$')
    
    # Add to the existing list if appropriate
    fileNames = folder.get('fileNames', [])
    if uploadType == 'file':
        fileNames = fileNames.extend(newFileNames)
    else:
        fileNames = newFileNames
    
    # Remove duplicates and update in the project
    fileNames = list(set(fileNames))
    folder['fileNames'] = fileNames
    
    # Write the updated project to the project folder and return the project.
    return {
        'succeeded': True,
        'project': project
        }    


# Uploads a folder to a project.
def uploadFolder(resourceNames, request):
    
    # Get the data from the request
    data = request.get_data()

    return upload(resourceNames, data)


# Deletes a folder from a project.
def deleteFolder_(input):

    try:
    
        # Get the project from the input, return error if no project
        projectName = input.get('projectName', None)
        folderName = input.get('folderName', None)
        if not projectName or not folderName:
            return {'succeeded': False, 'error': 'noProjectName', 'errorMsg': 'Project or folder not specified'}
        
        # Check to make sure /projects exists
        if not projectsPath:
            return {'succeeded': False, 'error': 'noProjectsDir', 'errorMsg': 'No projects directory'}
        
        # Project directory and project file path
        projectPath = projectsPath + '/' + projectName
        filePath = projectPath + '/project.json'
        
        # Retrieve the project
        project = cc.readJSONFile(filePath)
        
        # Check to see if the folder exists
        folderPath = projectPath + '/' + folderName
        if os.path.isdir(folderPath):
            # Remove the folder and its subfolders from the file system
            shutil.rmtree(folderPath)
        
        # Remove the folder from the project
        folders = project.get('folders', None)
        if not folders:
            project.put('folders', {})
        else:
            folders.pop(folderName, None)

        # Write out project file
        with open(filePath, 'w') as projectFile:
            projectFile.write(json.dumps(project, indent=2))

        # Return the updated project
        return {'succeeded': True, 'project': project}

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorDeletingFolder',
            'errorMsg': 'Error deleting folder',
            'detail': str(err)
            }


# Deletes a folder from a project.
def deleteFolder(resourceNames):

    try:
    
        # Get the project from the input
        projectName = resourceNames.get('projectname', None)
        folderName = resourceNames.get('foldername', None)
        
        return deleteFolder_({'projectName': projectName, 'folderName': folderName})
        
    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorDeletingFolder',
            'errorMsg': 'Error deleting folder',
            'detail': str(err)
            }


# Updates project data, excluding folders
def updateProject_(input):
    
    try:
    
        # Get the project from the input, return error if no project
        project = input.get('project', None)
        if not project:
            return {'succeeded': False, 'error': 'noProjectInfo', 'errorMsg': 'No project information specified'}
        
        # Get the project name, check project name
        projectName = project.get('projectName', None)
        if not projectName:
            return {'succeeded': False, 'error': 'noProjectName', 'errorMsg': 'No project name'}
        
        # Check to make sure /projects exists
        if not projectsPath:
            return {'succeeded': False, 'error': 'noProjectsDir', 'errorMsg': 'No projects directory'}
        
        # Check to see if the project exists already
        projectPath = projectsPath + '/' + projectName
        if not os.path.isdir(projectPath):
            # If not, create it
            return {'succeeded': False, 'error': 'noProject', 'errorMsg': 'Project does not exist'}
            
        # Write the project file to the project directory
        with open(projectPath + '/project.json', 'w') as projectFile:
            projectFile.write(json.dumps(project, indent=2))    
        
        # Return the 
        return {'succeeded': True, 'project': project}

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorUpdatingProject',
            'errorMsg': 'Error updating project',
            'detail': str(err)
            }


# Updates project data, excluding folders
def updateProject(resourceNames, input):
    
    try:
    
        # Get the project from the input, return error if no project
        project = input.get('project', None)
        if not project:
            return {'succeeded': False, 'error': 'noProjectInfo', 'errorMsg': 'No project information specified'}
        
        # Get the project name, add to the project
        projectName = resourceNames.get('projectname', None)
        project['projectName'] = projectName
        
        # Update the project
        return updateProject_(input)
        
    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorUpdatingProject',
            'errorMsg': 'Error updating project',
            'detail': str(err)
            }


# Updates a project and returns the updated project with function names
# populated for a module.
def updateModule(resourceNames, input):
    
    try:

        # Update the project to check for errors
        update = updateProject_(input)
        project = update.get('project', None)
        if not update.get('succeeded', None) or not project:
            return update

        # Get folder name and module name from resourceNames
        folderName = resourceNames.get('foldername', None)
        moduleName = resourceNames.get('modulename', None)
        folders = project.get('folders', {})
        if not (folderName and moduleName and folders):
            return {'succeeded': False, 'error': 'noModule', 'errorMsg': 'Module does not exist'}

        # Get the language and module
        folder = folders.get(folderName, {})
        language = folder.get('language', '')
        modules = folder.get('modules', {})
        module = modules.get(moduleName, {})
        if not (module and (language in ['R', 'Python'])):
            return {'succeeded': False, 'error': 'noModule',
                'errorMsg': 'Module does not exist or language not specified'}
        
        # Get the source file name
        sourceFile = module.get('sourceFile', None)
        if not sourceFile:
            return {'succeeded': False, 'error': 'noSourceFile', 
                'errorMsg': 'No source file specified for module'}
        
        # Get the source path
        projectName = project.get('projectName', None)
        sourcePath = projectsPath + '/' + projectName + '/' + folderName + '/' + sourceFile
        if not os.path.isfile(sourcePath):
            # If not, create it
            return {'succeeded': False, 'error': 'sourceNotFound',
                'errorMsg': 'Source file not found'}
        
        # Read the source file
        with open(sourcePath, "r") as sourceFile:
            source = sourceFile.read()
        
        # Parse the source to get the function names and add them to the module.
        module['functionNames'] = parseSource(source, language)
        
        # Update the project again and return the result
        return updateProject_({'project': project})
    
    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorUpdatingProject',
            'errorMsg': 'Error updating project',
            'detail': str(err)
            }


# Renames the project, both in the project file and the project folder name.
def renameProject(input):
    
    try:
    
        # Convert input to dictionary
        #inputObject = json.loads(input)
        
        # Get the project from the input, return error if no project
        oldProjectName = input.get('oldProjectName', None)
        newProjectName = input.get('newProjectName', None)
        if not oldProjectName or not newProjectName:
            return {'succeeded': False, 'error': 'noProjectName', 'errorMsg': 'No project names given'}
        
        # TODO: CHECK THAT newProjectName IS LEGAL
        
        # Check to make sure /projects exists
        if not projectsPath:
            return {'succeeded': False, 'error': 'noProjectsDir', 'errorMsg': 'No projects directory'}
        
        # Check to see if the project exists already
        oldProjectPath = projectsPath + '/' + oldProjectName
        if not os.path.isdir(oldProjectPath):
            # If not, create it
            return {'succeeded': False, 'error': 'noProject', 'errorMsg': 'Project does not exist'}
            
        # Check to make sure a project with the new name doesn't exist
        newProjectPath = projectsPath + '/' + newProjectName
        if os.path.isdir(newProjectPath):
            # If not, create it
            return {'succeeded': False, 'error': 'projectExists', 'errorMsg': 'A project with the new name exists'}

        # Retrieve the project document
        filePath = oldProjectPath + '/project.json'
        project = cc.readJSONFile(filePath)
        project['projectName'] = newProjectName
        
        # Rename the project folder
        os.rename(oldProjectPath, newProjectPath)
        
        # Write the project file to the project directory
        with open(newProjectPath + '/project.json', 'w') as projectFile:
            projectFile.write(json.dumps(project, indent=2))    
        
        # Return the 
        return {'succeeded': True, 'project': project}

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorUpdatingProject',
            'errorMsg': 'Error updating project',
            'detail': str(err)
            }


# Renames a folder.
def renameFolder(input):
    return {}


# Builds the project.
def buildProject_(input):

    try:

        # Update the project, return status if not successful
        status = updateProject_(input);
        if not status.get('succeeded', False):
            return status

        # Get the project
        project = status.get('project', None)
        
        # Build the project
        cb.buildProject(project, '', context)

        return {
            'succeeded': True,
            'project': project
            }

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorBuildingProject',
            'errorMsg': 'Error building project',
            'detail': str(err)
            }


# Builds the project.
def buildProject(resourceNames, input):

    try:
    
        # Update the project, return status if not successful
        status = updateProject(resourceNames, input);
        if not status.get('succeeded', False):
            return status

        # Get the project
        project = status.get('project', None)
        
        # Build the project
        cb.buildProject(project, '', context)

        return {
            'succeeded': True,
            'project': project
            }

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorBuildingProject',
            'errorMsg': 'Error building project',
            'detail': str(err)
            }



# Builds the image for the project.
def buildImage(resourceNames):

    try:

        # Get the project from the resourceNames, return error if no project
        projectName = resourceNames.get('projectName', None)
        tag = resourceNames.get('tag', None)
        # TODO:  CHECK FOR VALID TAG
        if not projectName:
            return {'succeeded': False, 'error': 'noProjectInfo', 'errorMsg': 'No project information specified'}

        # Create the docker client
        client = docker.from_env()

        # Get the built project path and check that it exists
        builtProjectPath = os.path.join(workingDirectory, projectName)
        builtDockerPath = os.path.join(builtProjectPath, 'Dockerfile')
        if not os.path.isfile(builtDockerPath):
            return {
                'succeeded': False, 
                'error': 'errorBuildingImage',
                'errorMsg': 'Error building image',
                'detail': 'No built project exists'
                }

        # Build the project and get the result.
        result = client.images.build(path = builtProjectPath, tag = (tag if tag else projectName))

        # Return the result
        if len(result) > 0:
            return {
                'succeeded': True, 
                'id': result[0].id,
                'tags': result[0].tags
                }
        else:
            return {
                'succeeded': False, 
                'error': 'errorBuildingImage',
                'errorMsg': 'Error building image',
                'detail': 'Image build returned no result'
                }

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorBuildingImage',
            'errorMsg': 'Error building image',
            'detail': str(err)
            }


# Exports the project.  This is the project as specified by the user, not the built project, which can be used to build the image.
def exportProject(input):
    return {}


# Imports a previously exported project.  This is the project as specified by the user, not the built project, which can be used to build the image.
def importProject(resourceNames, input):
    return {}


# Exports the built project.  This can then be used to build an image in another environment.
def exportBuild(input):
    return {}


# Runs a project image in a container.
def runContainer(input):

    try:

        # Get the image from the input, return error if no image
        image = input.get('image', None)
        name = input.get('name', None)
        if not image:
            return {'succeeded': False, 'error': 'noImage', 'errorMsg': 'No image specified'}

        # Create the docker client
        client = docker.from_env()

        # Run the container and get the result.
        container = client.containers.run(image, name = (name if name else None), detach=True)
        return {
            'succeeded': True, 
            'id': container.id,
            'short_id': container.short_id,
            'image': container.image,
            'labels': container.labels,
            'name': container.name,
            'status': container.status
            }

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorRunningContainer',
            'errorMsg': 'Error running container',
            'detail': str(err)
            }


# Stops the container running a project image.
def stopContainer(input):

    try:

        # Get the container id from the input, return error if no id.
        id = input.get('id', None)
        if not id:
            return {'succeeded': False, 'error': 'noContainerID', 'errorMsg': 'No container id specified'}

        # Create the docker client
        client = docker.from_env()

        # Get the container and check its status.
        container = client.containers.get(id)
        if container.status == 'running':
            container.stop();

        # Return the container status.
        return {
            'succeeded': True, 
            'status': container.status
            }

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorStoppingContainer',
            'errorMsg': 'Error stopping container',
            'detail': str(err)
            }


# Stops the container running a project image.
def getStatus(input):

    try:

        # Get the container id from the input, return error if no id.
        id = input.get('id', None)
        if not id:
            return {'succeeded': False, 'error': 'noContainerID', 'errorMsg': 'No container id specified'}

        # Create the docker client
        client = docker.from_env()

        # Get the container.
        container = client.containers.get(id)

        # Return the container status.
        return {
            'succeeded': True, 
            'status': container.status
            }

    except Exception as err:
        return {
            'succeeded': False, 
            'error': 'errorGettingContainerStatus',
            'errorMsg': 'Error getting container status',
            'detail': str(err)
            }


# Sends the contents of a zipped folder on the files system to the server.
# For use in REST API, R & Python packages.
def sendFolder(resourceNames, data):

    # Get the data from the request
    data = request.get_data()

    return upload(resourceNames, data, uploadType = 'zipfile')


# Sends a file to the server using the specified project, folder, and file name.
# For use in R & Python packages.
def sendFile(resourceNames, data):

    # Get the data from the request
    data = request.get_data()

    return upload(resourceNames, data, uploadType = 'file')


