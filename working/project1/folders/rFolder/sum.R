# Change to the source directory
setwd("/folders/rfolder/folder2")

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
# Generated 2020-11-04 20:12:16
################################################################################

library(jsonlite)
library(urltools)

workerID <- Sys.getenv("WORKER_ID")
credentials <- NULL
lastUpdateID <- NULL

# Service sum in module sum in folder rfolder
#' @post /services/rfolder/sum/sum
function(req) {
	rawJSON <- req$postBody
	listFromJSON <- fromJSON(rawJSON)
	bodyInput <- as.data.frame(listFromJSON)
	output <- sumX(bodyInput)
	return(output)
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
	if (updateID != lastUpdateID) {
		lastUpdateID <- updateID
		credentials <- listFromJSON[["credentials"]]
	}
	return(list("workerID" = workerID))
}
