/*
CANNR TM analytics container building tool project page Javascript functions.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
 */

// Global variables related to the current project
var selectedFolderName = null;
var project = null;
var folder = null;
var module = null;
var service = null;
var folderName = null;
var moduleName = null;
var serviceName = null;
var newProject = true;
var language = null;

// Flag indicating whether current screen has been changed
var changed = false;

// All of the modals.
var modals = ['projectPropertiesModal', 'folderPropertiesModal', 'modulePropertiesModal',
	'servicePropertiesModal', 'projectBuildModal'];

// Global variables for HTML DOM elements
var fileSelect = null;
var fileSelectRules = null;
var folderBack = null;
var folderNameInput = null;
var folderNext = null;
var folderSelectGroup = null;
var folderSelect = null;
var folderSelectLabel = null;
var functionSelect = null;
var functionSelectRules = null;
var goFolderButton = null;
var goModuleButton = null;
var goServiceButton = null;
var includeBodyInput = null;
var includeParamsInput = null;
var includeRequestInput = null;
var inputParseTypeInput = null;
var languageP = null;
var languageR = null;
var methodGETInput = null;
var methodPOSTInput = null;
var moduleBack = null;
var moduleDescriptionInput = null;
var moduleNameInput = null;
var moduleNameRules = null;
var moduleNext = null;
var moduleSelect = null;
var modulesRow = null;
var moduleTitleInput = null;
var newModule = null;
var newModulesRow = null;
var newService = null;
var newServicesRow = null;
var outputParseTypeInput = null;
var packageAddButton = null;
var packageDelButton = null;
var packageInput = null;
var packageSelect = null;
var paramsToDFInput = null;
var pathAddButton = null;
var pathDelButton = null;
var pathInput = null;
var pathSelect = null;
var projectBack = null;
var projectDescriptionInput = null;
var projectNameInput = null;
var projectNext = null;
var projectPageTitle = null;
var projectPropertiesTitle = null;
var projectTitleInput = null;
var serviceBack = null;
var serviceDescriptionInput = null;
var serviceNameInput = null;
var serviceNameRules = null;
var serviceNext = null;
var servicePropertiesTitle = null;
var serviceSelect = null;
var servicesRow = null;
var serviceTitleInput = null;
var sourcePathInput = null;
var	sourceUpload = null;
var titleFolderPath = null;
var titleServicePath = null;
var uploadRequired = null;
var workersInput = null;

// Initialize DOM object variables
function initDOMObjects() {

	fileSelect = document.getElementById('fileSelect');
	fileSelectRules = document.getElementById('fileSelectRules');
	folderBack = document.getElementById('folderBack');
	folderNameInput = document.getElementById('folderNameInput');
	folderNext = document.getElementById('folderNext');
	folderSelect = document.getElementById('folderSelect');
	folderSelectGroup = document.getElementById('folderSelectGroup');
	folderSelectLabel = document.getElementById('folderSelectLabel');
	functionSelect = document.getElementById('functionSelect');
	functionSelectRules = document.getElementById('functionSelectRules');
	goFolderButton = document.getElementById('goFolderButton');
	goModuleButton = document.getElementById('goModuleButton');
	goServiceButton = document.getElementById('goServiceButton');
	includeBodyInput = document.getElementById('includeBodyInput');
	includeParamsInput = document.getElementById('includeParamsInput');
	includeRequestInput = document.getElementById('includeRequestInput');
	inputParseTypeInput = document.getElementById('inputParseTypeInput');
	languageP = document.getElementById('languageP');
	languageR = document.getElementById('languageR');
	methodGETInput = document.getElementById('methodGETInput');
	methodPOSTInput = document.getElementById('methodPOSTInput');
	moduleBack = document.getElementById('moduleBack');
	moduleDescriptionInput = document.getElementById('moduleDescriptionInput');
	moduleNameInput = document.getElementById('moduleNameInput');
	moduleNameRules = document.getElementById('moduleNameRules');
	moduleNext = document.getElementById('moduleNext');
	moduleSelect = document.getElementById('moduleSelect');
	modulesRow = document.getElementById('modulesRow');
	moduleTitleInput = document.getElementById('moduleTitleInput');
	newModule = document.getElementById('newModule');
	newModulesRow = document.getElementById('newModulesRow');
	newService = document.getElementById('newService');
	newServicesRow = document.getElementById('newServicesRow');
	outputParseTypeInput = document.getElementById('outputParseTypeInput');
	packageAddButton = document.getElementById('packageAddButton');
	packageDelButton = document.getElementById('packageDelButton');
	packageInput = document.getElementById('packageInput');
	packageSelect = document.getElementById('packageSelect');
	paramsToDFInput = document.getElementById('paramsToDFInput');
	pathAddButton = document.getElementById('pathAddButton');
	pathDelButton = document.getElementById('pathDelButton');
	pathInput = document.getElementById('pathInput');
	pathSelect = document.getElementById('pathSelect');
	projectBack = document.getElementById('projectBack');
	projectDescriptionInput = document.getElementById('projectDescriptionInput');
	projectNameInput = document.getElementById('projectNameInput');
	projectNext = document.getElementById('projectNext');
	projectPageTitle = document.getElementById('projectPageTitle');
	projectPropertiesTitle = document.getElementById('projectPropertiesTitle');
	projectTitleInput = document.getElementById('projectTitleInput');
	serviceBack = document.getElementById('serviceBack');
	serviceDescriptionInput = document.getElementById('serviceDescriptionInput');
	serviceNameInput = document.getElementById('serviceNameInput');
	serviceNameRules = document.getElementById('serviceNameRules');
	serviceNext = document.getElementById('serviceNext');
	servicePropertiesTitle = document.getElementById('servicePropertiesTitle');
	serviceSelect = document.getElementById('serviceSelect');
	servicesRow = document.getElementById('servicesRow');
	serviceTitleInput = document.getElementById('serviceTitleInput');
	sourcePathInput = document.getElementById('sourcePathInput');
	sourceUpload = document.getElementById('sourceUpload');
	titleFolderPath = document.getElementById('titleFolderPath');
	titleServicePath = document.getElementById('titleServicePath');
	uploadRequired = document.getElementById('uploadRequired');
	workersInput = document.getElementById('workersInput');

	// Set input event handlers
	projectDescriptionInput.addEventListener('input', projectInput);
	projectNameInput.addEventListener('input', projectInput);
	projectTitleInput.addEventListener('input', projectInput);
	folderNameInput.addEventListener('input', folderInput);
	languageP.addEventListener('input', folderInput);
	languageR.addEventListener('input', folderInput);
	workersInput.addEventListener('input', folderInput);
	fileSelect.addEventListener('input', moduleInput);
	fileSelectRules.addEventListener('input', moduleInput);
	moduleDescriptionInput.addEventListener('input', moduleInput);
	moduleNameInput.addEventListener('input', moduleInput);
	moduleNameRules.addEventListener('input', moduleInput);
	moduleTitleInput.addEventListener('input', moduleInput);

	packageInput.addEventListener('input', onPackageInput);
	pathInput.addEventListener('input', onPathInput);

	functionSelect.addEventListener('input', serviceInput);
	functionSelectRules.addEventListener('input', serviceInput);
	includeBodyInput.addEventListener('input', serviceInput);
	includeParamsInput.addEventListener('input', serviceInput);
	includeRequestInput.addEventListener('input', serviceInput);
	inputParseTypeInput.addEventListener('input', serviceInput);
	methodGETInput.addEventListener('input', serviceInput);
	methodPOSTInput.addEventListener('input', serviceInput);
	outputParseTypeInput.addEventListener('input', serviceInput);
	paramsToDFInput.addEventListener('input', serviceInput);
	serviceDescriptionInput.addEventListener('input', serviceInput);
	serviceNameInput.addEventListener('input', serviceInput);
	serviceNameRules.addEventListener('input', serviceInput);
	serviceTitleInput.addEventListener('input', serviceInput);

}

