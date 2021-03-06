"""
Test harness for cannrcore.py
"""

import sys
import os
import json
import platform
import unittest
import pandas
import numpy as np

sys.path.append('../source/base_image/cannr/lib')

import cannrcore as cnc

class TestCannrCore(unittest.TestCase):

    # Stub
    def setUp(self):

        self.context = cnc.readJSONFile('../source/runtime/context.json')
        if platform.system() == 'Windows':
            self.project = cnc.readJSONFile('../examples/project1/winproject.json')
        else:
            self.project = cnc.readJSONFile('../examples/project1/project.json')

        self.webProject = cnc.readJSONFile('../source/webtool/project.json')

        with open('testfiles/upload.dat','rb') as uploadFile:
            self.uploadData = uploadFile.read()

        self.jsonData = ' { "data" :\n[ [1, 2, 3],\n[4, 5, 6]\n]\n}'

        self.dfJSONData = ' { "data" :\n[ {"a": 1, "b": 2, "c": 3},\n{"a": 4, "b": 5, "c": 6}\n]\n} \n'
        self.df = pandas.read_json('[{"a": 1, "b": 2, "c": 3},{"a": 4, "b": 5, "c": 6}]')
        self.dfJSON = '[{"a":1,"b":2,"c":3},{"a":4,"b":5,"c":6}]'

        self.dictJSONData = ' { "data" :\n { "stuff1": [ {"a": 1, "b": 2, "c": 3},\n{"a": 4, "b": 5, "c": 6}\n], "stuff2": 8 }\n} \n'
        self.dictJSON = json.dumps(json.loads(self.dictJSONData).get('data', None))

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
        self.assertFalse(cnc.isStdPkg('scipy'))

    # Completed
    def test_getLibPath(self):

        self.assertTrue(cnc.getLibPath())

    # Completed
    def test_isInstPkg(self):

        self.assertTrue(cnc.isInstPkg('numpy'))
        self.assertFalse(cnc.isStdPkg('scipy'))

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

        self.assertTrue(json.dumps(self.project))

    # Completed
    def test_getFolders(self):

        self.assertTrue(cnc.getFolders(self.project))

    # Completed
    def test_getFolder(self):

        folders = cnc.getFolders(self.project)
        self.assertTrue(cnc.getFolder('rfolder', self.project))

    # Completed
    def test_getFolderNames(self):

        folderNames = cnc.getFolderNames(self.project)
        self.assertTrue('rfolder' in folderNames)


    def test_getContentFolderNames(self):

        folderNames = cnc.getContentFolderNames(self.webProject)
        self.assertTrue('webtool' in folderNames)

    def test_getCodeFolderNames(self):

        folderNames = cnc.getCodeFolderNames(self.webProject)
        self.assertTrue('tool' in folderNames)

    # Completed
    def test_getModules(self):

        folders = cnc.getFolders(self.project)
        folder = cnc.getFolder('rfolder', self.project)
        self.assertTrue(cnc.getModules(folder))

    # Completed
    def test_getModule(self):

        folders = cnc.getFolders(self.project)
        folder = cnc.getFolder('rfolder', self.project)
        self.assertTrue(cnc.getModule('iris', folder))

    # Completed
    def test_getModuleNames(self):

        folders = cnc.getFolders(self.project)
        folder = cnc.getFolder('rfolder', self.project)
        moduleNames = cnc.getModuleNames(folder)
        self.assertTrue('iris' in moduleNames)

    # Completed
    def test_getServices(self):

        folders = cnc.getFolders(self.project)
        folder = cnc.getFolder('rfolder', self.project)
        module = cnc.getModule('iris', folder)
        self.assertTrue(cnc.getServices(module))

    # Completed
    def test_getServiceNames(self):

        folders = cnc.getFolders(self.project)
        folder = cnc.getFolder('rfolder', self.project)
        module = cnc.getModule('iris', folder)
        serviceNames = cnc.getServiceNames(module)
        self.assertTrue('predplengthslength' in serviceNames)

    # Completed
    def test_getService(self):

        folders = cnc.getFolders(self.project)
        folder = cnc.getFolder('rfolder', self.project)
        module = cnc.getModule('iris', folder)
        self.assertTrue(cnc.getService('predplengthslength', module))

    # Completed
    def test_getRelativePath(self):

        path = '/examples/project1/pyFolder'
        self.assertEqual(cnc.getRelativePath(path), 'pyFolder')

    # Completed
    def test_getHome(self):

        folders = cnc.getFolders(self.project)
        folder = cnc.getFolder('rfolder', self.project)
        path = '/folders/rfolder/folder2'
        self.assertEqual(cnc.getHome('rfolder', folder), path)

    def test_getWorkingPath(self):

        # Save the current directory and change to the runtime directory
        cwd = os.getcwd()
        os.chdir('../source/runtime')

        # Get the project path and the correct value
        projectPath = cnc.getWorkingPath(self.project, self.context)
        os.chdir(cwd)
        absPath = os.path.abspath('../working/project1'.replace('/', os.path.sep))

        self.assertEqual(projectPath, absPath)

    def test_legalName(self):

        self.assertFalse(cnc.legalName(''))

        self.assertTrue(cnc.legalName('nrjd9276_vnkhb'))

        self.assertFalse(cnc.legalName('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'))

        self.assertFalse(cnc.legalName('NRjd92*76_vnkhB'))

        self.assertFalse(cnc.legalName('nrjd9@276_vn&`khb'))

        self.assertFalse(cnc.legalName('NRjd9276_vnkhB'))

    def test_buildPPackMap(self):

        pPackageMap = cnc.buildPPackMap(['re==1.0','numpy>=2.0','scipy','os'])
        self.assertEqual(pPackageMap.get('re'), 're==1.0')

        pPackageMap = cnc.buildPPackMap(['re==1.0','numpy>=2.0','scipy','os', 'scipy>=2.0'])
        self.assertEqual(pPackageMap.get('scipy'), 'scipy>=2.0')

        errCode = None
        try:
            cnc.buildPPackMap(['re==1.0','numpy>=2.0','scipy','os', 'scipy>=2.0', 'numpy>=2.1'])
        except cnc.RTAMError as err:
            errCode = err.getErrorCode()
            
        self.assertTrue(errCode)
        self.assertEqual(errCode, cnc.multiplePackageSpecCode)


    # Completed
    def test_saveProject(self):

        project = cnc.readJSONFile('../examples/project1/project.json')
        authPolicy = self.context.get('authPolicy')
        authPolicyLen = authPolicy.get('authPolicyLen')
        authPolicyChars = authPolicy.get('authPolicyChars')
        result = cnc.saveProject(self.project, 'project1.json', authPolicyLen, authPolicyChars)
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

