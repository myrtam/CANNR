
# CANNR TM tool example showing R function to expose as a Web service.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

# Sum the values of the variable x in a data frame.
sumX <- function(df) {
  
  return(sum(df$x))
  
}

# Sample JSON input is
# [{"x":1},{"x":2},{"x":3}]