//Display project properties.
function onProjectProps() {

	// Disable and hide the next button.
	if (newProject)
		projectNext.innerHTML = 'Next';
	else
		projectNext.innerHTML = 'Save';

	// Populate the modal
	popProjectProps();

	// Display the modal
	switchModal('projectPropertiesModal');

}

// Switch modal
function switchModal(nextModalID) {

	// Hide all the modals.
	modals.forEach(function(modalID, index, array) {
		var modal = document.getElementById(modalID);
		if (modal)
			modal.style.display = 'none';
	});

	// No changes made in the next modal.
	changed = false;

	// Show the next modal, if any.
	if (nextModalID) {
		var modal = document.getElementById(nextModalID);
		if (modal)
			modal.style.display = 'block';
	}
	// Otherwise, if no modal reload page with project name.
	// That way, if project page gets reloaded, it will remember the project!
	else {
		var params = new URLSearchParams(window.location.search);
		if (!params.has('projectname')&&project&&project['projectName'])
			window.location.assign("project.html?projectname=" + project['projectName'] + "&timestamp=" + Date.now());
	}

}

// Return the current modal
function whichModal() {

	// Find the current modal ID.
	var currentModalID = null;
	modals.forEach(function(modalID, index, array) {
		var modal = document.getElementById(modalID);
		if (modal && modal.style.display != 'none')
			currentModalID = modalID
	});

	return currentModalID;
	
}

// Populates project properties screen
function popProjectProps() {

	// Populate project properties
	projectPageTitle.innerHTML = 'New Project';
	projectPropertiesTitle.innerHTML = 'Project Properties';
	projectNameInput.innerHTML = '';
	projectNameInput.disabled = false;
	projectTitleInput.value = '';
	projectDescriptionInput.value = '';

	// Disable the Save button
	disableButton(projectNext, true);
	
	// Check for valid project and name
	if (!project)
		return false;

	projectName = project['projectName'];
	if (!projectName)
		return false;

	// Populate project properties
	projectPageTitle.innerHTML = 'Project ' + projectName;
	projectPropertiesTitle.innerHTML = 'Project Properties';
	projectNameInput.innerHTML = projectName;
	projectNameInput.disabled = true;
	var projectTitle = project['projectTitle'];
	var projectDescription = project['projectDescription'];
	if (projectTitle)
		projectTitleInput.value = projectTitle;
	if (projectDescription)
		projectDescriptionInput.value = projectDescription;

	// Get the folders in the project.
	var folders = project['folders'];
	if (!folders) {
		folders = {}
		project['folders'] = folders
	}
		
	deleteChildNodes(folderSelect);

	// Load the folders into the pick list.
	var keys = Object.keys(folders);
	if (keys.length == 0) {
		folderSelectGroup.style.visibility = 'hidden';
		folderSelectLabel.style.visibility = 'hidden';
		goFolderButton.style.visibility = 'hidden';
		disableButton(goFolderButton, true);
	}
	else {
		keys.forEach(function(key, index) {

			// Create a new pick list item and add the folder to it.
			var option = document.createElement('option');
			folderSelect.appendChild(option);
			var label = key;
			var newFolder = folders[key];
			if (newFolder['folderTitle'])
				label += ' - ' + newFolder['folderTitle'];
			option.innerHTML = label;
			option.setAttribute('value', key);

			// If only one project, select it by default.
			if (keys.length==1) {
				selectedFolderName = key;
				option.selected = true;
			}
			
		});
		folderSelectGroup.style.visibility = 'visible';
		folderSelectLabel.style.visibility = 'visible';
		disableButton(goFolderButton, false);
		goFolderButton.style.visibility = 'visible';
	}

	return true;

}


//Populates project properties screen
function popFolderProps() {

	// Check for project.  If doesn't exist, that's an error.
	if (!project)
		return false;

	// Check for folders collection
	var folders = project['folders'];
	if (!folders) {
		folders = {};
		project['folders'] = folders;
	}

	// Initialize screen items
	titleFolderPath.innerHTML = '';
	folderNameInput.value = '';
	folderNameInput.disabled = false;
	folderNameRules.innerHTML = '&nbsp;*<br>' + nameRules;
	folderNameRules.style.color = 'Black';
	sourcePathInput.innerHTML = '';
	//sourceUpload.files = null;
	sourceUpload.value = '';
	uploadRequired.innerHTML = '&nbsp;*';
	workersInput.value = 2;
	deleteChildNodes(moduleSelect);
	modulesRow.style.visibility = 'hidden';
	disableButton(goModuleButton, true);
	changed = false;

	// Disable the Save button
	disableButton(folderNext, true);
	
	// If new project, hide module related buttons
	if (newProject) {
		newModulesRow.style.visibility = 'hidden';
		disableButton(newModule, true);
	}
	else {
		disableButton(newModule, false);
		newModulesRow.style.visibility = 'visible';
	}
	
	// If folder name doesn't exist, we're done
	if (folderName) {

		// If can't find folder, that's an error.
		var folder = folders[folderName]
		if (!folder)
			return false;
	
		// Set subtitle to /projectname/foldername
		titleFolderPath.innerHTML = '/' + projectName + '/' + folderName;

		// Populate the folder name
		folderNameInput.value = folderName;
		folderNameInput.disabled = true;

		// Set subtitle to /projectname/foldername
		var sourcePath = folder['sourcePath'];
		if (sourcePath) {
			sourcePathInput.innerHTML = sourcePath;
			uploadRequired.innerHTML = '';
		}
		else {
			sourcePathInput.innerHTML = '';
			uploadRequired.innerHTML = '&nbsp;*';
		}

		// Set programming language
		language = folder['language'];
		languageR.checked = false;
		languageP.checked = false;
		if (language) {
			if (language == 'R')
				languageR.checked = true;
			else
				languageP.checked = true;
		}

		// Handle workers
		var workers = folder['workers'];
		if (workers) {
			workersInput.value = workers;
		}

		// Handle modules
		var modules = folder['modules'];
		deleteChildNodes(moduleSelect);
		
		// Load the modules into the pick list.
		var keys = Object.keys(modules);
		if (keys.length == 0) {
			moduleSelect.style.visibility = "hidden";
			goModuleButton.style.visibility = 'hidden';
		}
		else
			keys.forEach( function (key, index) {

				// Create a new pick list item and add the project to it.
				var option = document.createElement('option');
				moduleSelect.appendChild(option);
				var module = modules[key];
				label = key
				if (module['moduleTitle'])
					key = key + ' - ' + module['moduleTitle'];
				option.innerHTML = label;
				option.setAttribute('value', key);

				// If only one project, select it by default.
				if (keys.length==1) {
					selectedModuleName = key;
					option.selected = true;
				}
				
			});
		
	}

	return true;
	
}


