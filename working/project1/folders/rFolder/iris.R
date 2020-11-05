# Change to the source directory
setwd("/folders/rfolder/folder2")

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
# Generated 2020-11-04 20:12:16
################################################################################

library(jsonlite)
library(urltools)

workerID <- Sys.getenv("WORKER_ID")
credentials <- NULL
lastUpdateID <- NULL

# Service predplengthslength in module iris in folder rfolder
#' @get /services/rfolder/iris/predplengthslength
function(req) {
	queryParams <- param_get(paste0("http://x.com/x", req$QUERY_STRING))
	output <- predPLengthSLength(queryParams)
	return(output)
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
	if (updateID != lastUpdateID) {
		lastUpdateID <- updateID
		credentials <- listFromJSON[["credentials"]]
	}
	return(list("workerID" = workerID))
}
