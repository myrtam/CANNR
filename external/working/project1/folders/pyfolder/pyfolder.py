"""
CANNR TM analytics container building tool Python service script.
Module that calls other modules to provide Web services.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

"""
Generated 2021-01-13 02:20:40
"""
import json
import os
import sys
import logging
import uuid
import pandas
from flask import Flask, render_template, request
import cannrcore as cnr


os.chdir("/folders/pyfolder/pyfolder")
m_1 = cnr.importPackage("m_1", "/folders/pyfolder/pyfolder/rand.py")
m_2 = cnr.importPackage("m_2", "/folders/pyfolder/pyfolder/rand.py")

app = Flask(__name__)
workerID = str(uuid.uuid4())
credentials = None
lastUpdateID = None

# Shut down the worker
@app.route("/shutdown/pyfolder", methods=["POST"])
def shutdown():
	shutdown.shutdown()
	return "Shutting down..."

# Service rand in module rand
@app.route("/services/pyfolder/rand/rand", methods=["GET"])
def s_1():
	output = m_1.rand()
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)

# Refresh objects in module rand
@app.route("/refreshObjects/pyfolder/rand", methods=["POST"])
def refresh_1():
	# TODO: STUB - TO BE ADDED
	# TODO: PASS BACK workerID IN THE RESPONSE
	return({})

# Update credentials in module rand
@app.route("/updateCredentials/pyfolder/rand", methods=["POST"])
def updateCred_1():
	parsedBody = json.loads(request.get_json())
	updateID = parsedBody.get("updateID", None)
	if updateID and updateID != lastUpdateID:
		lastUpdateID = updateID
		
	return({"workerID": workerID})

# Service sum in module sum
@app.route("/services/pyfolder/sum/sum", methods=["POST"])
def s_2():
	output = m_2.rand(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)

# Refresh objects in module sum
@app.route("/refreshObjects/pyfolder/sum", methods=["POST"])
def refresh_2():
	# TODO: STUB - TO BE ADDED
	# TODO: PASS BACK workerID IN THE RESPONSE
	return({})

# Update credentials in module sum
@app.route("/updateCredentials/pyfolder/sum", methods=["POST"])
def updateCred_2():
	parsedBody = json.loads(request.get_json())
	updateID = parsedBody.get("updateID", None)
	if updateID and updateID != lastUpdateID:
		lastUpdateID = updateID
		
	return({"workerID": workerID})


# Run the app.
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(sys.argv[1]))