// Populate the module properties screen
function popModuleProps() {

	// Check for folders collection
	var folders = project['folders'];
	if (!folders||!folderName)
		return false;

	// Get the folder
	var folder = folders[folderName];
	if (!folder)
		return false;

	// Get the list of filenames
	var fileNames = folder['fileNames']
	if (!fileNames||fileNames.length==0)
		return false;

	// Get the modules collection
	var modules = folder['modules'];
	if (!modules) {
		modules = {};
		folder['modules'] = modules;
	}

	// Populate the Source File pulldown
	deleteChildNodes(fileSelect);
	for (var i=0; i<fileNames.length; i++) {

		// Create a new pick list item and add the file name to it.
		var option = document.createElement('option');
		fileSelect.appendChild(option);
		fileName = fileNames[i];
		option.innerHTML = fileName;
		option.setAttribute('value', fileName);
		
		// If only one file, select it by default.
		if (fileNames.length==1)
			option.selected = true;
		
	}

	// Prep the module name, title, and description inputs
	moduleNameInput.disabled = false;
	moduleNameRules.innerHTML = '&nbsp;*<br>' + nameRules;
	moduleNameRules.style.color = 'Black';
	moduleTitleInput.value = '';
	moduleDescriptionInput.value = '';

	// Initially list of services is hidden and button disabled
	servicesRow.style.visibility = 'hidden';
	disableButton(goServiceButton, true);

	// Prep the package input items
	deleteChildNodes(packageSelect);
	packageInput.value = '';
	packageAddButton.disabled = true;
	packageDelButton.disabled = true;

	// Prep the path input items
	deleteChildNodes(pathSelect);
	pathInput.value = '';
	pathAddButton.disabled = true;
	pathDelButton.disabled = true;

	changed = false;

	// Disable the Save button
	disableButton(moduleNext, true);

	// If new project, hide module related buttons
	if (newProject) {
		newServicesRow.style.visibility = 'hidden';
		disableButton(newService, true);
	}
	else {
		disableButton(newService, false);
		newServicesRow.style.visibility = 'visible';
	}

	// Populate module data if exists
	if (moduleName) {

		// If module can't be found, that's an error
		var module = modules[moduleName];
		if (!module)
			return false;

		// If module name exists, can't be changed
		moduleNameInput.value = moduleName;
		moduleNameInput.disabled = true;
		moduleNameRules.innerHTML = '';

		// Populate module title
		var moduleTitle = module['moduleTitle'];
		moduleTitle = moduleTitle? moduleTitle: '';
		moduleTitleInput.value = moduleTitle;

		// Populate module description
		var moduleDescription = module['moduleDescription'];
		moduleDescription = moduleDescription? moduleDescription: '';
		moduleDescriptionInput.value = moduleDescription;

		// Get services for the module
		var services = module['services'];
		if (!services) {
			services = {};
			module['services'] = services;
		}

		// Get the source file, if any, and set the select list to use it
		var sourceFile = module['sourceFile'];
		if (sourceFile&&(fileSelect.length > 1))
			setSelected(fileSelect, sourceFile);

		// Load the services into the pick list.
		deleteChildNodes(serviceSelect);
		var keys = Object.keys(services);
		// If there are existing services
		if (keys.length > 0) {

			// Enable and make visible
			disableButton(goServiceButton, false);
			servicesRow.style.visibility = 'visible';

			// Load the list
			keys.forEach( function (key, index) {

				// Create a new pick list item and add the project to it.
				var option = document.createElement('option');
				serviceSelect.appendChild(option);
				var service = services[key];
				label = key
				if (service['serviceTitle'])
					key = key + ' - ' + service['serviceTitle'];
				option.innerHTML = label;
				option.setAttribute('value', key);

				// If only one project, select it by default.
				if (keys.length==1) {
					selectedServiceName = key;
					option.selected = true;
				}
				
			});
		}

		// Add required packages
		// Make sure packages exist in the module
		var packages = module['packages'];
		if (!packages) {
			packages = {};
			module['packages'] = packages;
		}

		// Add the packages to the pick list
		for (var i=0; i<packages.length; i++) {

			// Create a new pick list item and add the file name to it.
			var option = document.createElement('option');
			packageSelect.appendChild(option);
			var packageName = packages[i];
			option.innerHTML = packageName;
			option.setAttribute('value', packageName);

			// If only one file, select it by default.
			if (packages.length==1) {
				option.selected = true;
				packageDelButton.disabled = false;
			}
			
		}

		// Enable the package delete button
		packageDelButton.disabled = !packageSelect.length;		

		// Add paths (Python only)
		var language = folder['language'];
		if (language=='Python') {

			// Make sure paths exist in the module
			var paths = module['paths'];
			if (!paths) {
				paths = {};
				module['paths'] = paths;
			}

			// Add paths to the pick list
			for (var i=0; i<paths.length; i++) {
	
				// Create a new pick list item and add the file name to it.
				var option = document.createElement('option');
				pathSelect.appendChild(option);
				var pathName = paths[i];
				option.innerHTML = pathName;
				option.setAttribute('value', pathName);
	
				// If only one file, select it by default.
				if (paths.length==1) {
					option.selected = true;
					pathDelButton.disabled = false;
				}
				
			}

			// Disable the path delete button
			pathDelButton.disabled = !pathSelect.length;

		}

	}

	return true;
	
}


