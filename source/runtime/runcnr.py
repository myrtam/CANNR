"""
CANNR TM analytics container building tool command line program.
Python script for running the tool stand alone.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

# Python script for running cannR stand alone 

import cannrcore as crc
import cannrbuild as cnb
import sys

project = crc.readJSONFile(sys.argv[1])
name = project.get('projectName', 'Unknown')

context = crc.readJSONFile(sys.argv[2])

cnb.buildFromFile(sys.argv[1], context)

print(f'Project {name} built successfully!')
