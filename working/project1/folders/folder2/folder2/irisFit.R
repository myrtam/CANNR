
# Fit a model to iris data, specifically predict petal length from sepal length
# for virginica species.

library(tidyverse)

# Set the working directory
setwd('/Users/ptendick/open-source-workspace/MyRTAM Project Example 1/project1/folder2/home')

# Subset virginica
irisData <- as_tibble(subset(iris, Species == 'virginica'))

# Rename Sepal.Length and Petal.Length to x and y for simplicity since we will be
# passing in x as a URL query parameter.
irisData <- irisData %>% 
	rename(
		x = Sepal.Length,
		y = Petal.Length
	)

# Subset columns to be just x and y
irisData <- irisData[c('x','y')]

# Fit a straight line model
irisModel <- lm(y ~ x, data = irisData)

# Save the model
saveRDS(irisModel, 'models/irisModel.rds')
