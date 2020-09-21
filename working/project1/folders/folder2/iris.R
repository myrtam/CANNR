
# Return the predicted petal length from sepal length for virginica species
# of irises.

# Load the model
irisModel <- readRDS('models/irisModel.rds')

# Function to predict petal length from sepal length
predPLengthSLength <- function(new) {

	# Convert input to numeric
	new$x <- as.double(new$x)

	# Find the predicted petal length
	predicted <- predict(irisModel, new, se.fit = TRUE)

	# Return the prediction merged with the input
	return(merge(new, predicted))

}



################################################################################
# Copyright/license notice for the project
# Generated 2020-09-20 20:19:51
################################################################################

library(urltools)

workerID <- Sys.getenv("WORKER_ID")
credentials <- NULL
lastUpdateID <- NULL

# Service predPLengthSLength in module iris in folder folder2
#' @get /services/folder2/iris/predPLengthSLength
function(req) {
	queryParams <- param_get(paste0("http://x.com/x", req$QUERY_STRING))
	output <- predPLengthSLength(queryParams)
	return(output)
}

# Refresh objects in module iris
#' @post /refreshObjects/folder2/iris
function(req) {
	# TODO:  STUB
	return
}

# Update credentials in module iris
#' @post /updateCredentials/folder2/iris
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