//Populate the module properties screen
function popServiceProps() {

	// Check for folders collection
	var folders = project['folders'];
	if (!folders||!folderName)
		return false;

	// Get the folder
	var folder = folders[folderName];
	if (!folder)
		return false;

	// Check for services collection
	var modules = folder['modules'];
	if (!modules||!moduleName)
		return false;

	// Get the service
	var module = modules[moduleName];
	if (!module)
		return false;

	// Get the list of filenames
	var functionNames = module['functionNames']
	if (!functionNames||functionNames.length==0)
		return false;

	// Get the modules collection
	var services = module['services'];
	if (!services) {
		services = {};
		module['services'] = services;
	}

	// Populate the Function pulldown
	deleteChildNodes(functionSelect);
	for (var i=0; i<functionNames.length; i++) {

		// Create a new pick list item and add the file name to it.
		var option = document.createElement('option');
		functionSelect.appendChild(option);
		functionName = functionNames[i];
		option.innerHTML = functionName;
		option.setAttribute('value', functionName);

		//if (function_&&fileName==function_)
		//	option.selected = true;

		// If only one file, select it by default.
		if (functionNames.length==1)
			option.selected = true;
		
	}

	// Prep the module name, title, and description inputs
	serviceNameInput.disabled = false;
	serviceNameRules.innerHTML = '&nbsp;*<br>' + nameRules;
	serviceNameRules.style.color = 'Black';
	serviceTitleInput.value = '';
	serviceDescriptionInput.value = '';
	methodPOSTInput.checked = true;
	methodGETInput.checked = false;
	includeBodyInput.checked = true;
	includeParamsInput.checked = false;
	paramsToDFInput.checked = false;
	paramsToDFInput.disabled = true;
	includeRequestInput.checked = false;
	changed = false;

	// Disable the Save button
	disableButton(serviceNext, true);


	var option = null;
	deleteChildNodes(inputParseTypeInput);

	option = document.createElement('option');
	inputParseTypeInput.appendChild(option);
	if (language=='R') {
		option.innerHTML = 'R List';
		option.setAttribute('value', 'rlist');
	}
	else {
		option.innerHTML = 'Python Dictionary';
		option.setAttribute('value', 'dictionary');
	}

	option = document.createElement('option');
	inputParseTypeInput.appendChild(option);
	if (language=='R')
		option.innerHTML = 'R Data Frame';
	else
		option.innerHTML = 'Pandas DataFrame';
	option.setAttribute('value', 'dataframe');

	if (language=='Python') {
		option = document.createElement('option');
		inputParseTypeInput.appendChild(option);
		option.innerHTML = 'Python List';
		option.setAttribute('value', 'plist');
	}

	option = document.createElement('option');
	inputParseTypeInput.appendChild(option);
	if (language=='R') {
		option.innerHTML = 'Vector/Matrix';
		option.setAttribute('value', 'vector');
	}
	else {
		option.innerHTML = 'Numpy Array';
		option.setAttribute('value', 'nparray');
	}

	option = document.createElement('option');
	inputParseTypeInput.appendChild(option);
	option.innerHTML = "Do not parse";
	option.setAttribute('value', 'none');

	if (language=='R')
		setSelected(inputParseTypeInput, 'rlist');
	else
		setSelected(inputParseTypeInput, 'dictionary');

	deleteChildNodes(outputParseTypeInput);

	option = document.createElement('option');
	outputParseTypeInput.appendChild(option);
	if (language=='R') {
		option.innerHTML = 'R List';
		option.setAttribute('value', 'rlist');
	}
	else {
		option.innerHTML = 'Python Dictionary';
		option.setAttribute('value', 'dictionary');
	}

	option = document.createElement('option');
	outputParseTypeInput.appendChild(option);
	if (language=='R')
		option.innerHTML = 'R Data Frame';
	else
		option.innerHTML = 'Pandas DataFrame';
	option.setAttribute('value', 'dataframe');

	if (language=='Python') {
		option = document.createElement('option');
		outputParseTypeInput.appendChild(option);
		option.innerHTML = 'Python List';
		option.setAttribute('value', 'plist');
	}

	option = document.createElement('option');
	outputParseTypeInput.appendChild(option);
	if (language=='R') {
		option.innerHTML = 'Vector/Matrix';
		option.setAttribute('value', 'vector');
	}
	else {
		option.innerHTML = 'Numpy Array';
		option.setAttribute('value', 'nparray');
	}

	option = document.createElement('option');
	outputParseTypeInput.appendChild(option);
	option.innerHTML = "Do not parse";
	option.setAttribute('value', 'none');

	if (language=='R')
		setSelected(outputParseTypeInput, 'rlist');
	else
		setSelected(outputParseTypeInput, 'dictionary');

	// Populate module data if exists
	if (serviceName) {

		// If module can't be found, that's an error
		var service = services[serviceName];
		if (!service)
			return false;

		// If service name exists, can't be changed
		serviceNameInput.value = serviceName;
		serviceNameInput.disabled = true;
		serviceNameRules.innerHTML = '';

		// Populate service title
		var serviceTitle = service['serviceTitle'];
		serviceTitle = serviceTitle? serviceTitle: '';
		serviceTitleInput.value = serviceTitle;

		// Populate service description
		var serviceDescription = service['serviceDescription'];
		serviceDescription = serviceDescription? serviceDescription: '';
		serviceDescriptionInput.value = serviceDescription;

		var function_ = service['function'];
		if (function_&&(functionSelect.length > 1))
			setSelected(functionSelect, function_);

		method = service['method']
		if (method=='GET') {
			methodPOSTInput.checked = false;
			methodGETInput.checked = true;
		}

		includeBody = service['includeBody'];
		includeParams = service['includeParams'];
		paramsToDF = service['paramsToDF'];
		includeRequest = service['includeRequest'];
		inputParseType = service['inputParseType'];
		outputParseType = service['outputParseType'];
		includeBodyInput.checked = includeBody? true: false;
		includeParamsInput.checked = includeParams? true: false;
		paramsToDFInput.checked = paramsToDF? true: false;
		includeRequestInput.checked = includeRequest? true: false;
		setSelected(inputParseTypeInput, inputParseType);
		setSelected(outputParseTypeInput, outputParseType);

		checkServiceProperties();
		
	}

	return true;
	
}


// Handle the results from backend project operations.
function handleResponse(response, nextModalID) {

	// Get the project.
	project = response['project'];

	// If no modal and the current project exists, not a new project.
	if (!nextModalID && project)
		newProject = false;

	// Populate project properties screen.
	if (!popProjectProps()) {
		alert('Error reading project');
		return;
	}

	if (nextModalID && nextModalID!='projectPropertiesModal') {

		// Populate folder properties screen.
		if (!popFolderProps()) {
			alert('Error reading folder');
			return;
		}
	
		if (nextModalID!='folderPropertiesModal') {

			// Populate the module properties screen.
			if (!popModuleProps()) {
				alert('Error reading module');
				return;
			}
		
			if (nextModalID!='modulePropertiesModal') {

				// Populate the service properties screen.
				if (!popServiceProps()) {
					alert('Error reading service');
					return;
				}

			}

		}

	}

	// Switch to the next modal.
	switchModal(nextModalID);

}

