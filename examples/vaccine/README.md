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

<img src="https://github.com/myrtam/CANNR/blob/master/examples/images/launcher1.png" alt="Launcher" width="80%" height="80%"/>

![Title Screen](https://github.com/myrtam/CANNR/blob/master/examples/images/webtitle1.png)

Once you have gotten to the CannR Projects page, create a new project:

![New Project](https://github.com/myrtam/CANNR/blob/master/examples/images/newproject1.png)

Enter the name of the project (vaccine), and optionally a title and description:

![New Project](https://github.com/myrtam/CANNR/blob/master/examples/images/projectproperties1.png)

