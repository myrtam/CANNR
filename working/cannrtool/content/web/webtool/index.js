/*
CANNR TM analytics container building tool main page Javascript functions.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
 */

// Selected project name
var selectedProjectName = null;

// Global variables for HTML DOM elements
var projectSelectLabel = null;
var projectSelectGroup = null;
var projectSelect = null;
var goProjectButton = null;

// Initialize DOM object variables
function initDOMObjects() {

	projectSelectLabel = document.getElementById('projectSelectLabel');
	projectSelectGroup = document.getElementById('projectSelectGroup');
	projectSelect = document.getElementById('projectSelect');
	goProjectButton = document.getElementById('goProjectButton');

}

//Enable/disable the folder select and buttons.
function disableProjectSelect() {

	if (projectSelect.length) {
		projectSelect.disabled = false;
		disableButton(goProjectButton, false);
		disableButton(delProjectButton, false);
		projectSelectLabel.style.color = enabledTextColor;
	}
	else {
		projectSelect.disabled = true;
		disableButton(goProjectButton, true);
		disableButton(delProjectButton, true);
		projectSelectLabel.style.color = disabledTextColor;
	}

}

// Populate select list of projects
function getProjects() {

	// Get the project name query parameter
	var params = new URLSearchParams(window.location.search);	
	var projectName = params.get('projectname');

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
				deleteChildNodes(projectSelect);

				// Load the projects into the pick list.
				var keys = Object.keys(projects);
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
				
				setSelected(projectSelect, projectName);
				
			}
			else
				alert(response.errorMsg);
	
		} else {
			console.error(xhr.responseText);
			alert("Error retrieving session state");
		}

		disableProjectSelect();

	}

	// Send the request.
	xhr.send();
	
}


// Handle changes to the selection in the project pick list.
function onProjectSelectChange() {

	var selectedIndex = projectSelect.selectedIndex;

	if (selectedIndex)
		selectedProjectName = projectSelect[selectedIndex].value;

}


// Go to the project page for the selected project.
function onGoProject() {
	
	selectedProjectName = getSelected(projectSelect);

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


//Handler for delFolderButton.
function onDelProject() {

	projectName = getSelected(projectSelect);
	// If no folder selected, do nothing.
	if (!projectName)
		return;

	// Confirm delete
	if (!confirm('Delete project ' + projectName + '?  ' +
		'This will delete the project and any folders or files that have been uploaded.')) 
		return;

	// Prepare the XHR request.
	var request = {"projectName": projectName};
	var xhr = new XMLHttpRequest();
	xhr.open("POST", baseURL + "deleteproject");
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var succeeded = response.succeeded;
			if (succeeded) {

				alert('Project deleted.');

				// Remove the project from the pick list
				delSelected(projectSelect);
				
				disableProjectSelect();

			}
			else
				alert(response.errorMsg);
	
		} else {
			alert("Error deleting project.");
		}

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);

}