// Captures project properties and writes the modified document to the service.
function writeProject(project1, overwrite, cancel) {

	// Get the project name and check it.
	var projectName = projectNameInput.value;

	// Check the project name.
	if (!checkName(projectName)) {
		if (!cancel) {
			alert('Project name must consist of lower case letters, numbers, and underscores, and be no more than 30 characters.');
			return;
		}
		else if (newProject) {
			onExitProject();
			return;
		}
		else
			switchModal(null);
	}
	
	// Prepare the project to write to the service.
	var project2 = project1? JSON.parse(JSON.stringify(project1)): null;
	if (!project2) {
		project2 = {};
		project2['projectName'] = projectName;
	}
	project2['projectTitle'] = projectTitleInput.value;
	project2['projectDescription'] = projectDescriptionInput.value;
	if (!project2['folders'])
		project2['folders'] = {};
	
	// Check that the project has a name.  This should never happen.
	if (!project2['projectName']) {
		alert('Missing project name');
		return;
	}

	// Define the request, including the project.
	var request = {
			'project': project2,
			'overwrite': overwrite
		};

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	var date = new Date();
	xhr.open("POST", baseURL + "createproject?timestamp=" + date.getTime());
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var succeeded = response.succeeded;
			if (succeeded) {
				// If succeeded, identify the next screen and process the response.
				var nextModalID = newProject&&!cancel? 'folderPropertiesModal': null;
				// Populate project properties on the page
				handleResponse(response, nextModalID);
				// Notify that project created.
				if (newProject) {
					alert('Project created.');
					newProject = !cancel;
				}
			}
			else {
				// Otherwise, handle the error.
				var error = response['error']
				if (error)
					// If the project already exists and not cancelling, prompt whether to overwrite and try again.
					if  (error=='projectExists') {
						if (!cancel&&confirm("Project exists.  Overwrite?"))
							writeProject(project1, true, false);
					}
					else
						alert(response['errorMsg']);
				else
					alert('Error creating project');
					
			}

		} else {
			alert('Error creating project');
		}

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Display folder properties.
// folderName is the name of the folder, or null if a new folder.
function onFolderProps(folderName) {
	
	if (project) {
		
		var projectName = project['projectName'];
		folders = project['folders'];
		if (folders) {

			folder = project[folderName];
			if (folder && projectName && folderName) {
				
				// Set subtitle to /projectname/foldername
				titleFolderPath.innerHTML = '/' + projectName + '/' + folderName;

				folderNameInput.value = folderName;
				folderNameInput.disabled = true;

				// Set subtitle to /projectname/foldername
				var sourcePath = folder['sourcePath'];
				if (sourcePath) {
					sourcePathInput.innerHTML = sourcePath;
					uploadRequired.innerHTML = '';
				}
				else {
					sourcePathInput.innerHTML = '';
					uploadRequired.innerHTML = '&nbsp;*';
				}

				// Set programming language
				language = folder['language'];
				languageR.checked = false;
				languageP.checked = false;
				if (language) {
					if (language == 'R')
						languageR.checked = true;
					else
						languageP.checked = true;
				}

				var workers = folder['workers'];
				if (workers)
					workersInput.value = workers;

				var modules = folder['modules'];
				deleteChildNodes(moduleSelect);
				
				// Load the modules into the pick list.
				var keys = Object.keys(modules);
				if (keys.length == 0) {
					moduleSelect.style.visibility = "hidden";
					goModuleButton.style.visibility = 'hidden';
				}
				else
					keys.forEach( function (key, index) {
	
						// Create a new pick list item and add the project to it.
						var option = document.createElement('option');
						moduleSelect.appendChild(option);
						var module = modules[key];
						label = key
						if (module['moduleTitle'])
							key = key + ' - ' + module['moduleTitle'];
						option.innerHTML = label;
						option.setAttribute('value', key);
	
						// If only one project, select it by default.
						if (keys.length==1) {
							selectedModuleName = key;
							option.selected = true;
						}
						
					});
				
			}
			else {
				folderNameInput.disabled = false;
			}
		}

		// If new project, hide module related buttons
		if (newProject){
			document.getElementById('modulesLabel').style.visibility = 'hidden';
			moduleSelect.style.visibility = 'hidden';
			goModuleButton.style.visibility = 'hidden';
			newModule.style.visibility = 'hidden';
		}

		// Display the modal
		switchModal('folderPropertiesModal');

	}

}

// Keep new folder properties.
// nextModalID - ID of modal to which to navigate.
function onKeepFolderProps(nextModalID) {

	// Check if project exists
	if (!project)
		return false;

	// Check if folders exist
	var folders = project['folders'];
	if (!folders) {
		folders = {};
		project['folders'] = folders;
	}

	var failed = false;
	var edit = folderName? true: false;

	// Check if name populated, try to get the folder
	var folder = null;
	var newFolderName = null;
	if (!edit) {
		newFolderName = folderNameInput.value;
		if (!newFolderName||!checkName(newFolderName)) {
			failed = true;
			document.getElementById('folderNameRules').style.color = 'Red';
		}
		else
			document.getElementById('folderNameRules').style.color = 'Black';
		folder = folders[newFolderName];
	}
	else {
		folder = folders[folderName];
		if (!folder)
			return false;
	}

	// Check if source files have been specified or previously uploaded
	var files = sourceUpload.files;
	var sourcePath = sourcePathInput.innerHTML;

	// If no source path and list of filenames or files to be uploaded, stop.
	if (!edit&&!files || edit&&!sourcePath) {
		failed = true;
		uploadRequired.style.color = 'Red';
	}
	else
		uploadRequired.style.color = 'Black';

	// Check if language populated
	language = languageR.checked? 'R':
		languageP.checked? 'Python': null;
	if (!language) {
		failed = true;
		document.getElementById('languageRules').style.color = 'Red';
	}
	else
		document.getElementById('languageRules').style.color = 'Black';

	// Check if workers populated
	var workers = workersInput.value;
	if (!workers||workers < 1 || workers > 1024) {
		failed = true;
		document.getElementById('workerRules').style.color = 'Red';
	}
	else
		document.getElementById('workerRules').style.color = 'Black';

	// If data validation failure, don't do anything.
	if (failed)
		return false;

	// Check if OK to overwrite.
	if (!edit&&folder&&!confirm('Folder exists.  Overwrite?'))
		return;

	// Hide import paths if not Python
	// TODO:  HAVE SEPARATE EVENT HANDLER THAT CHANGES THIS WHEN LANGUAGE CHANGES
	if (language == 'Python')
		document.getElementById('importPathsRow').disabled = false;
	else
		document.getElementById('importPathsRow').disabled = true;

	// Create the folder if needed
	if (!edit&&newFolderName) {
		folderName = newFolderName;
		folder = {}
		folders[folderName] = folder;
	}		

	// Populate folder attributes
	folder['language'] = language;
	folder['sourcePath'] = sourcePath? sourcePath: null;
	folder['workers'] = workers;
	if (!folder['modules'])
		folder['modules'] = {};

	// Prepare the request doc
	var request = {'project': project};
	
	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.open("POST", baseURL + "updateproject");
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var succeeded = response.succeeded;
			if (succeeded) {

				// Get the updated project (should be the same)
				project = response['project']

				// If files to upload, upload them.
				if (files&&files.length>0) {

					// Populate the multipart form data.
					var formData = new FormData();
					for (var i = 0; i < files.length; i++)
				    	formData.append('files', files[i]);			
	
					// Prepare the request
					var xhr2 = new XMLHttpRequest();
					xhr2.open("POST", baseURL + "uploadfolder?projectname=" + projectName + '&foldername=' + folderName);
					xhr2.setRequestHeader('Content-type','application/octet-stream');
	
					// Define the callback function.
					xhr2.onload = function () {
	
						// Get the response, check HTTP status.
						if (xhr2.status == "200") {
	
							// Retrieve the response and check whether the request succeeded.
							var response = JSON.parse(xhr2.responseText);
							var succeeded = response.succeeded;
							if (succeeded) {
								// If succeeded, identify the next screen and process the response.
								//var nextModalID = newProject&&forward? 'modulePropertiesModal': 'projectPropertiesModal';
								// Populate project properties on the page
								handleResponse(response, nextModalID);
							}
	
						}
	
					}
					xhr2.send(formData);
	
				}
				else
					// Populate project properties on the page
					handleResponse(response, nextModalID);
				
			}
			else
				alert(response['errorMsg']);
		} else
			alert('Error updating project');

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Display module properties.
// moduleName is the name of the module, or null if a new module.
// TODO: DELETE THIS!
function onModuleProps(moduleName) {

	// Get the folder
	var folders = project['folders'];
	var folder = folders[folderName];

	// Populate the Source File pulldown
	var fileNames = folder['fileNames']
	deleteChildNodes(fileSelect);
	for (var i=0; i<fileNames.length; i++) {

		// Create a new pick list item and add the file name to it.
		var option = document.createElement('option');
		fileSelect.appendChild(option);
		fileName = fileNames[i];
		option.innerHTML = fileName;
		option.setAttribute('value', fileName);

		// If only one file, select it by default.
		if (fileNames.length==1) {
			selectedFileName = fileName;
			option.selected = true;
		}
		
	};

	// Get the module, if any, and populate the form fields from it
	var module = null;
	if (moduleName) {
		var modules = folder['modules'];
		var module = modules[moduleName];
		if (!module)
			return;

		// TODO: POPULATE THE REST OF THE FORM FIELDS
	}

	// Display the modal
	var modal = document.getElementById('modulePropertiesModal');
	modal.style.display = "block";

}

