This is the CANNR TM analytics container building tool for converting R and
Python code into microservices.  The CANNR tool takes functions in R and Python
source files and creates scalable containerized microservices that expose things
like models and calculations so that they may be easily consumed by software
applications.

NOTE:  THIS IS A PRE-RELEASE.  WATCH THIS PROJECT FOR UPCOMING RELEASES!

You need to have Docker and Python 3.7 or higher installed.  Also, you need to
install the stdlib_list package, using e.g.,

pip3 install stdlib_list

Future versions will probably run in a container and only require having Docker
installed.

To install the tool, clone the CANNR project or download and copy the
directories to your computer.

You will first need to build the CANNR base Docker image by changing to the
source/base_image directory and running the command

docker build -t cannr-base

Once you have built the base image, you can run the tool to create containerized
microservices from your R or Python code.

There is currently one example project in the directory examples/project1.
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

runcnr.cmd ..\..\examples\project1\winproject.json

Then navigate to the working\project1 or working/project1 directory, where you
will find a Docker project.  You can then use Docker to build the container
using, e.g.,

docker build -t project1 .

You should then be able to run the container using

docker run -d -p 80:80 project1

You should then be able to access some of the example services from a browser using

http://127.0.0.1/services/pyFolder/rand/rand

http://127.0.0.1/services/rFolder/iris/predPLengthSLength?x=6.5
