# Change to the source directory
setwd("/folders/rfolder/rfolder")

# CANNR TM analytics container building tool example showing R function to
# expose as a Web service.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

# Sum the values of the variable x in a data frame.
# Sample JSON input is
# [{"x":1},{"x":2},{"x":3}]
sumX <- function(df) {
  
  return(sum(df$x))
  
}


################################################################################
# CANNR TM analytics container building tool R service script.
# Wrapper module that provides Web services.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com
################################################################################

################################################################################
# Generated 2021-02-21 20:36:01
################################################################################

library(jsonlite)
library(urltools)
library(cannrio)

cnr__workerID <- Sys.getenv("WORKER_ID")
cnr__credentials <- NULL
cnr__lastUpdateID <- NULL

# Service sum in module sum in folder rfolder
#* @serializer unboxedJSON
#* @post /services/rfolder/sum/sum
function(req) {
	inputObject <- cnrFromJSON(req$postBody, inputParseType="default")
	if (class(inputObject)=="data.frame" && nrow(inputObject) > 1000) {
		return(list(error = "Capacity exceeded"))
	}
	outputObject <- sumX(inputObject)
	return(cnrToJSONList(outputObject, outputParseType="default"))
}

# Refresh objects in module sum
#' @post /refreshObjects/rfolder/sum
function(req) {
	# TODO:  STUB
	return
}

# Update credentials in module sum
#' @post /updateCredentials/rfolder/sum
function(req) {
	rawJSON <- req$postBody
	listFromJSON <- fromJSON(rawJSON)
	updateID <- listFromJSON[["updateID"]]
	if (updateID != cnr__lastUpdateID) {
		cnr__lastUpdateID <- updateID
		cnr__credentials <- listFromJSON[["credentials"]]
	}
	return(list("workerID" = cnr__workerID))
}
