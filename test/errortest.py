# Test behavior of exceptions
import sys
import pandas
import json
sys.path.append('../source/base_image/cannr/lib')

import cannrcore as cc
'''
try:

    raise Exception(cc.missingOutputMsg, cc.missingOutputCode)

except Exception as err:
    print(str(err))
'''

try:

    df = pandas.read_json('[{"a": 1, "b": 2, "c": 3},{"a": 4, "b": 5, "c": 6}]')
    json.dumps(df)

except Exception as err:
    print(str(err))


