# CANNR TM analytics container building tool script that runs R services.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

# Usage:
# $ Rscript --vanilla runApp.R <module path> <port> <worker ID> &
# Example:
# $ Rscript --vanilla runApp.R /folders/folder2/sum.R 5005 3 &

library(plumber)

# Retrieve command line args (module path and port)
args = commandArgs(trailingOnly=TRUE)

# Save the worker number to an environment variable
Sys.setenv(WORKER_ID = args[3])

# Plumb the file
pr <- plumber::plumb(args[1])

# Run
pr$run(host='0.0.0.0', port=strtoi(args[2]))
