
# Python script for running cannR stand alone 

import cannrcore as crc
import cannrbuild as cnb
import sys

project = crc.readJSONFile(sys.argv[1])
name = project.get('name', 'Unknown')

context = crc.readJSONFile(sys.argv[2])

#cnb.buildProject(project, context)
cnb.buildFromFile(sys.argv[1], context)

print(f'Project {name} built successfully!')