// Keep new module properties.
function onKeepModuleProps(nextModalID) {

	// Check if project exists
	if (!project)
		return false;

	// Check if folders exist
	var folders = project['folders'];
	if (!folders||!folderName)
		return false;

	var folder = folders[folderName];
	if (!folder)
		return false;

	// Check if modules exist
	var modules = folder['modules'];
	if (!modules) {
		modules = {};
		folder['modules'] = modules;
	}

	var failed = false;
	var edit = moduleName? true: false;

	// Check if name populated, try to get the folder
	var module = null;
	var newModuleName = null;
	if (!edit) {
		newModuleName = moduleNameInput.value;
		if (!newModuleName||!checkName(newModuleName)) {
			failed = true;
			moduleNameRules.style.color = 'Red';
		}
		else
			moduleNameRules.style.color = 'Black';
		module = modules[newModuleName];
	}
	else {
		module = modules[moduleName];
		if (!module)
			return false;
	}

	// Get module name and description.
	var moduleTitle = moduleTitleInput.value;
	var moduleDescription = moduleDescriptionInput.value;

	// Get the source file.
	var sourceFile = getSelected(fileSelect);
	if (!sourceFile) {
		failed = true;
		fileSelectRules.style.color = 'Red';
	}
	else
		fileSelectRules.style.color = 'Black';

	// Add the specified packages.
	var packages = [];
	for (var i=0; i<packageSelect.length; i++)
		packages.push(packageSelect[i].value);

	// Find the specified import paths (Python only).
	if (language == 'Python') {
		// TODO:  FIX THIS.  CURRENTLY, SCOPE OF importPaths IS if BLOCK, DOESN'T WORK.
		var importPaths = [];
		for (var i=0; i<importPaths.length; i++)
			importPaths.push(pathSelect[i].value);
	}
	
	// If data validation failure, don't do anything.
	if (failed)
		return;

	// Check if OK to overwrite.
	if (!edit&&module&&!confirm('Module exists.  Overwrite?'))
		return;

	// Create the module if needed
	if (!edit&&newModuleName) {
		moduleName = newModuleName;
		module = {}
		modules[moduleName] = module;
	}		

	// Populate folder attributes
	module['moduleName'] = moduleName;
	module['moduleTitle'] = moduleTitle;
	module['moduleDescription'] = moduleDescription;
	module['sourceFile'] = sourceFile;
	module['packages'] = packages;
	module['importPaths'] = importPaths;
	if (!module['services'])
		module['services'] = {};

	// Prepare the request doc
	var request = {'project': project};

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.open("POST", baseURL + "updatemodule?foldername=" + folderName + "&modulename=" + moduleName);
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var succeeded = response.succeeded;
			if (succeeded) {
				// If succeeded, identify the next screen and process the response.
				var nextModalID = newProject? 'servicePropertiesModal': null;
				// Populate project properties on the page
				handleResponse(response, nextModalID);
			}
			else
				alert(response['errorMsg']);
		} else {
			alert('Error updating project');
		}

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Display service properties.
// serviceName is the name of the service, or null if a new service.
function onServiceProps(serviceName) {

	// Display the modal
	var modal = document.getElementById('servicePropertiesModal');
	modal.style.display = "block";

}

// Keep new service properties.
// toProject is true if focus is to be returned to the main project page,
// false to return to the module properties.
function onKeepServiceProps(edit) {

	// Check if project exists
	if (!project)
		return false;

	// Check if folder exists
	var folders = project['folders'];
	if (!folders||!folderName)
		return false;

	var folder = folders[folderName];
	if (!folder)
		return false;

	// Check if module exist
	var modules = folder['modules'];
	if (!modules||!moduleName)
		return false;

	var module = modules[moduleName];
	if (!module)
		return false;

	// Check if services exist
	var services = module['services'];
	if (!services) {
		services = {};
		module['services'] = services;
	}

	var failed = false;
	var edit = serviceName? true: false;

	// Check if name populated, try to get the folder
	var service = null;
	var newServiceName = null;
	if (!edit) {
		newServiceName = serviceNameInput.value;
		if (!newServiceName||!checkName(newServiceName)) {
			failed = true;
			serviceNameRules.style.color = 'Red';
		}
		else
			serviceNameRules.style.color = 'Black';
		service = services[newServiceName];
	}
	else {
		service = services[serviceName];
		if (!service)
			return false;
	}

	// Get module name and description.
	var serviceTitle = serviceTitleInput.value;
	var serviceDescription = serviceDescriptionInput.value;

	// Get the name of the function.
	var functionName = getSelected(functionSelect);
	if (!functionName) {
		failed = true;
		functionSelectRules.style.color = 'Red';
	}
	else
		functionSelectRules.style.color = 'Black';

	// Get HTTP method
	var method = methodPOSTInput.checked? 'POST': 
		(methodGETInput.checked? 'GET': null);

	// Get parameter options
	var includeBody = includeBodyInput.checked;
	var includeParams = includeParamsInput.checked;
	var paramsToDF = paramsToDFInput.checked;
	var includeRequest = includeRequestInput.checked;

	// Get the input parse type method
	var inputParseType = getSelected(inputParseTypeInput);
	inputParseType = inputParseType? inputParseType: 'none';
	
	// Get the input parse type method
	var outputParseType = getSelected(outputParseTypeInput);
	outputParseType = outputParseType? outputParseType: 'none';
	
	// If data validation failure, don't do anything.
	if (failed)
		return;

	// Check if OK to overwrite.
	if (!edit&&service&&!confirm('Service exists.  Overwrite?'))
		return;

	// Create the service if needed
	if (!edit&&newServiceName) {
		serviceName = newServiceName;
		service = {}
		services[serviceName] = service;
	}

	// Populate service attributes
	service['serviceName'] = serviceName;
	service['serviceTitle'] = serviceTitle;
	service['serviceDescription'] = serviceDescription;
	service['functionName'] = functionName;
	service['method'] = method;
	service['includeBody'] = includeBody;
	service['includeParams'] = includeParams;
	service['paramsToDF'] = paramsToDF;
	service['includeRequest'] = includeRequest;
	service['inputParseType'] = inputParseType;
	service['outputParseType'] = outputParseType;

	// Prepare the request doc
	var request = {'project': project};
	
	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	var date = new Date();
	xhr.open("POST", baseURL + "updateproject?timestamp=" + date.getTime());
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var succeeded = response.succeeded;
			if (succeeded)
				handleResponse(response, null);
			else
				alert(response['errorMsg']);
		} 
		else
			alert('Error updating project');

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Display the build screen.
function onBuildProject() {

	// Display the modal
	var modal = document.getElementById('projectBuildModal');
	modal.style.display = 'block';

}

