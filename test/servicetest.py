'''
Test harness for services.py
'''

import sys
import os
import json
import platform
import shutil
import unittest

sys.path.append('../source/base_image/cannr/lib')
sys.path.append('../source/runtime')
sys.path.append('../source/webtool/server')

import cannrcore as cnc
import cannrbuild as cnb
import services as svs

class TestServices(unittest.TestCase):
    
    def setUp(self):

        shutil.rmtree('../projects')
        os.mkdir('../projects')

        self.context = cnc.readJSONFile('context.json')
        svs.setContext(self.context)

        self.project1 = {
            'projectTitle': 'Basic test project',
            'projectName': 'project1',
            'projectDescription': 'project1 description',
            'baseImage': 'cannr-base',
            'maintainerName': 'Pat Tendick',
            'maintainerEmail': 'ptendick@gmail.com',
            'dependencyNotice': 'Copyright/license notice for dependencies',
            'portRange': [5001,5500],
            'nginxPort': 80,
            'smiPort': 8080,
            'initRequired': True,
            'local': True
        }
            
        self.project2 = {
            'projectTitle': 'Basic test project',
            'projectName': 'project2',
            'projectDescription': 'project2 description',
            'baseImage': 'cannr-base',
            'maintainerName': 'Pat Tendick',
            'maintainerEmail': 'ptendick@gmail.com',
            'dependencyNotice': 'Copyright/license notice for dependencies',
            'portRange': [5001,5500],
            'nginxPort': 80,
            'smiPort': 8080,
            'initRequired': True,
            'local': True,
            'folders': {
                'folder1': {'folderTitle': 'folder1'},
                'folder2': {'folderTitle': 'folder2'}
            }
        }
            
        self.project3 = {
            'projectTitle': 'Modified test project',
            'projectName': 'project1',
            'projectDescription': 'project1 description',
            'baseImage': 'cannr-base',
            'maintainerName': 'Pat Tendick',
            'maintainerEmail': 'ptendick@gmail.com',
            'dependencyNotice': 'Copyright/license notice for dependencies',
            'portRange': [5001,5500],
            'nginxPort': 80,
            'smiPort': 8080,
            'initRequired': True,
            'local': True
        }

        # Read a Python source file
        with open('../source/base_image/cannr/lib/cannrcore.py', "r") as sourceFile:
            self.pSource = sourceFile.read()

        # Read an R source file
        with open('../examples/project1/folder2/iris.R', "r") as sourceFile:
            self.rSource = sourceFile.read()

        # Read the source file
        with open('testfiles/upload.dat', "rb") as sourceFile:
            self.uploadData = sourceFile.read()

        # Read the source file
        with open('testfiles/folder123.zip', "rb") as sourceFile:
            self.uploadZip = sourceFile.read()

        
    # Completed
    def test_createProject(self):

        resourceNames = {'projectname': 'project1'}
        svs.deleteProject(resourceNames)
                
        # Try to create a project
        input = {'project': self.project1, 'overwrite': False}
        response = svs.createProject(resourceNames, input)
        self.assertTrue(response.get('succeeded', False))

        # Check that overwrite flag works when set to false
        input = {'project': self.project1, 'overwrite': False}
        response = svs.createProject(resourceNames, input)
        self.assertFalse(response.get('succeeded', False))

        # Check that overwrite flag works when set to true
        input = {'project': self.project1, 'overwrite': True}
        response = svs.createProject(resourceNames, input)
        self.assertTrue(response.get('succeeded', False))

    
    # Completed
    def test_deleteProject(self):

        resourceNames = {'projectname': 'project1'}
        input = {'project': self.project1, 'overwrite': True}

        svs.createProject(resourceNames, input)
        projectPath = svs.getProjectsPath() + '/project1'
        self.assertTrue(os.path.isdir(projectPath))
        self.assertTrue(os.path.isfile(projectPath + '/project.json'))

        # Now try to delete it
        svs.deleteProject(resourceNames)
        self.assertFalse(os.path.isdir(projectPath))
        self.assertFalse(os.path.isfile(projectPath + '/project.json'))

    
    # Completed
    def test_getProject(self):

        resourceNames = {'projectname': 'project1'}
        input = {'project': self.project1, 'overwrite': True}
        svs.createProject(resourceNames, input)

        # Get the project document and check the response
        response = svs.getProject(resourceNames)
        self.assertTrue(response.get('succeeded', True))
        project = response.get('project', None)
        self.assertTrue(project)
        self.assertEqual(project.get('projectName', None), 'project1')
    
    
    # Completed
    def test_getProjects(self):
        
        # Create some projects
        resourceNames = {'projectname': 'project1'}
        input = {'project': self.project1, 'overwrite': True}
        svs.createProject(resourceNames, input)
        resourceNames = {'projectname': 'project2'}
        input = {'project': self.project2, 'overwrite': True}
        svs.createProject(resourceNames, input)

        # Get the projects collection and check the response
        response = svs.getProjects()
        self.assertTrue(response.get('succeeded', True))
        projects = response.get('projects', None)
        self.assertTrue(projects)
        project1 = projects.get('project1', None)
        project2 = projects.get('project2', None)
        self.assertTrue(project1)
        self.assertTrue(project2)
    
    
    # Completed
    def test_upload(self):
        
        # Create a project
        resourceNames = {'projectname': 'project1'}
        svs.deleteProject(resourceNames)
        input = {'project': self.project1, 'overwrite': True}
        svs.createProject(resourceNames, input)

        resourceNames = {'projectname': 'project22'}
        svs.deleteProject(resourceNames)
        input = {'project': self.project1, 'overwrite': True}
        svs.createProject(resourceNames, input)

        resourceNames = {'projectname': 'project1', 'foldername': 'folder1'}
        response = svs.upload(resourceNames, self.uploadData)
        
        resourceNames = {'projectname': 'project22', 'foldername': 'folder22'}
        response = svs.upload(resourceNames, self.uploadZip, uploadType = 'zipfile')
        
        resourceNames = {'projectname': 'project1', 'foldername': 'folder1', 'filename': 'iris.R'}
        response = svs.upload(resourceNames, self.rSource, uploadType = 'file')

        self.assertTrue(True)
    
    
    # Completed
    def test_deleteFolder(self):
    
        # Create a project
        resourceNames = {'projectname': 'project2'}
        input = {'project': self.project2, 'overwrite': True}
        svs.createProject(resourceNames, input)
        
        # Create some folders in the project directory
        projectPath = svs.getProjectsPath() + '/project2'
        os.mkdir(projectPath + '/' + 'folder1')
        os.mkdir(projectPath + '/' + 'folder2')
        
        # Try deleting a folder and check the results
        resourceNames = {'projectname': 'project2', 'foldername': 'folder2'}
        response = svs.deleteFolder(resourceNames)
        newproject = response.get('project')
        self.assertTrue(os.path.isdir(projectPath + '/' + 'folder1'))
        self.assertFalse(os.path.isdir(projectPath + '/' + 'folder2'))
        folders = newproject.get('folders', None)
        self.assertTrue(folders.get('folder1', None))
        self.assertFalse(folders.get('folder2', None))


    # Completed
    def test_updateProject(self):
        
        # Create a project
        resourceNames = {'projectname': 'project1'}
        input = {'project': self.project1, 'overwrite': True}
        response = svs.createProject(resourceNames, input)

        # Try updating the project.json file
        input = {'project': self.project3}
        response = svs.updateProject(resourceNames, input)
        newProject = response.get('project')
        self.assertTrue('Modified' in newProject.get('projectTitle'))
    
    
    # Completed
    def test_renameProject(self):

        resourceNames = {'projectname': 'project11'}
        svs.deleteProject(resourceNames)
                
        # Create a project
        resourceNames = {'projectname': 'project1'}
        input = {'project': self.project1, 'overwrite': True}
        response = svs.createProject(resourceNames, input)

        # Try to rename the project and check the results
        input = {"oldProjectName": 'project1', "newProjectName": 'project11'}
        response = svs.renameProject(input)
        newProject = response.get('project')
        self.assertTrue(newProject.get('projectName', None)=='project11')
        oldProjectPath = svs.projectsPath + '/' + self.project1.get('projectName', None)
        newProjectPath = svs.projectsPath + '/project11'
        self.assertFalse(os.path.isdir(oldProjectPath))
        self.assertTrue(os.path.isdir(newProjectPath))


    def test_parseSource(self):
        
        pFunctionNames = svs.parseSource(self.pSource, 'Python')
        rFunctionNames = svs.parseSource(self.rSource, 'R')

        self.assertTrue('legalName' in pFunctionNames)
        self.assertTrue('predPLengthSLength' in rFunctionNames)

    
    # Not implemented
    def test_renameFolder(self):

        self.assertTrue(True)
    
    
    # Not implemented
    def test_buildProject(self):
 
        self.assertTrue(True)
    
    
    # Not implemented
    def test_buildImage(self):

        self.assertTrue(True)
    
    
    # Not implemented
    def test_exportProject(self):

        self.assertTrue(True)
    
    
    # Not implemented
    def test_importProject(self):
 
        self.assertTrue(True)
    
    
    # Not implemented
    def test_exportBuild(self):

        self.assertTrue(True)
    
    
    # Not implemented
    def test_runContainer(self):

        self.assertTrue(True)
    
    
    # Not implemented
    def test_stopContainer(self):
 
        self.assertTrue(True)

    
if __name__ == '__main__':
    unittest.main()    
