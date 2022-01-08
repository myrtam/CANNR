Vaccine Example Tutorial
------------------------

This tutorial uses a simple Web app to illustrate the use of the CannR tool.
The example involves a hypothetical scenario in which a vaccine is being offered to the public
to control a viral pandemic.

The app schedules people for the vaccine by collecting their information and then calling
a REST service exposed by the CannR tool to decide whether someone can be scheduled to receive the
vaccine immediately or should be placed on a waiting list.
The REST service exposes models of mortality and life expectancy provided as simple Python functions.
The models in this example are strictly hypothetical.

To use the tutorial, you first need to have the [CannR Web Tool](https://github.com/myrtam/CANNR/) installed.
To run the tutorial, you need to download the 
[example directory](https://github.com/myrtam/CANNR/tree/master/examples/vaccine).
To download the example directory, you can clone the project, download the zipped project, or just enter
the following URL into [DownGit](https://downgit.github.io):

https://github.com/myrtam/CANNR/tree/master/examples/vaccine

Once you have the example directory copied to your local machine, you can launch the CannR Web tool
if you have not already done so.
You can do this using the CannR Tool Launcher:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/launcher1.png" alt="Launcher" width="50%" height="50%"/></kbd>

which will start the tool in your default browser:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/webtitle1.png" alt="Title Screen"/></kbd>

Once you reach the CannR Projects page, create a new project:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/newproject1.png" alt="New Project"/></kbd>

Enter the name of the project (vaccine), and optionally a title and description.

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/projectproperties1.png" alt="Project Properties" width="60%" height="60%"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/projectcreated.png" alt="Project Created"/></kbd>

Next, we will create a <i>folder</i>.
Folders contain code or content to be included in your container.
First, we will create a folder containing the Python file that contains the models and decision logic
used in the Vaccine app.
We will call the folder "decisions", because the app will be calling services in the folder
to provide decisions about whether someone gets the vaccine.
When creating folders and other items in this tutorial, be sure to use the exact names
specified, or else the example will not work correctly.

Also, we will upload the source folder containing the Python code by clicking the Choose File button:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/folder1.png" alt="Folder Properties" width="60%" height="60%"/></kbd>

Navigate to the vaccine folder on your local computer and select the decisions subfolder:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/upload1.png" alt="Folder Upload"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/upload1a.png" alt="Folder Upload"/></kbd>

We also need to specify what type of folder this is, either code or content.
A code folder can contain one or more files containing the code you want to expose
as services or <i>modules</i>, plus other files and subdirectories containing
data and supporting modules.
You must specify a language for a code folder, either R or Python.
Click Next to create the folder, then we will create a module:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/folder2.png" alt="Creating the Folder" width="60%" height="60%"/></kbd>

Our folder contains one module,
[vaccine.py](https://github.com/myrtam/CANNR/blob/master/examples/vaccine/decisions/vaccine.py).
Enter vaccine as the module name, and optionally a title and description.

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/module1.png" alt="Module Properties" width="60%" height="60%"/></kbd>

Next, we will create a <i>service</i> within the module.
Services describe the microservices we want to provide in the container.
The first service we will create will return a sample input to be used with the real
service we want to call, which will be specified later.
The sample input contains data for a hypothetical user.
Creating a sample input function like this can be very useful when testing a POST service that requires
us to send JSON input.
Name the service sampleinput and enter an optional title and description.
Then select the function sampleInput from the drop down list.
Also, we need to specify that this service is used with HTTP GET requests:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/service1.png" alt="Service Properties" width="60%" height="60%"/></kbd>

Now we're ready to build and run a basic container and service.
Make sure that both "Build image" and "Start container on localhost" are checked, then
click Build:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/build1.png" alt="Build Screen" width="60%" height="60%"/></kbd>

Then copy the URL for the sampleinput service from the Build screen:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/build2.png" alt="Copy URL" width="60%" height="60%"/></kbd>

Open a new browser window or tab and paste the URL into the address bar, but replace &lt;domain or ip&gt; with localhost:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/sampleinput1.png" alt="Sample Input"/></kbd>

You have now verified that the sampleinput service works, and have also obtained a sample input
for the second service you will be creating, vaxdecision.
Next, we need to create and test the vaxdecision service and add the Web page for the app.
First, stop the container that is currently running by clicking the Stop button,
then click Finish to return to the main Project page:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/build3.png" alt="Stop Container & Finish" width="60%" height="60%"/></kbd>

Go back to the decisions folder:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/project1.png" alt="Project Screen"/></kbd>

Then go back to the vaccine module:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/folder3.png" alt="Decisions Folder" width="60%" height="60%"/></kbd>

Create a new service called vaxdecision:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/module2.png" alt="Vaccine Module" width="60%" height="60%"/></kbd>

Specify vaxDecision as the function, POST as the HTTP method, and that the request body will be included: 

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/vaxdecision1.png" alt="vaxdecision Service" width="50%" height="50%"/></kbd>

Note that the Service Properties screen tells us that the function argument(s) should be the HTTP request body.
This is just the data we will be sending in POST requests to the service.
By default, the CannR Tool will convert the JSON input into a Python list or dictionary depending on its content,
and convert the output back into JSON according to the default JSON conversion performed by Python.

Finally, let's create a folder containing the Web page for the app.

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/project2.png" alt="New Folder"/></kbd>

Name the folder web and select Content as the folder type.
(You don't have to specify a language for a content folder.)

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/folder4.png" alt="Web Folder" width="60%" height="60%"/></kbd>

Click the Choose File button to specify the source folder, then navigate to the vaccine folder and select the web subfolder:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/upload2.png" alt="Directory"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/upload2a.png" alt="Upload"/></kbd>

Save the new folder and return to the main project screen:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/folder6.png" alt="Save Folder" width="60%" height="60%"/></kbd>

Now we can build the container, including the Web page:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/project3.png" alt="Build Project"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/build5.png" alt="Build Screen" width="60%" height="80%"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/build6.png" alt="Build Screen" width="60%" height="60%"/></kbd>

Now that the full container is running, we can test the vaxdecision service, which is the main microservice exposed by the container.
To do this, we can use the [Postman API Client](https://www.postman.com/product/api-client/),
which can be used to send REST service requests and check the responses.
If you use Postman, create a new POST request, add the URL for the vaxdecision service from the Build screen
but with &lt;domain or ip&gt; replaced by localhost, and paste the sample input from the sampleinput service
into the request body:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/postman1.png" alt="Postman Request"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/postman2.png" alt="Postman Response"/></kbd>

We can now see that the sample input produces a <b>true</b> response from the vaxdecision service.
Next, we can try running the app using the URL for the web folder.
Note that because the page for the app is named index.html, we don't need to include the page name
in the URL.
For any other page, we would need to add the page to the end of the URL.

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/vaxapp1.png" alt="Vaccine App Title" width="60%" height="60%"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/vaxapp2.png" alt="Vaccine App Input" width="60%" height="60%"/></kbd>

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/vaxapp3.png" alt="Vaccine App Response" width="60%" height="60%"/></kbd>

Finally, we can stop the app container from the Build screen as before, exit the build screen, exit the project,
and shut down the CannR Web Tool:

<kbd><img src="https://github.com/myrtam/CANNR/blob/master/examples/images/shutdown1.png" alt="Shutting Down" width="50%" height="50%"/></kbd>





