"""
CANNR TM analytics container building tool Python service script.
Module that calls other modules to provide Web services.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

"""
Generated 2021-03-20 20:50:03
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
app.url_map.strict_slashes = False
cnr__workerID = str(uuid.uuid4())
cnr__credentials = None
cnr__lastUpdateID = None

# Shut down the worker
@app.route("/shutdown/tool", methods=["POST"])
def shutdown():
	shutdown.shutdown()
	return "Shutting down..."

# Service createproject in module services
@app.route("/services/tool/services/createproject/<projectname>", methods=["POST"])
def s_1(projectname, ):
	try:
		resources = {"projectname": projectname, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.createProject(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service deleteproject in module services
@app.route("/services/tool/services/deleteproject/<projectname>", methods=["GET"])
def s_2(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.deleteProject(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service getproject in module services
@app.route("/services/tool/services/getproject/<projectname>/<timestamp>", methods=["GET"])
def s_3(projectname, timestamp, ):
	try:
		resources = {"projectname": projectname, "timestamp": timestamp, }
		output = m_1.getProject(resources, )
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
@app.route("/services/tool/services/uploadfolder/<projectname>/<foldername>", methods=["POST"])
def s_5(projectname, foldername, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, }
		output = m_1.uploadFolder(resources, request, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service deletefolder in module services
@app.route("/services/tool/services/deletefolder/<projectname>", methods=["GET"])
def s_6(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.deleteFolder(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service updateproject in module services
@app.route("/services/tool/services/updateproject/<projectname>", methods=["POST"])
def s_7(projectname, ):
	try:
		resources = {"projectname": projectname, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateProject(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service updatemodule in module services
@app.route("/services/tool/services/updatemodule/<projectname>/<foldername>/<modulename>", methods=["POST"])
def s_8(projectname, foldername, modulename, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, "modulename": modulename, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateModule(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service buildproject in module services
@app.route("/services/tool/services/buildproject/<projectname>/<buildRun>", methods=["POST"])
def s_9(projectname, buildRun, ):
	try:
		resources = {"projectname": projectname, "buildRun": buildRun, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.buildProject(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service buildimage in module services
@app.route("/services/tool/services/buildimage/<projectname>", methods=["GET"])
def s_10(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.buildImage(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service exportproject in module services
@app.route("/services/tool/services/exportproject/<projectname>", methods=["GET"])
def s_11(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.exportProject(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service importproject in module services
@app.route("/services/tool/services/importproject/<projectname>", methods=["POST"])
def s_12(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.importProject(resources, request, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service exportbuild in module services
@app.route("/services/tool/services/exportbuild/<projectname>", methods=["GET"])
def s_13(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.exportBuild(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service runcontainer in module services
@app.route("/services/tool/services/runcontainer/<projectname>", methods=["GET"])
def s_14(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.runContainer(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service stopcontainer in module services
@app.route("/services/tool/services/stopcontainer/<projectname>", methods=["GET"])
def s_15(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.stopContainer(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service getstatus in module services
@app.route("/services/tool/services/getstatus/<projectname>", methods=["GET"])
def s_16(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.getStatus(resources, )
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

# Service sendfolder in module services
@app.route("/services/tool/services/sendfolder/<projectname>/<foldername>", methods=["POST"])
def s_19(projectname, foldername, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, }
		output = m_1.sendFolder(resources, request, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service sendFile in module services
@app.route("/services/tool/services/sendFile/<projectname>/<foldername>/<filename>", methods=["POST"])
def s_20(projectname, foldername, filename, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, "filename": filename, }
		output = m_1.sendFile(resources, request, )
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
