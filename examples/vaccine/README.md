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

To use the tutorial, you first need to have the CannR Web tool installed.
Please see https://github.com/myrtam/CANNR for instructions.

To run the tutorial, you need to download the example directory, which may be found at
https://github.com/myrtam/CANNR/tree/master/examples/vaccine

To download the example directory, you can clone the project, download the zipped project, or just enter
the URL into DownGit (https://downgit.github.io).

Once you have the example directory copied to your local machine, you can launch the CannR Web tool
if you have not already done so.
You can do this using the CannR Launcher:

<img src="https://github.com/myrtam/CANNR/blob/master/examples/images/launcher1.png" alt="Launcher" width="50%" height="50%"/>

![Title Screen](https://github.com/myrtam/CANNR/blob/master/examples/images/webtitle1.png)

Once you have gotten to the CannR Projects page, create a new project:

![New Project](https://github.com/myrtam/CANNR/blob/master/examples/images/newproject1.png)

Enter the name of the project (vaccine), and optionally a title and description:

![New Project](https://github.com/myrtam/CANNR/blob/master/examples/images/projectproperties1.png)

![Project Created](https://github.com/myrtam/CANNR/blob/master/examples/images/projectcreated.png)

Next, you can create a folder.
Folders contain code or content to be included in your container.
First, we will create a folder containing the Python module that contains the models and decision logic
used in the Vaccine app.
A code folder can contain one or more modules, plus other files and subdirectories containing
data and supporting modules.
You must specify a language for a code folder, either R or Python.
We will call the folder "decisions", because the app will be calling services in the folder
to provide decisions about whether someone gets the vaccine.

![Folder Properties](https://github.com/myrtam/CANNR/blob/master/examples/images/folder1.png)

Click the "Choose File" button to specify the location of the source folder, then navigate to the decisions
folder and select it, then click Upload:

![Folder Properties](https://github.com/myrtam/CANNR/blob/master/examples/images/upload1.png)

