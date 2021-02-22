

"""
Test harness for cannrio.py
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
import cannrio as ci

class TestCannrIO(unittest.TestCase):

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


    def test_getDataPortion(self):

        self.assertEqual(ci.getDataPortion(self.jsonData), '[ [1, 2, 3],\n[4, 5, 6]\n]')

    def test_getFirstLine(self):

        firstLine = ci.getFirstLine(self.uploadData)
        self.assertEqual(firstLine, b'------WebKitFormBoundary7mqeUsPtFGhYEsuU')

    def test_getFilePath(self):

        filePath = ci.getFilePath(self.uploadData)
        self.assertEqual(filePath, 'uploadTest/file2.txt')

    def test_getAllChunks(self):

        m = ci.getAllChunks(self.uploadData, b'------WebKitFormBoundary7mqeUsPtFGhYEsuU')
        self.assertTrue(True)

    def test_getContents(self):

        m = ci.getAllChunks(self.uploadData, b'------WebKitFormBoundary7mqeUsPtFGhYEsuU')
        self.assertEqual(ci.getContents(m[0]), b'Second file.')

    def test_getDataPortion(self):

        self.assertEqual(ci.getDataPortion(self.jsonData), '[ [1, 2, 3],\n[4, 5, 6]\n]')

    def test_getSubdirectory(self):

        subDirectory = ci.getSubdirectory('xxx/yyy/zzz/file.txt')
        self.assertEqual(subDirectory, 'yyy/zzz/')

    def test_getFileName(self):

        fileName = ci.getFileName('xxx/yyy/zzz/file.txt')
        self.assertEqual(fileName, 'file.txt')

    def test_getDirName(self):

        directoryName = ci.getDirName('xxx/yyy/zzz/file.txt')
        self.assertEqual(directoryName, 'xxx')

    def test_writeFiles(self):

        fileNames = ci.writeFiles(self.uploadData, 'folders/folder123')
        self.assertTrue(True)

    def test_toDataFrame(self):

        df = ci.toDataFrame(self.dfJSON)
        self.assertEqual(pandas.DataFrame.to_json(df, orient='records'), self.dfJSON)

    def test_toDictionary(self):

        dictionary = ci.toDictionary(self.dictJSON)
        self.assertEqual(json.dumps(dictionary), self.dictJSON)

    def test_toNumpyArray(self):

        array = ci.toNumpyArray('[ [1, 2, 3],\n[4, 5, 6]\n]')
        self.assertEqual(array[1,1], 5)

 
if __name__ == '__main__':
    unittest.main()

