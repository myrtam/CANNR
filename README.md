This is the CANNR TM analytics container building tool for converting R and
Python code into microservices.  The CANNR tool takes functions in R and Python
source files and creates scalable containerized microservices that expose things
like models and calculations so that they may be easily consumed by software
applications.

You need to have Docker and Python 3.7 or higher installed.  Also, you need to
install the stdlib_list package, using e.g.,

pip3 install stdlib_list

Future versions will probably run in a container and only require having Docker
installed.

To install the tool, clone the CANNR project or download and copy the
directories to your computer.

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
