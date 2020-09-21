
# Sum the values of the variable x in a data frame.
sumX <- function(df) {
  
  return(sum(df$x))
  
}

# Sample JSON input is
# [{"x":1},{"x":2},{"x":3}]

################################################################################
# Copyright/license notice for the project
# Generated 2020-09-20 20:19:51
################################################################################

library(urltools)

workerID <- Sys.getenv("WORKER_ID")
credentials <- NULL
lastUpdateID <- NULL

# Service sum in module sum in folder folder2
#' @post /services/folder2/sum/sum
function(req) {
	rawJSON <- req$postBody
	listFromJSON <- fromJSON(rawJSON)
	bodyInput <- as.data.frame(listFromJSON)
	if (nrow(bodyInput) > 1000) {
		return(data.frame(error = "Capacity exceeded"))
	}
	output <- sumX(bodyInput)
	return(output)
}

# Refresh objects in module sum
#' @post /refreshObjects/folder2/sum
function(req) {
	# TODO:  STUB
	return
}

# Update credentials in module sum
#' @post /updateCredentials/folder2/sum
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
