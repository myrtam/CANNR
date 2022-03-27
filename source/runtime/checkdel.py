"""
CANNR TM analytics container building tool delete/overwrite confirm.
Returns directory that could be deleted or overwritten by the build process.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import cannrcore as cc
import sys

project = cc.readJSONFile(sys.argv[1])

context = cc.readJSONFile(sys.argv[2])

#print('The directory')
print(cc.getWorkingPath(project, context))
#print('and its descendants will be deleted or overwritten.')
