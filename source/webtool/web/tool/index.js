/*
CANNR TM analytics container building tool main page Javascript functions.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
 */

// Selected project name
var selectedProjectName = null;

// Populate select list of projects
function getProjects() {

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.withCredentials = true;
	var date = new Date();
	xhr.open("GET", baseURL + "getprojects" + "?timestamp=" + date.getTime());

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var succeeded = response.succeeded;
			if (succeeded) {

				// If success, get the projects collection.
				var projects = response['projects'];
				var projectSelect = document.getElementById('projectSelect');
				deleteChildNodes(projectSelect);

				// Load the projects into the pick list.
				var keys = Object.keys(projects);
				if (keys.length == 0) {
					projectSelect.style.visibility = 'hidden';
					document.getElementById('goButton').style.visibility = 'hidden';
				}
				else {
					projectSelect.style.visibility = 'visible';
					document.getElementById('goButton').style.visibility = 'visible';
					keys.forEach( function (key, index) {
	
						// Create a new pick list item and add the project to it.
						var option = document.createElement('option');
						projectSelect.appendChild(option);
						project = projects[key];
						label = key
						if (project['projectTitle'])
							label = label + ' - ' + project['projectTitle'];
						option.innerHTML = label;
						option.setAttribute('value', key);
	
						// If only one project, select it by default.
						if (keys.length==1) {
							selectedProjectName = key;
							option.selected = true;
						}
						
					});
				}

			}
			else
				alert(response.errorMsg);
	
		} else {
			console.error(xhr.responseText);
			alert("Error retrieving session state");
		}

	}

	// Send the request.
	xhr.send();
	
}


// Handle changes to the selection in the project pick list.
function onProjectSelectChange() {

	var projectSelect = document.getElementById('projectSelect');
	var selectedIndex = projectSelect.selectedIndex;

	if (selectedIndex)
		selectedProjectName = projectSelect[selectedIndex].value;

}


// Go to the project page for the selected project.
function go() {

	if (!selectedProjectName)
		alert('No project selected');
	else
		window.location.assign("project.html?projectname=" + selectedProjectName + "&timestamp=" + Date.now());	
	
}


// Handle add project events.
function addProject() {

	window.location.assign("project.html?timestamp=" + Date.now());
	
}


// Handle edit configuration events.
function configure() {

	
}

