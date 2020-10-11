# CANNR TM analytics container building tool command line script for bash.
# Copyright 2020 Pat Tendick ptendick@gmail.com
# All rights reserved
# Maintainer Pat Tendick ptendick@gmail.com

# You have Python 3.7 or higher and the stdlib_list package installed to use this tool.
# To install stdlib_list, use e.g.
# pip3 install stdlib_list
# To run the tool, change to the source/runtime directory and then run this
# file with the path of the project file as an argument, e.g.,
# ./runcnr.sh ../../examples/project1/project.json

export PYTHONPATH=$PYTHONPATH:../base_image/cannr/lib

# Warning that directories will be overwritten/deleted
echo "The directory"
python3 checkdel.py $1 context.json
echo "and its descendants will be deleted or overwritten!"
read -p "Proceed(Y/n)? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Y]$ ]]
then
	# Run build script
	python3 runcnr.py $1 context.json
fi