// Build the project.
function buildProject() {

	alert('Feature not implemented!')
	cancelBuild();

}

// Cancel the build.
function cancelBuild() {

	var modal = document.getElementById('projectBuildModal');
	modal.style.display = 'none';

}


function getProject() {

	// Get the project name query parameter
	var params = new URLSearchParams(window.location.search);	
	var projectName = params.get('projectname');

	// If project name specified, try to retrieve the project document
	if (projectName) {

		// Not a new project
		newProject = false;
		
		// Prepare the XHR request.
		var xhr = new XMLHttpRequest();
		var date = new Date();
		xhr.open("GET", baseURL + "getproject" + "?projectname=" + projectName + "&timestamp=" + date.getTime());

		// Define the callback function.
		xhr.onload = function () {

			// Get the response, check HTTP status.
			if (xhr.status == "200") {

				// Retrieve the response and process it.
				var response = JSON.parse(xhr.responseText);
				handleResponse(response, null);

			} else {
				console.error(xhr.responseText);
				alert("Error retrieving project");
			}

		}

		// Send the request.
		xhr.send();
		
	}
	else {
		
		projectPageTitle.innerHTML = 'New Project';
		projectPropertiesTitle.innerHTML = 'New Project';
		onProjectProps();
		
	}
	
}

// Handler for the folder Go button
function onGoFolder(newFolder) {

	// Get the selected folder name
	if (!newProject) {
		// Next becomes Save, Back becomes Cancel.
		folderNext.innerHTML = 'Save';
		folderBack.innerHTML = 'Cancel';
	}
	else {
		// Next becomes Next, Back becomes Back.
		folderNext.innerHTML = 'Next';
		folderBack.innerHTML = 'Back';
	}
	
	// If new folder, no folder name yet.
	if (newFolder)
		folderName = null;
	else {		
		folderName = folderSelect.value;
		// If no folder selected, do nothing.
		if (!newFolder&&!folderName)
			return;
	}

	// Populate the form and display the modal
	popFolderProps();
	switchModal('folderPropertiesModal');

}

// Handler for change to folder select
function onFolderSelectChange() {

	// Get the folder name if any.
	folderName = getSelected(folderSelect);
	
	// Null out the module and service names.
	moduleName = null;
	serviceName = null;
	
	// Enable or disable the folder Go button.
	disableButton(goFolderButton, !folderName);
	
}

// Exit the project and return to the home screen
function onExitProject() {

	// URL of the home screen, plus timestamp to avoid caching.
	var homeURL = 'index.html?timestamp=' + Date.now()

	// Try to include the latest project name if possible, so it can be preselected
	if (project&&project['projectName']) {
		homeURL += '&projectname=' + project['projectName']
	}

	// Navigate to the home page
	window.location.assign(homeURL);	
	
}

// Delete the project
// TODO:  IMPLEMENT THIS!
function onDelProject () {

	alert('Feature not implemented!')
	
}

// Check the project name on change
function onChangeProjectName() {

	// Get the project name and check it.
	var projectName = projectNameInput.value;
	if (!checkName(projectName))
		document.getElementById('projectNameRules').style.color = 'Red';
	else
		document.getElementById('projectNameRules').style.color = 'Black';

	// Enable the Next/Save button
	//disableButton(projectNext, false);
	//projectBack.innerHTML = 'Cancel';

}

// Check the folder name on change
function onChangeFolderName() {

	// Get the folder name and check it.
	var folderName = folderNameInput.value;
	if (!checkName(folderName))
		document.getElementById('folderNameRules').style.color = 'Red';
	else
		document.getElementById('folderNameRules').style.color = 'Black';
	
	// Enable the Next/Save button
	//changed = true;
	//disableButton(folderNext, false);
	//folderBack.innerHTML = 'Cancel';

}

//Check the folder name on change
function onChangeModuleName() {

	// Get the folder name and check it.
	var moduleName = moduleNameInput.value;
	if (!checkName(moduleName))
		moduleNameRules.style.color = 'Red';
	else
		moduleNameRules.style.color = 'Black';
	
	//disableButton(moduleNext, false);
	//changed = true;
	
}

//Check the folder name on change
function onChangeServiceName() {

	// Get the folder name and check it.
	var serviceName = serviceNameInput.value;
	if (!checkName(serviceName))
		serviceNameRules.style.color = 'Red';
	else
		serviceNameRules.style.color = 'Black';
	
	//disableButton(serviceNext, false);
	//changed = true;
	
}

// Go to the selected module
function onGoModule(newModule) {

	// Get the selected module name
	if (!newProject) {
		// Next becomes Save, Back becomes Cancel.
		moduleNext.innerHTML = 'Save';
		moduleBack.innerHTML = 'Cancel';
	}
	else {
		// Next becomes Next, Back becomes Back.
		moduleNext.innerHTML = 'Next';
		moduleBack.innerHTML = 'Back';
	}
	
	// If new folder, no folder name yet.
	if (newModule)
		moduleName = null;
	else {
		moduleName = moduleSelect.value;
		// If no folder selected, do nothing.
		if (!newModule&&!moduleName)
			return;
	}

	// Populate the form and display the modal
	popModuleProps();
	switchModal('modulePropertiesModal');

}

// Go to the selected service
function onGoService(newService) {

	// Get the selected service name
	if (!newProject) {
		// Next becomes Save, Back becomes Cancel.
		serviceNext.innerHTML = 'Save';
		serviceBack.innerHTML = 'Cancel';
	}
	else {
		// Next becomes Next, Back becomes Back.
		serviceNext.innerHTML = 'Next';
		serviceBack.innerHTML = 'Back';
	}

	// If new folder, no folder name yet.
	if (newService)
		serviceName = null;
	else {
		serviceName = serviceSelect.value;
		// If no folder selected, do nothing.
		if (!newService&&!serviceName)
			return;
	}

	// Populate the form and display the modal
	popServiceProps();
	switchModal('servicePropertiesModal');

}

