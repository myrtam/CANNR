This is the CANNR<sup>TM</sup> analytics container building tool for converting R and
Python code into microservices.  The CANNR tool takes functions in R and Python
source files and creates scalable containerized microservices that expose things
like models and calculations so that they may be easily consumed by software
applications.

NOTE:  THIS IS A PRE-RELEASE.  WATCH THIS PROJECT FOR UPCOMING RELEASES!

NEW!  Single executable available for the Mac.  Windows version coming soon!

Requirements
------------

You need to have Docker and Python 3.7 or higher installed.  Also, you need to
install the stdlib_list package, using e.g.

pip install stdlib_list 

Future versions will probably run in a container and only require having Docker
installed.

Single Executable for the Mac
-----------------------------
There is now a single executable version of the Web based tool available for the Mac.
To run it, you need to have at least 8 GB of memory and Docker installed.
To install the executable, just download the dmg file at

https://github.com/myrtam/CANNR/blob/master/source/launcher/OSX/CannR.dmg

Then open the dmg file and copy the executable into your Applications folder.
After that, the CannR Launcher should appear in Launchpad.
Before running the launcher, make sure that Docker desktop is running.
The first time you run the launcher, it will ask you to provide some information to set things up.
The default values should work fine for most people.
Then the launcher will start the Web UI.
Clicking the Launch button will launch the Web based tool in your default browser and close the launcher.
To shut down the Web UI, restart the launcher and click the Shut Down button.

Installation of the Command Line Tool
-------------------------------------

To install the tool, clone the CANNR project or download and copy the
directories to your computer.

You will first need to build the CANNR base Docker image by changing to the
source/base_image directory and running in a Windows command shell

docker build -t cannr-base .

For Powershell, use

.\docker build -t cannr-base .

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

docker run -d -p 80:80 --name project1 project1

You should then be able to access some of the example services from a browser using

http://127.0.0.1/services/pyfolder/rand/rand

http://127.0.0.1/services/rfolder/iris/predplengthslength?x=6.5

To stop the container, use the command

docker stop project1

To restart it, use the command

docker start project1

Web UI
------

To use the Web-based version of the CANNR tool, you must first build it.  To build the tool,
navigate to the working/cannr-web (or working\cannr-web on Windows) directory and use the command

docker build -t cannr-web .

On OSX, you can  start the tool by changing to the external directory and entering the command

docker run -d -p 8080:80 --name cannr-web --mount type=bind,source="$(pwd)",target=/external cannr-web

On Windows, use the command

docker run -d -p 8080:80 --name cannr-web --mount type=bind,source="%CD%",target=/external cannr-web

which runs the tool on port 8080.  To run the tool on a different port, replace 8080 in the above with
the port you want to use.  You should then be able to access the Web tool using the URL

http://localhost:8080/web/webtool/index.html

When you access this URL, you should see, among other things, a list of projects that contains the project1 project.
If you go to this project and then click the Build button, you will be prompted to build the project.  Once the project
has been built, you can find the built Docker project in the external/working/project1 folder.  To build the image
and run the container, follow the instructions for building and running project1 above.

To stop the tool, use the command

docker stop cannr-web

To restart it, use the command

docker start cannr-web
