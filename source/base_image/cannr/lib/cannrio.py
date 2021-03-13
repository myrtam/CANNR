"""
CANNR TM analytics container building tool service IO functions.
Copyright 2021 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import numpy
import pandas
from numpyencoder import NumpyEncoder
from flask import request
from werkzeug.utils import secure_filename
import re
import shutil
import json
import os
import zipfile
import tempfile

badRequestMsg = "Bad request"
badRequestCode = 2001

badFileMsg = "Bad file name"
badFileCode = 2002

multiDirMsg = "Multiple directories in archive"
multiDirCode = 2003

noDirMsg = "No directory in archive"
noDirCode = 2004


# Compile the regular expression for later use
regexExp = re.compile('\s*\{\s*"data"\s*:\s*([\{\[].*[\}\]])\s*\}\s*', re.DOTALL)

# Returns the data portion of a JSON input. 
def getDataPortion(jsonInput):

    # Try to extract the data portion
    m = regexExp.match(jsonInput)

    # If something matches, return it, otherwise None
    if m and m.lastindex>0:
        return m[1]
    else:
        return None

# Does tests to see what error to raise after parsing fails.
def testInput(jsonInput, err):

    # Try to see if there are too many keys.
    try:
        testDict = json.loads(jsonInput)
        # If too many elements, throw exception.
        if testDict and len(testDict.keys()) > 1:
            raise Exception(tooManyKeysMsg)
    # If something else, throw exception.
    except Exception as err2:
        raise Exception(errorParsingDataMsg + ': ' + str(err2))

    # If not too many elements but something else happened, throw exception.
    raise Exception(errorParsingDataMsg + ': ' + str(err))


# Converts the input JSON into a Pandas DataFrame.
def toDataFrame(dataString):

    return pandas.read_json(dataString)


# Converts the input JSON into a Python dictionary or list.
def toDictionary(dataString):

    return json.loads(dataString)


# Converts the input JSON into a Numpy array.
def toNumpyArray(dataString):

    # Try to convert to a list, then to a Numpy array.
    return numpy.asarray(json.loads(dataString))


# Handles parsing of the POST service input, given the request.
def toInputType(request, inputParseType):

    # Check to make sure the request exists
    if not request:
        raise Exception(badRequestMsg)

    # Check to make sure the request isn't too big
    #if bodySizeLimit and bodySizeLimit > 0 and request.content_length > bodySizeLimit:
    #    raise Exception(requestTooLargeMsg + ': ' + str(request.content_length + ' bytes'))

    # Get the input parse type
    inputType = inputParseType if inputParseType else 'none'
    
    # Get the body input as text
    jsonInput = request.get_data(as_text=True)

    # Get the "data" element of the JSON input.
    dataString = getDataPortion(jsonInput)

    if not dataString:
        raise Exception(noInputDataMsg)

    try:
        
        # Map the input to the appropriate parser
        if inputType=='dataframe':
            return toDataFrame(dataString)
        elif inputType=='default':
            return toDictionary(dataString)
        elif inputType=='array':
            return toNumpyArray(dataString)
        else:
            return dataString
    
    except Exception as err:
        # If exception, test the input
        testInput(jsonInput, err)


# Converts the output object into a form that can be returned from the Flask handler.
# Returns a JSON serialized DataFrame if outputtype is 'dataframe', otherwise it
# returns a dictionary.
def serviceOutput(output, outputParseType):

    # Check to make sure the output exists
    if output is None:
        raise Exception(missingOutputMsg)

    # Get the input parse type
    outputType = outputParseType if outputParseType else 'none'
    
    # Map the input to the appropriate parser
    if outputType=='dataframe':
        return '{"data": ' + pandas.DataFrame.to_json(output, orient='records') + '}'
    elif outputType=='default':
        return json.dumps({'data': output}, cls=NumpyEncoder)
    else:
        return {'data': str(output)}


# Returns the first line of a byte string, along with the start and end positions. 
def getFirstLine(byteString):
    
    m = re.search(b'[^\r\n]*', byteString)
    if m:
        return m[0]
    else:
        return None


# Returns the first line of a byte string, along with the start and end positions. 
def getFilePath(byteString):
    
    #m = re.search(b'^.*\n.*filename="(.*)"\n', byteString)
    m = re.search(b'^[^\r\n]*(?:\n|\r\n)[^\r\n]*filename="([^\r\n]*)"(?:\n|\r\n)', byteString)
    
    if m and m.lastindex>0:
        return m[1].decode('utf-8') 
    else:
        return None


# Returns all file chunks in a bytes object, given the form boundary string.
# Includes the file header info. 
def getAllChunks(byteString, formBoundary):
    
    return re.findall(
        b'(' + formBoundary + b'.*?)(?:\n|\r\n)(?=' + formBoundary + b')',
        byteString, re.DOTALL)


# Strips off the first four lines of byteString, returns the rest.
def getContents(byteString):

    m = re.search(4*b'[^\r\n]*(?:\n|\r\n)' + b'(.*)', byteString, re.DOTALL)

    if m and m.lastindex>0:
        return m[1]
    else:
        return None


# Returns the subdirectory, if any associated with the file.
# E.g., if the file path is directory/file.txt, then the subdirectory is blank.
# If the file path is directory/subdirectory/file.txt.
def getSubdirectory(filePath):

    m = re.search('[\\/](.*[\\/])', filePath)
    if m and m.lastindex>0:
        return m[1]
    else:
        return ''

# Returns the file name portion of the file path.
def getFileName(filePath):
    
    m = re.search('[^\\/]*$', filePath)
    
    if m and m[0]:
        return m[0]
    else:
        return None

# Returns the file name portion of the file path.
def getDirName(filePath):
    
    m = re.search('^[^\\/]*', filePath)
    
    if m and m[0]:
        return m[0]
    else:
        return None


# Filter a list of strings based on a regex
def regexFilter(stringList, regex):

    # Return strings that match the regex
    return [str for str in stringList
        if re.search(regex, str)]


# Given multipart form data containing files as a bytes object, saves the files
# to the specified directory.  If the directory exists, replaces it.
# Returns a list of the files written.
def writeFiles(data, directory):
    
    if not data:
        return None
    
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    
    formBoundary = getFirstLine(data)
    if formBoundary:
        fileNames = []
        foldersPath = directory
        m = getAllChunks(data, formBoundary)
        for chunk in m:
            filePath = getFilePath(chunk)
            # TODO:  CHECK THAT filePath is legit
            if not filePath:
                break
            subDirPath = directory + ('' if directory.endswith('/') else '/') + getSubdirectory(filePath)
            if not os.path.isdir(subDirPath):
                os.makedirs(subDirPath)
            contents = getContents(chunk)
            fileName = getFileName(filePath)
            if not fileName or not secure_filename(fileName):
                break
            subDirFilePath = subDirPath + fileName
            fileNames.append(subDirFilePath)
            with open(subDirFilePath, "wb") as dataFile:
                dataFile.write(contents)
                
    return fileNames


# Given a bytes object containing a zipped directory, saves the files
# to the specified directory.  If the directory exists, replaces it.
# Returns a list of the files written.
def writeZipFiles(data, directory):

    # If no data, nothing to do
    if not data:
        return None

    # Get a temp directory and copy the data to a file in it
    td1 = tempfile.TemporaryDirectory()
    tempZipPath = os.path.join(td1.name, 'temp.zip')
    with open(tempZipPath, 'wb') as tempZip:
        tempZip.write(data)

    # Open the zip file
    zf = zipfile.ZipFile(tempZipPath)
    
    # Get the list of file names and check to make sure they are safe
    fileNames = []
    for fileName in zf.namelist():
        if not fileName or not secure_filename(fileName):
            raise Exception(badFileMsg)
        subDirPath = directory + ('' if directory.endswith('/') else '/') + getSubdirectory(fileName)
        subDirFilePath = subDirPath + fileName
        fileNames.append(subDirFilePath)

    # Get a temp directory and extract the contents of the zip file into it
    td2 = tempfile.TemporaryDirectory()
    zf.extractall(td2.name)

    # Remove the target directory if it exists
    if os.path.isdir(directory):
        shutil.rmtree(directory)

    # Get the source directory name, check to make sure there is only one
    sd = os.scandir(td2.name)
    dirCount = 0
    dirName = None
    for dirEntry in sd:
        if dirEntry != '__MACOSX':
            dirCount += 1
            dirName = dirEntry
        if dirCount > 1:
            raise Exception(multiDirMsg)

    # Check to make sure there is a directory to copy 
    if not dirName:
        raise Exception(noDirMsg)

    # Copy the directory
    shutil.copytree(os.path.join(td2.name, dirName), directory)
    
    # Clean up the temp directories
    td1.cleanup()
    td2.cleanup()
    
    return fileNames


# Given a bytes object containing a file, saves the file
# to the specified directory using the specified file name.
# If the file exists, replaces it.
def writeFile(data, directory, fileName):

    # If no data, nothing to do
    if not data:
        return None

    # Check to make sure file name is OK
    if not fileName or not secure_filename(fileName):
        raise Exception(badFileMsg)

    # Write out the file
    fullName = os.path.join(directory, fileName)
    with open(fullName, 'wb') as outputFile:
        outputFile.write(data)

    # Return the new full file name
    return fullName
