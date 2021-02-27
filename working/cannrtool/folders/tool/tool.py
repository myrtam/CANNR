"""
CANNR TM analytics container building tool Python service script.
Module that calls other modules to provide Web services.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
"""

"""
Generated 2021-02-27 17:30:52
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

# Service createproject_ in module services
@app.route("/services/tool/services/createproject_", methods=["POST"])
def s_1():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.createProject_(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service createproject in module services
@app.route("/services/tool/services/createproject/<projectname>", methods=["POST"])
def s_2(projectname, ):
	try:
		resources = {"projectname": projectname, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.createProject(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service deleteproject_ in module services
@app.route("/services/tool/services/deleteproject_", methods=["POST"])
def s_3():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.deleteProject_(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service deleteproject in module services
@app.route("/services/tool/services/deleteproject/<projectname>", methods=["GET"])
def s_4(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.deleteProject(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service getproject_ in module services
@app.route("/services/tool/services/getproject_", methods=["GET"])
def s_5():
	try:
		output = m_1.getProject(request.args.to_dict(), )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service getproject in module services
@app.route("/services/tool/services/getproject/<projectname>/<timestamp>", methods=["GET"])
def s_6(projectname, timestamp, ):
	try:
		resources = {"projectname": projectname, "timestamp": timestamp, }
		output = m_1.getProject(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service getprojects in module services
@app.route("/services/tool/services/getprojects", methods=["GET"])
def s_7():
	try:
		output = m_1.getProjects()
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service uploadfolder_ in module services
@app.route("/services/tool/services/uploadfolder_", methods=["POST"])
def s_8():
	try:
		output = m_1.uploadFolder(request.args.to_dict(), request, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service uploadfolder in module services
@app.route("/services/tool/services/uploadfolder/<projectname>/<foldername>", methods=["POST"])
def s_9(projectname, foldername, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, }
		output = m_1.uploadFolder(resources, request, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service deletefolder_ in module services
@app.route("/services/tool/services/deletefolder_", methods=["POST"])
def s_10():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.deleteFolder_(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service deletefolder in module services
@app.route("/services/tool/services/deletefolder/<projectname>", methods=["GET"])
def s_11(projectname, ):
	try:
		resources = {"projectname": projectname, }
		output = m_1.deleteFolder(resources, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service updateproject_ in module services
@app.route("/services/tool/services/updateproject_", methods=["POST"])
def s_12():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateProject_(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service updateproject in module services
@app.route("/services/tool/services/updateproject/<projectname>", methods=["POST"])
def s_13(projectname, ):
	try:
		resources = {"projectname": projectname, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateProject(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service updatemodule_ in module services
@app.route("/services/tool/services/updatemodule_", methods=["POST"])
def s_14():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateModule(request.args.to_dict(), inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service updatemodule in module services
@app.route("/services/tool/services/updatemodule/<projectname>/<foldername>/<modulename>", methods=["POST"])
def s_15(projectname, foldername, modulename, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, "modulename": modulename, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.updateModule(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service buildproject_ in module services
@app.route("/services/tool/services/buildproject_", methods=["POST"])
def s_16():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.buildProject_(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service buildproject in module services
@app.route("/services/tool/services/buildproject/<projectname>", methods=["POST"])
def s_17(projectname, ):
	try:
		resources = {"projectname": projectname, }
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.buildProject(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service buildimage in module services
@app.route("/services/tool/services/buildimage", methods=["POST"])
def s_18():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.buildImage(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service exportproject in module services
@app.route("/services/tool/services/exportproject", methods=["POST"])
def s_19():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.exportProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service importproject in module services
@app.route("/services/tool/services/importproject", methods=["POST"])
def s_20():
	try:
		output = m_1.importProject(request.args.to_dict(), request, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service exportbuild in module services
@app.route("/services/tool/services/exportbuild", methods=["POST"])
def s_21():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.exportBuild(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service runcontainer in module services
@app.route("/services/tool/services/runcontainer", methods=["POST"])
def s_22():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.runContainer(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service stopcontainer in module services
@app.route("/services/tool/services/stopcontainer", methods=["POST"])
def s_23():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.stopContainer(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service getstatus in module services
@app.route("/services/tool/services/getstatus", methods=["POST"])
def s_24():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.getStatus(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service renameproject in module services
@app.route("/services/tool/services/renameproject", methods=["POST"])
def s_25():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.renameProject(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service renamefolder in module services
@app.route("/services/tool/services/renamefolder", methods=["POST"])
def s_26():
	try:
		inputObject = ci.toInputType(request, inputParseType="default")
		output = m_1.renameFolder(inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service sendfolder in module services
@app.route("/services/tool/services/sendfolder/<projectname>/<foldername>", methods=["POST"])
def s_27(projectname, foldername, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, }
		output = m_1.sendFolder(resources, request, )
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service sendmodule in module services
@app.route("/services/tool/services/sendmodule/<projectname>/<foldername>/<modulename>", methods=["POST"])
def s_28(projectname, foldername, modulename, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, "modulename": modulename, }
		inputObject = ci.toInputType(request, inputParseType="none")
		output = m_1.sendModule(resources, inputObject)
		return Response(ci.serviceOutput(output, "default"), content_type="application/json")
	except Exception as err:
		return {"error": str(err)}

# Service sendobject in module services
@app.route("/services/tool/services/sendobject/<projectname>/<foldername>", methods=["POST"])
def s_29(projectname, foldername, ):
	try:
		resources = {"projectname": projectname, "foldername": foldername, }
		output = m_1.sendObject(resources, request, )
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
