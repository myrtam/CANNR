"""
CANNR TM tool example showing Python function to expose as a Web service.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import time
import random

# Module info
rtModuleInfo = {
    "moduleName": "Python cannR rand test module",
    "moduleVersion": "0.1.0"
    }

# Return a random number in a dictionary.
def rand():

    return {'result': random.random()}
