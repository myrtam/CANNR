"""
CANNR TM analytics container building tool Flask worker shutdown module.
Utility to shut down a Flask (werkzeug) worker.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

from flask import request

# Shuts down a werkzeug worker.
def shutdown():
    s = request.environ.get('werkzeug.server.shutdown')
    if not func:
        print('Unable to shut down server normally')
        sys.exit(1)
    s()
