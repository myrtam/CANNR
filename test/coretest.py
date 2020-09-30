"""
Test harness for cannrcore.py
"""

import sys
import os
import json
import unittest

sys.path.append('../source/base_image/cannr/lib')

import cannrcore as cnc

class TestCannrCore(unittest.TestCase):
    
    # Stub
    def setUp(self):
        pass

    # Completed
    def test_RTAMError(self):
        message = None
        errorCode = None
        try:
            raise cnc.RTAMError(cnc.noDirectorySpecMsg, cnc.noDirectorySpecCode)
        except cnc.RTAMError as err:
            message = err.message
            errorCode = err.errorCode
            
        self.assertTrue(message == cnc.noDirectorySpecMsg and errorCode == cnc.noDirectorySpecCode)
    
    # Stub,  Not currently used.
    # TODO:  Complete this
    def test_EventCalendar(self):
    
        self.assertTrue(True)
    
    # Completed
    def test_importPackage(self):
        
        module = cnc.importPackage('cnc', '../source/base_image/cannr/lib/cannrcore.py')
        
        self.assertTrue(module)
    
    # Completed
    def test_isStdPkg(self):
    
        self.assertTrue(cnc.isStdPkg('os'))
    
    # Completed
    def test_getLibPath(self):
    
        self.assertTrue(cnc.getLibPath())
    
    # Completed
    def test_isInstPkg(self):
    
        self.assertTrue(cnc.isInstPkg('numpy'))
    
    # Completed
    def test_isRInstPkg(self):
    
        self.assertTrue(cnc.isRInstPkg('mgcv'))
    
    # Stub,  Not currently used.
    # TODO:  Complete this
    def test_setLogFile(self):
    
        self.assertTrue(True)
    
    # Completed
    def test_hashPassword(self):
    
        self.assertEqual(
            cnc.hashPassword('123456', '4f599ae3-cf4f-479c-94d0-c0938f96b468', 'SHA-256'),
            'DA42EA30B55C5460BA34E9FB5F2B364BFAB48DEF68AF560050A9F3E76065A919')
    
    # Completed
    def test_buildHash(self):
        
        pwInfo = cnc.buildHash('123456', 'SHA-256')
    
        self.assertEqual(pwInfo.get('hashAlgorithm', ''), 'SHA-256')
        self.assertTrue(pwInfo.get('salt', ''))
        self.assertTrue(pwInfo.get('hash', ''))
    
    # Completed
    def test_authenticate(self):
        
        pwInfo = cnc.buildHash('123456', 'SHA-256')
    
        self.assertTrue(cnc.authenticate('123456',
            pwInfo.get('hashAlgorithm', ''),
            pwInfo.get('hash', ''),
            pwInfo.get('salt', '')))
    
    # Completed
    def test_readJSONFile(self):
    
        x = cnc.readJSONFile('../examples/project1/project.json')
        self.assertTrue(json.dumps(x))
    
    # Completed
    def test_getFolders(self):
        
        project = cnc.readJSONFile('../examples/project1/project.json')
        self.assertTrue(cnc.getFolders(project))
    
    # Completed
    def test_getFolder(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        self.assertTrue(cnc.getFolder('rFolder', project))
    
    # Completed
    def test_getFolderNames(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folderNames = cnc.getFolderNames(project)
        self.assertTrue('rFolder' in folderNames)
    
    # Completed
    def test_getModules(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        self.assertTrue(cnc.getModules(folder))
    
    # Completed
    def test_getModule(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        self.assertTrue(cnc.getModule('iris', folder))
    
    # Completed
    def test_getModuleNames(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        moduleNames = cnc.getModuleNames(folder)
        self.assertTrue('iris' in moduleNames)
    
    # Completed
    def test_getServices(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        module = cnc.getModule('iris', folder)
        self.assertTrue(cnc.getServices(module))
    
    # Completed
    def test_getServiceNames(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        module = cnc.getModule('iris', folder)
        serviceNames = cnc.getServiceNames(module)
        self.assertTrue('predPLengthSLength' in serviceNames)
    
    # Completed
    def test_getService(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        module = cnc.getModule('iris', folder)
        self.assertTrue(cnc.getService('predPLengthSLength', module))
    
    # Completed
    def test_getRelativePath(self):
        
        path = '/examples/project1/pyFolder'.replace('/', os.path.sep)
        self.assertEqual(cnc.getRelativePath(path), 'pyFolder')
    
    # Completed
    def test_getHome(self):
    
        project = cnc.readJSONFile('../examples/project1/project.json')
        folders = cnc.getFolders(project)
        folder = cnc.getFolder('rFolder', project)
        path = '/folders/rFolder/folder2'.replace('/', os.path.sep)
        self.assertEqual(cnc.getHome('rFolder', folder), path)
    
    # Completed
    def test_saveProject(self):
        
        project = cnc.readJSONFile('../examples/project1/project.json')
        context = cnc.readJSONFile('../source/runtime/context.json')
        authPolicy = context.get('authPolicy')
        authPolicyLen = authPolicy.get('authPolicyLen')
        authPolicyChars = authPolicy.get('authPolicyChars')
        result = cnc.saveProject(project, 'project1.json', authPolicyLen, authPolicyChars)
        self.assertEqual(result, 1)

        authentication = {
            'password': '123456',
            'adminID': 'IRule'
            }
        project['authentication'] = authentication
        result = cnc.saveProject(project, 'project1.json', authPolicyLen, authPolicyChars)
        self.assertEqual(result, 3)
    
        authentication = {
            'password': '12aB~skjhdfkdG',
            'adminID': 'IRule'
            }
        project['authentication'] = authentication
        result = cnc.saveProject(project, 'project1.json', authPolicyLen, authPolicyChars)
        self.assertEqual(result, 0)
    
if __name__ == '__main__':
    unittest.main()    
    
