# Change to the source directory
setwd("/folders/rfolder/rfolder")

# CANNR TM analytics container building tool example showing R function to
# expose as a Web service.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

# Return the predicted petal length from sepal length for virginica species
# of irises.

# Load the model
irisModel <- readRDS('models/irisModel.rds')

# Function to predict petal length from sepal length
# Example:
# http://<host>/services/rFolder/iris/predPLengthSLength?x=6.5
predPLengthSLength <- function(new) {

	# Convert input to numeric
	new$x <- as.double(new$x)

	# Find the predicted petal length
	predicted <- predict(irisModel, new, se.fit = TRUE)

	# Return the prediction merged with the input
	return(merge(new, predicted))

}



################################################################################
# CANNR TM analytics container building tool R service script.
# Wrapper module that provides Web services.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com
################################################################################

################################################################################
# Generated 2021-04-18 00:34:37
################################################################################

library(jsonlite)
library(urltools)
library(cannrio)

cnr__workerID <- Sys.getenv("WORKER_ID")
cnr__credentials <- NULL
cnr__lastUpdateID <- NULL

# Service predplengthslength in module iris in folder rfolder
#* @serializer unboxedJSON
#* @get /services/rfolder/iris/predplengthslength
function(req) {
	queryParams <- param_get(paste0("http://x.com/x", req$QUERY_STRING))
	outputObject <- predPLengthSLength(queryParams)
	return(cnrToJSONList(outputObject, outputParseType="default"))
}

# Refresh objects in module iris
#' @post /refreshObjects/rfolder/iris
function(req) {
	# TODO:  STUB
	return
}

# Update credentials in module iris
#' @post /updateCredentials/rfolder/iris
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
