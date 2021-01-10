"""
CANNR TM analytics container building tool Python service script.
Module that calls other modules to provide Web services.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

"""
Generated 2021-01-10 17:19:37
"""
import json
import os
import sys
import logging
import uuid
import pandas
from flask import Flask, render_template, request
import cannrcore as cnr


os.chdir("/folders/tool/tool")
m_1 = cnr.importPackage("m_1", "/folders/tool/tool/services.py")

app = Flask(__name__)
workerID = str(uuid.uuid4())
credentials = None
lastUpdateID = None

# Shut down the worker
@app.route("/shutdown/tool", methods=["POST"])
def shutdown():
	shutdown.shutdown()
	return "Shutting down..."

# Service createproject in module services
@app.route("/services/tool/services/createproject", methods=["POST"])
def s_1():
	output = m_1.createProject(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service deleteproject in module services
@app.route("/services/tool/services/deleteproject", methods=["POST"])
def s_2():
	output = m_1.deleteProject(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service getproject in module services
@app.route("/services/tool/services/getproject", methods=["GET"])
def s_3():
	output = m_1.getProject(request.args.to_dict())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service getprojects in module services
@app.route("/services/tool/services/getprojects", methods=["GET"])
def s_4():
	output = m_1.getProjects()
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service uploadfolder in module services
@app.route("/services/tool/services/uploadfolder", methods=["POST"])
def s_5():
	output = m_1.uploadFolder(request.args.to_dict(),request)
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service deletefolder in module services
@app.route("/services/tool/services/deletefolder", methods=["POST"])
def s_6():
	output = m_1.deleteFolder(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service updateproject in module services
@app.route("/services/tool/services/updateproject", methods=["POST"])
def s_7():
	output = m_1.updateProject(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service updatemodule in module services
@app.route("/services/tool/services/updatemodule", methods=["POST"])
def s_8():
	output = m_1.updateModule(request.args.to_dict(),request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service buildproject in module services
@app.route("/services/tool/services/buildproject", methods=["POST"])
def s_9():
	output = m_1.buildProject(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service buildimage in module services
@app.route("/services/tool/services/buildimage", methods=["POST"])
def s_10():
	output = m_1.buildImage(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service exportproject in module services
@app.route("/services/tool/services/exportproject", methods=["POST"])
def s_11():
	output = m_1.exportProject(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service importproject in module services
@app.route("/services/tool/services/importproject", methods=["POST"])
def s_12():
	output = m_1.importProject(request.args.to_dict(),request)
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service exportbuild in module services
@app.route("/services/tool/services/exportbuild", methods=["POST"])
def s_13():
	output = m_1.exportBuild(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service runcontainer in module services
@app.route("/services/tool/services/runcontainer", methods=["POST"])
def s_14():
	output = m_1.runContainer(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service stopcontainer in module services
@app.route("/services/tool/services/stopcontainer", methods=["POST"])
def s_15():
	output = m_1.stopContainer(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service renameproject in module services
@app.route("/services/tool/services/renameproject", methods=["POST"])
def s_16():
	output = m_1.renameProject(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)
# Service renamefolder in module services
@app.route("/services/tool/services/renamefolder", methods=["POST"])
def s_17():
	output = m_1.renameFolder(request.get_json())
	parsedOutput = json.dumps(output, indent=2)
	return(parsedOutput)

# Refresh objects in module services
@app.route("/refreshObjects/tool/services", methods=["POST"])
def refresh_1():
	# TODO: STUB - TO BE ADDED
	# TODO: PASS BACK workerID IN THE RESPONSE
	return({})

# Update credentials in module services
@app.route("/updateCredentials/tool/services", methods=["POST"])
def updateCred_1():
	parsedBody = json.loads(request.get_json())
	updateID = parsedBody.get("updateID", None)
	if updateID and updateID != lastUpdateID:
		lastUpdateID = updateID
		
	return({"workerID": workerID})


# Run the app.
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(sys.argv[1]))