// Check controls in service properties modal to enable/disable according to data
function checkServiceProperties() {

	// Descriptions of the function arguments
	var arguments = [];

	// Handle whether HTTP parameters are to be included
	var methodPOST = methodPOSTInput.checked;
	var includeBody = includeBodyInput.checked;
	if (methodPOST&&includeBody)
		arguments.push('HTTP request body');

	// Handle whether HTTP parameters are to be included
	if (includeParamsInput.checked) {
		paramsToDFInput.disabled = false;
		arguments.push('HTTP query parameters');
	}
	else
		paramsToDFInput.disabled = true;

	// Handle whether the HTTP request is to be included
	if (includeRequestInput.checked) {
		var comment = (language=='Python'? 'Flask': 'Plumber') + ' request object';
		arguments.push(comment);
	}
	
	// Enable or disable choice of body parsing according to the HTTP method
	inputParseTypeInput.disabled = false;
	if (!methodPOST) {
		includeBodyInput.disabled = true;
		inputParseTypeInput.disabled = true;
	}
	else {
		includeBodyInput.disabled = false;
		if (!includeBody)
			inputParseTypeInput.disabled = true;
	}

	// Fill in the function argument description
	var inputComments = document.getElementById('inputComments');
	var desc = 'The function should have no arguments.';
	if (arguments.length) {
		desc = 'Function arguments:  (';
		for (var i=0; i<arguments.length; i++) {
			desc += arguments[i];
			if (i < arguments.length - 1)
				desc += ', ';
		}
		desc += ')';
	}
	document.getElementById('inputComments').innerHTML = desc;

	changed = true;

}

// Displays the directory selected in the source upload screen.
function onSourceUploadChange() {

	// Display the source directory relative path name.
	var files = event.target.files;
	var sourceRelPath = '';
	if (files.length>0) {
		sourceRelPath = '/';
		var firstPath = files[0].webkitRelativePath;
		var slashPos = firstPath.search(/[\\/]/);
		if (slashPos > 0)
			sourceRelPath = firstPath.substring(0, slashPos);
	}
	sourcePathInput.innerHTML = sourceRelPath;	

	folderInput(null);

}

//Handle the Next/Save button in the Project Properties screen.
function onProjectNext() {

	// Create or save the project
	if (newProject)
		writeProject(null, false, false);
	else {
		projectBack.innerHTML = 'Close';
		writeProject(project, true, false);
	}

}

// Handles cancel button on Project Properties screen.
function onProjectCancel() {

	// Create the project
	if (newProject) {
		writeProject(null, false, true);
	}
	else if ((projectBack.innerHTML=='Close')||confirm('Discard changes?'))
		switchModal(null);

}

//Handle the Next/Save button in the Project Properties screen.
function onFolderNext() {

	folderBack.innerHTML = 'Close';
	var modalID = newProject? 'modulePropertiesModal': 'folderPropertiesModal';
	onKeepFolderProps(modalID);

}

// Handles back button on Folder Properties screen.
function onFolderBack() {

	var modalID = newProject? 'projectPropertiesModal': null;
	if (!changed||confirm('Discard changes?'))
		switchModal(modalID);

}

//Handles cancel button on Folder Properties screen.
function onFolderCancel() {

	if (!changed||confirm('Discard changes?'))
		switchModal(null);

}

//Handle the Next/Save button in the Module Properties screen.
function onModuleNext() {

	var modalID = newProject? 'servicePropertiesModal': null;
	onKeepModuleProps(modalID);

}

// Handles back button on Module Properties screen.
function onModuleBack() {

	//var modalID = newProject? 'folderPropertiesModal': null;
	if (!changed||confirm('Discard changes?'))
		switchModal('folderPropertiesModal');

}

//Handles cancel button on Module Properties screen.
function onModuleCancel() {

	if (!changed||confirm('Discard changes?'))
		switchModal(null);

}

//Handle the Next/Save button in the Service Properties screen.
function onServiceNext() {

	// TODO:  GO TO BUILD SCREEN FOR NEW PROJECTS.
	onKeepServiceProps(null);

}

// Handles back button on Service Properties screen.
function onServiceBack() {

	//var modalID = newProject? 'modulePropertiesModal': null;
	if (!changed||confirm('Discard changes?'))
		switchModal('modulePropertiesModal');

}

//Handles cancel button on Service Properties screen.
function onServiceCancel() {

	if (!changed||confirm('Discard changes?'))
		switchModal(null);

}

// Checks whether the package input element is populated to enable/disable the add button.
function onPackageInputChange() {

	// Package add button disabled iff no text to input
	packageAddButton.disabled = !packageInput.length;
	
}

// Adds a package if one has been specified.
function onPackageAdd() {

	// Add the value if it exists
	var value = packageInput.value;
	if (value) {
		addSelect(packageSelect, value, value);
		packageInput.value = '';
		changed = true;
		packageDelButton.disabled = false;
	}
	packageAddButton.disabled = true;

}

// Deletes a package if one is selected.
function onPackageDel() {

	// Delete the currently selected item, if any
	if (packageSelect.selectedIndex >= 0) {
		delSelected(packageSelect);
		changed = true;
	}
	packageDelButton.disabled = !packageSelect.length;

}

// Checks whether the path input element is populated to enable/disable the add button.
function onPathInputChange() {

	// Path add button disabled iff no text to input
	pathAddButton.disabled = !pathInput.value;

}

// Adds a path if one has been specified.
function onPathAdd() {

	// Add the value if it exists
	var value = pathInput.value;
	if (value) {
		addSelect(pathSelect, value, value);
		pathInput.value = '';
		changed = true;
		pathDelButton.disabled = false;
	}
	pathAddButton.disabled = true;
	
}

//Deletes a path if one is selected.
function onPathDel() {

	// Delete the currently selected item, if any
	if (pathSelect.selectedIndex >= 0) {
		delSelected(pathSelect);
		changed = true;
	}
	pathDelButton.disabled = !pathSelect.length;
	
}

// Event handler for updating project properties
function projectInput(event) {
	
	if (!changed) {	
		changed = true;
		disableButton(projectNext, false);
		if (!newProject)
			projectBack.innerHTML = 'Cancel';
	}
	
}

// Event handler for updating folder properties
function folderInput(event) {
	
	if (!changed) {	
		changed = true;
		disableButton(folderNext, false);	
		if (!newProject)
			folderBack.innerHTML = 'Cancel';
	}
	
}

// Event handler for updating module properties
function moduleInput(event) {
	
	if (!changed) {	
		changed = true;
		disableButton(moduleNext, false);
		if (!newProject)
			moduleBack.innerHTML = 'Cancel';
	}
	
}

// Event handler for updating service properties
function serviceInput(event) {
	
	if (!changed) {	
		changed = true;
		disableButton(serviceNext, false);
		if (!newProject)
			serviceBack.innerHTML = 'Cancel';
	}
	
}

// Event handler for package name input
function onPackageInput(event) {
	
	if (!changed) {	
		changed = true;
		disableButton(moduleNext, false);
		if (!newProject)
			moduleBack.innerHTML = 'Cancel';
	}
	packageAddButton.disabled = !packageInput.value;
	
}

//Event handler for package name input
function onPathInput(event) {
	
	if (!changed) {	
		changed = true;
		disableButton(moduleNext, false);
		if (!newProject)
			moduleBack.innerHTML = 'Cancel';
	}
	pathAddButton.disabled = !pathInput.value;
	
}

// Handles changes to the package select list.
function onPackageSelectChange() {

	changed = true;
	packageDelButton.disabled = !packageSelect.value;
	
}

//Handles changes to the path select list.
function onPathSelectChange() {

	changed = true;
	pathDelButton.disabled = !pathSelect.value;
	
}
