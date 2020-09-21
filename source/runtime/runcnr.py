
# Python script for running cannR stand alone 

import cannrcore as crc
import cannrbuild as cnr
import sys

project = crc.readJSONFile(sys.argv[1])
name = project.get('name', 'Unknown')

context = crc.readJSONFile(sys.argv[2])

cnr.buildProject(project, context)

print(f'Project {name} built successfully!')