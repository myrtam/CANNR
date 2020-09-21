"""
Test harness for smp.py
"""
import sys
import os
sys.path.append('/Users/ptendick/open-source-workspace/cannr Image/source/cannr/lib')
os.environ['PATH'] = '/Library/Frameworks/Python.framework/Versions/3.7/bin:' + os.environ['PATH']

import cannr
import smp

# Test openProcess by opening a Flask process
def test_openProcess1():
    
    return smp.openProcess(
        {"processInfo": "processInfo"},
        ['python', '/Users/ptendick/open-source-workspace/cannr Image/test/flaskSample.py', '5000', '1'])

# Test openProcess by opening a Plumber process
def test_openProcess2():
    
    return smp.openProcess(
        {"processInfo": "processInfo"},
        ['Rscript', '--vanilla', '/Users/ptendick/open-source-workspace/cannr Image/source/cannr/runApp.R', 
            '/Users/ptendick/open-source-workspace/cannr Image/test/hello.R', '5001', '2'])

# Test countPorts
def test_countPorts():
    
    projectFilePath = '/Users/ptendick/open-source-workspace/MyRTAM Service/working/project1/project.json'
    project = cannr.readJSONFile(projectFilePath)
    
    return smp.countPorts(project)
