This is the CANNR TM analytics container building tool for converting R and
Python code into microservices.  The CANNR tool takes functions in R and Python
source files and creates scalable containerized microservices that expose things
like models and calculations so that they may be easily consumed by software
applications.

NOTE:  THIS IS A PRE-RELEASE.  WATCH THIS PROJECT FOR UPCOMING RELEASES!

NEW!  Web Tool Available!  See Web UI below.

Requirements
------------

You need to have Docker and Python 3.7 or higher installed.  Also, you need to
install the stdlib_list package, using e.g.,

pip3 install stdlib_list

Future versions will probably run in a container and only require having Docker
installed.

Installation of the Command Line Tool
-------------------------------------

To install the tool, clone the CANNR project or download and copy the
directories to your computer.

You will first need to build the CANNR base Docker image by changing to the
source/base_image directory and running the command

docker build -t cannr-base

Once you have built the base image, you can run the tool to create containerized
microservices from your R or Python code.

If you have R code, it must be compatible with R 4.0.  If you have Python code,
it needs to be compatible with Python 3.8.

Example
-------

There is an example project in the directory examples/project1.
The example consists of two Python scripts and two R scripts.  The Python
scripts are in subdirectory folder1 and the R scripts are in folder2.
Each script contains one function to be exposed as a service.  The scripts
sum.py and sum.R perform a simple sum of numbers.  The script rand.py returns
a random number.  The script iris.R returns the result of applying a regression
based on Fisher's iris data to a new x value.  An additional script, irisFit.R,
fits the model exposed by iris.R.  Please see the scripts for more details.
The project1 directory also contains files that specify how the project should
be built.  project.json is the project file for OSX, whereas winproject.json
is the project file for Windows.

THIS INITIAL RELEASE DOES NOT ALLOW FOR SPACES IN FILE OR DIRECTORY NAMES!

To run the example on OSX, navigate to the source/runtime directory, then run
the command

./runcnr.sh ../../examples/project1/project.json

To run the example from Windows, navigate to the source\runtime directory,
then run the command

runcnr.cmd ..\\..\examples\project1\winproject.json

Then navigate to the working\project1 or working/project1 directory, where you
will find a Docker project.  You can then use Docker to build the container
using, e.g.,

docker build -t project1 .

You should then be able to run the container using

docker run -d -p 80:80 project1

You should then be able to access some of the example services from a browser using

http://127.0.0.1/services/pyfolder/rand/rand

http://127.0.0.1/services/rfolder/iris/predplengthslength?x=6.5


Web UI
------

To use the Web-based version of the CANNR tool, you must first build it.  To build the tool,
navigate to the working directory and use the command

docker build -t cannrtool .

You can then start the tool by changing to the external directory and entering the command

docker run -d -p 8080:80 --name cannrtool --mount type=bind,source="$(pwd)",target=/external cannrtool

which runs the tool on port 8080.  To run the tool on a different port, replace 8080 in the above with
the port you want to use.  You should then be able to access the Web tool using the URL

http://localhost:8080/web/webtool/index.html

When you access this URL, you should see, among other things, a list of projects that contains the project1 project.
If you go to this project and then click the Build button, you will be prompted to build the project.  Once the project
has been built, you can find the built Docker project in the external/working/project1 folder.  To build the image
and run the container, follow the instructions for building and running project1 above.
