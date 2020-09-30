"""
CANNR TM tool example showing Python function to expose as a Web service.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import json
import numpy as np

# Module info
rtModuleInfo = {
    "moduleName": "Python cannR sum test module",
    "moduleVersion": "0.1.0"
    }

# Calculates the sum of the elements in an array.
# Sample input is {"data": [1,2,3]}
def calcSum(
    pInput     # Input dictionary
    ):

    data = pInput.get("data", None)
    if data:
        return {'sum': int(np.sum(np.array(data)))}
    
    return 0.0

