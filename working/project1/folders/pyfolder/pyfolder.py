"""
CANNR TM analytics container building tool Python service script.
Module that calls other modules to provide Web services.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

"""
Generated 2021-02-20 21:13:13
"""
import json
import os
import sys
import logging
import uuid
import pandas
from flask import Flask, render_template, request, Response
import cannrcore as cc
import cannrio as ci


os.chdir("/folders/pyfolder/pyfolder")
m_1 = cc.importPackage("m_1", "/folders/pyfolder/pyfolder/sum.py")
m_2 = cc.importPackage("m_2", "/folders/pyfolder/pyfolder/rand.py")

app = Flask(__name__)
cnr__workerID = str(uuid.uuid4())
cnr__credentials = None
cnr__lastUpdateID = None

# Shut down the worker
@app.route("/shutdown/pyfolder", methods=["POST"])
def shutdown():
	shutdown.shutdown()
	return "Shutting down..."

# Service sum in module sum
@app.route("/services/pyfolder/sum/sum", methods=["POST"])
def s_1():
	try:
		inputObject = ci.toInputType(request, inputParseType="array")
		output = m_1.calcSum(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Refresh objects in module sum
@app.route("/refreshObjects/pyfolder/sum", methods=["POST"])
def refresh_1():
	# TODO: STUB - TO BE ADDED
	# TODO: PASS BACK cnr__workerID IN THE RESPONSE
	return({})

# Update credentials in module sum
@app.route("/updateCredentials/pyfolder/sum", methods=["POST"])
def updateCred_1():
	parsedBody = json.loads(request.get_json())
	updateID = parsedBody.get("updateID", None)
	if updateID and updateID != cnr__lastUpdateID:
		cnr__lastUpdateID = updateID
		
	return({"workerID": cnr__workerID})


# Service rand in module rand
@app.route("/services/pyfolder/rand/rand", methods=["GET"])
def s_2():
	try:
		output = m_2.rand()
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Refresh objects in module rand
@app.route("/refreshObjects/pyfolder/rand", methods=["POST"])
def refresh_2():
	# TODO: STUB - TO BE ADDED
	# TODO: PASS BACK cnr__workerID IN THE RESPONSE
	return({})

# Update credentials in module rand
@app.route("/updateCredentials/pyfolder/rand", methods=["POST"])
def updateCred_2():
	parsedBody = json.loads(request.get_json())
	updateID = parsedBody.get("updateID", None)
	if updateID and updateID != cnr__lastUpdateID:
		cnr__lastUpdateID = updateID
		
	return({"workerID": cnr__workerID})


# Run the app.
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(sys.argv[1]))
