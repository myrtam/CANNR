"""
Test harness for cannrcore.py
"""

import sys
import os
import json
import shutil
import unittest

sys.path.append('../source/base_image/cannr/lib')
sys.path.append('../source/runtime')

import cannrcore as cnc
import cannrbuild as cnb

class TestCannrBuild(unittest.TestCase):
    
    # Stub
    def setUp(self):
        pass

    # Completed
    def test_getDockerfile(self):

        dockerFileText = cnb.getDockerfile()
        print(dockerFileText)
        self.assertTrue(dockerFileText)
    
    # Completed
    def test_buildCodeLine(self):

        codeLine = cnb.buildCodeLine(3, ['a','b','c','d'])
        print(codeLine)
        self.assertTrue(True)
    
    # Completed
    def test_buildPyFolder(self):

        project = cnc.readJSONFile('../examples/project1/project.json')
        pyFolderText = cnb.buildPyFolder('pyFolder', project)
        print(pyFolderText)
        self.assertTrue(pyFolderText)
    
    # Completed
    def test_buildRModuleEpilogue(self):

        project = cnc.readJSONFile('../examples/project1/project.json')
        rFolderText = cnb.buildRModuleEpilogue('rFolder', 'iris', project)
        print(rFolderText)
        self.assertTrue(rFolderText)
    
    # Completed
    def test_checkWorkingDirectory(self):
        
        context = cnc.readJSONFile('../source/runtime/context.json')
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.checkWorkingDirectory(context)
        ex = result.exception
        self.assertEqual(ex.message, cnc.noDirectoryMsg)
        self.assertEqual(ex.errorCode, cnc.noDirectoryCode)
        
        context = cnc.readJSONFile('../source/runtime/context.json')
        workingDirectory = context['workingDirectory']
        workingDirectory['path'] = '../working'
        self.assertTrue(cnb.checkWorkingDirectory(context))
    
    # Completed
    def test_existsDirectory(self):

        self.assertTrue(cnb.existsDirectory('/'))
        self.assertFalse(cnb.existsDirectory('/doesnotexist'))
    
    # Completed
    def test_getFolderPath(self):

        folderPath = cnb.getFolderPath('../working/project1', 'folder1')
        self.assertEqual(folderPath, '../working/project1/folder1')
    
    # Completed
    def test_initBuild(self):

        project = cnc.readJSONFile('../examples/project1/project.json')
        context = cnc.readJSONFile('context.json')
        
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.initBuild(None, context)
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.initBuild(project, None)
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.initBuild([], context)
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.initBuild(project, [])
        
        project['name'] = None
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.initBuild(project, context)
        
        project = cnc.readJSONFile('../examples/project1/project.json')
        context['baseImage'] = None
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.initBuild(project, context)
        
        context = cnc.readJSONFile('context.json')
        context['workingDirectory'] = {'path': '../doesnotexist'}
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.initBuild(project, context)
        
        context = cnc.readJSONFile('context.json')
        self.assertEqual(cnb.initBuild(project, context), os.path.abspath('../working/project1'))
        
    
    # Completed
    def test_copySource(self):

        # Setup
        context = cnc.readJSONFile('context.json')
        workingDirectory = context.get('workingDirectory')
        workingPath = workingDirectory.get('path')
        foldersPath = workingPath + os.path.sep + 'folders'
        if cnb.existsDirectory(foldersPath):
            shutil.rmtree(foldersPath)
        os.mkdir(foldersPath)
        projectFilePath = os.path.abspath('../examples/project1/project.json')
        project = cnc.readJSONFile(projectFilePath)
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)

        # Make sure that copySource raises appropriate exceptions.
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.copySource(None, foldersPath, 'rFolder')
        folder['source'] = None
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.copySource(folder, foldersPath, 'rFolder')
        project = cnc.readJSONFile(projectFilePath)
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        folder['source'] = {}
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.copySource(folder, foldersPath, 'rFolder')
        project = cnc.readJSONFile(projectFilePath)
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        folder['source'] = {'sourceType': 'file'}
        with self.assertRaises(cnc.RTAMError) as result:
            cnb.copySource(folder, foldersPath, 'rFolder')

        # Ensure that copySource does not fail.
        project = cnc.readJSONFile(projectFilePath)
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        failed = False
        try:
            cnb.copySource(folder, foldersPath, 'rFolder')
        except cnc.RTAMError as err:
            failed = True
        self.assertFalse(failed)

    # Completed
    def test_getPortRange(self):

        projectFilePath = os.path.abspath('../examples/project1/project.json')
        project = cnc.readJSONFile(projectFilePath)
        self.assertEqual(cnb.getPortRange(project), [4000,4500])
    
    # Completed
    def test_walkNumber(self):

        projectFilePath = os.path.abspath('../examples/project1/project.json')
        project = cnc.readJSONFile(projectFilePath)
        cnb.walkNumber(project)
        self.assertTrue(project['folders']['pyFolder']['modules']['sum']['nodeNumber'])
    
    # Completed
    def test_buildProject(self):

        projectFilePath = os.path.abspath('../examples/project1/project.json')
        project = cnc.readJSONFile(projectFilePath)
        context = cnc.readJSONFile('context.json')
        failed = False
        try:
            cnb.buildProject(project, context)
        except cnc.RTAMError as err:
            failed = True
        self.assertFalse(failed)
    
    
if __name__ == '__main__':
    unittest.main()    
    
