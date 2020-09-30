
rem Command script to run the CANNR TM containerizer tool

rem You need to install the stdlib_list package to use this tool.
rem E.g. pip3 install stdlib_list
rem To run the tool, change to the source\runtime directory and then run this
rem file with the path of the project file as an argument, e.g.,
rem runcnr.cmd ..\..\examples\project1\project.json
rem to run the example.

set PYTHONPATH=..\base_image\cannr\lib
python runcnr.py %1 context.json
