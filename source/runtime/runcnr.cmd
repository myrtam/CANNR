ECHO OFF
rem CANNR TM analytics container building tool command line script for the
rem Windows command shell.
rem Copyright 2020 Pat Tendick ptendick@gmail.com
rem All rights reserved
rem Maintainer Pat Tendick ptendick@gmail.com

rem You need to install the stdlib_list package to use this tool.
rem E.g. pip3 install stdlib_list
rem To run the tool, change to the source\runtime directory and then run this
rem file with the path of the project file as an argument, e.g.,
rem runcnr.cmd ..\..\examples\project1\project.json

set PYTHONPATH=..\base_image\cannr\lib
python runcnr.py %1 context.json
ECHO ON
