"""
CANNR TM analytics container building tool example showing Python function 
to expose as a Web service.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import numpy as np

# Calculates the sum of the elements in an array.
# We want to expose this as a Web service.
# Sample input is {"data": [1,2,3]}
def calcSum(pInput):

    data = pInput.get("data", None)
    if data:
        return {'sum': int(np.sum(np.array(data)))}
    
    return 0.0

