"""
CANNR TM analytics container building tool Python service script.
Module that calls other modules to provide Web services.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

"""
Generated 2021-02-21 20:38:42
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


os.chdir("/folders/tool/tool")
m_1 = cc.importPackage("m_1", "/folders/tool/tool/services.py")

app = Flask(__name__)
cnr__workerID = str(uuid.uuid4())
cnr__credentials = None
cnr__lastUpdateID = None

# Shut down the worker
@app.route("/shutdown/tool", methods=["POST"])
def shutdown():
	shutdown.shutdown()
	return "Shutting down..."

# Service createproject in module services
@app.route("/services/tool/services/createproject", methods=["POST"])
def s_1():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.createProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service deleteproject in module services
@app.route("/services/tool/services/deleteproject", methods=["POST"])
def s_2():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.deleteProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service getproject in module services
@app.route("/services/tool/services/getproject", methods=["GET"])
def s_3():
	try:
		output = m_1.getProject(request.args.to_dict())
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service getprojects in module services
@app.route("/services/tool/services/getprojects", methods=["GET"])
def s_4():
	try:
		output = m_1.getProjects()
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service uploadfolder in module services
@app.route("/services/tool/services/uploadfolder", methods=["POST"])
def s_5():
	try:
		output = m_1.uploadFolder(request.args.to_dict(),request)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service deletefolder in module services
@app.route("/services/tool/services/deletefolder", methods=["POST"])
def s_6():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.deleteFolder(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service updateproject in module services
@app.route("/services/tool/services/updateproject", methods=["POST"])
def s_7():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service updatemodule in module services
@app.route("/services/tool/services/updatemodule", methods=["POST"])
def s_8():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateModule(request.args.to_dict(),inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service buildproject in module services
@app.route("/services/tool/services/buildproject", methods=["POST"])
def s_9():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.buildProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service buildimage in module services
@app.route("/services/tool/services/buildimage", methods=["POST"])
def s_10():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.buildImage(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service exportproject in module services
@app.route("/services/tool/services/exportproject", methods=["POST"])
def s_11():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.exportProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service importproject in module services
@app.route("/services/tool/services/importproject", methods=["POST"])
def s_12():
	try:
		output = m_1.importProject(request.args.to_dict(),request)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service exportbuild in module services
@app.route("/services/tool/services/exportbuild", methods=["POST"])
def s_13():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.exportBuild(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service runcontainer in module services
@app.route("/services/tool/services/runcontainer", methods=["POST"])
def s_14():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.runContainer(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service stopcontainer in module services
@app.route("/services/tool/services/stopcontainer", methods=["POST"])
def s_15():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.stopContainer(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service getstatus in module services
@app.route("/services/tool/services/getstatus", methods=["POST"])
def s_16():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.getStatus(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service renameproject in module services
@app.route("/services/tool/services/renameproject", methods=["POST"])
def s_17():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.renameProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}
# Service renamefolder in module services
@app.route("/services/tool/services/renamefolder", methods=["POST"])
def s_18():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.renameFolder(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Refresh objects in module services
@app.route("/refreshObjects/tool/services", methods=["POST"])
def refresh_1():
	# TODO: STUB - TO BE ADDED
	# TODO: PASS BACK cnr__workerID IN THE RESPONSE
	return({})

# Update credentials in module services
@app.route("/updateCredentials/tool/services", methods=["POST"])
def updateCred_1():
	parsedBody = json.loads(request.get_json())
	updateID = parsedBody.get("updateID", None)
	if updateID and updateID != cnr__lastUpdateID:
		cnr__lastUpdateID = updateID
		
	return({"workerID": cnr__workerID})


# Run the app.
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=int(sys.argv[1]))
