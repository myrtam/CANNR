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

