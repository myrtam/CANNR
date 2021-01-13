"""
CANNR TM analytics container building tool example showing Python function 
to expose as a Web service.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

import random

# Return a random number in a dictionary.
# We want to expose this as a Web service.
def rand():

    return {'result': random.random()}
