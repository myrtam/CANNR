/*
CANNR TM analytics container building tool project page Javascript functions.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
 */

// Global variables related to the current project
var selectedFolderName = null;
var project = null;
var module = null;
var module = null;
var service = null;
var projectName = null;
var folderName = null;
var moduleName = null;
var serviceName = null;
var newProject = true;
var language = null;
var built = false;
var running = false;
var currentModal = null;
var timestamp = null;
var folderType = null;
var containerStatus = null;
var containerID = null;
var containerDetail = null;
var containerErrMsg = null;
var dockerConnected = false;

// Flag indicating whether current screen has been changed
var changed = false;

// All of the modals.
var modals = ['projectPropertiesModal', 'folderPropertiesModal', 'modulePropertiesModal',
	'servicePropertiesModal', 'projectBuildModal'];

// Global variables for HTML DOM elements
var buildImageCheckBox = null;
var buildProjectButton = null;
var cancelBuildButton = null;
var codeFolder = null;
var contentFolder = null;
var fileSelect = null;
var fileSelectRules = null;
var folderBack = null;
var folderDescriptionInput = null;
var folderNameAst = null;
var folderNameInput = null;
var folderNext = null;
var folderPropertiesModal = null;
var folderRequired = null;
var folderSelectGroup = null;
var folderSelect = null;
var folderSelectLabel = null;
var folderTitleInput = null;
var folderTypeRow = null;
var functionSelect = null;
var functionSelectRules = null;
//var buildProjectCheckBox = null;
var goFolderButton = null;
var goModuleButton = null;
var goServiceButton = null;
var includeBodyInput = null;
var includeParamsInput = null;
var includeRequestInput = null;
var inputParseTypeInput = null;
var languageP = null;
var languageR = null;
var languageRules = null;
var methodGETInput = null;
var methodPOSTInput = null;
var methodRules = null;
var moduleBack = null;
var moduleDescriptionInput = null;
var moduleNameAst = null;
var moduleNameInput = null;
var moduleNameRules = null;
var moduleNext = null;
var moduleRequired = null;
var moduleSelect = null;
var modulesRow = null;
var moduleTitleInput = null;
var newFolderButton = null;
var newModuleButton = null;
var newModulesRow = null;
var newServiceButton = null;
var newServicesRow = null;
var outputParseTypeInput = null;
var packageAddButton = null;
var packageDelButton = null;
var packageInput = null;
var packageSelect = null;
//var paramsToDFInput = null;
var projectBack = null;
var projectBuildModal = null;
var projectDescriptionInput = null;
var projectNameAst = null;
var projectNameInput = null;
var projectNameRules = null;
var projectNext = null;
var projectPageTitle = null;
var projectPropertiesTitle = null;
var projectRequired = null;
var projectTitleInput = null;
var serviceBack = null;
var serviceDescriptionInput = null;
var serviceNameAst = null;
var serviceNameInput = null;
var serviceNameRules = null;
var serviceNext = null;
var servicePropertiesTitle = null;
var serviceRequired = null;
var serviceSelect = null;
var servicesRow = null;
var serviceTitleInput = null;
var sourcePathInput = null;
var	sourceUpload = null;
var startLocalhostCheckBox = null;
var statusPane = null;
var stopContainerButton = null;
var titleFolder = null;
var titleFolderPath = null;
var titleModuleFolder = null;
var titleModuleModule = null;
var titleModulePath = null;
var titleServiceFolder = null;
var titleServiceModule = null;
var titleServicePath = null;
var titleServicePort = null;
var titleServiceService = null;
var uploadRequired = null;
var workersInput = null;
var workerRules = null;
var languageRow = null;
var workersRow = null;

// Initialize DOM object variables
function initDOMObjects() {

	buildImageCheckBox = document.getElementById('buildImageCheckBox');
	buildProjectButton = document.getElementById('buildProjectButton');
	cancelBuildButton = document.getElementById('cancelBuildButton');
	codeFolder = document.getElementById('codeFolder');
	contentFolder = document.getElementById('contentFolder');
	fileSelect = document.getElementById('fileSelect');
	fileSelectRules = document.getElementById('fileSelectRules');
	folderBack = document.getElementById('folderBack');
	folderDescriptionInput = document.getElementById('folderDescriptionInput');
	folderNameAst = document.getElementById('folderNameAst');
	folderNameInput = document.getElementById('folderNameInput');
	folderNext = document.getElementById('folderNext');
	folderPropertiesModal = document.getElementById('folderPropertiesModal');
	folderRequired = document.getElementById('folderRequired');
	folderSelect = document.getElementById('folderSelect');
	folderSelectGroup = document.getElementById('folderSelectGroup');
	folderSelectLabel = document.getElementById('folderSelectLabel');
	folderTitleInput = document.getElementById('folderTitleInput');
	folderTypeRow = document.getElementById('folderTypeRow');
	functionSelect = document.getElementById('functionSelect');
	functionSelectRules = document.getElementById('functionSelectRules');
	//buildProjectCheckBox = document.getElementById('buildProjectCheckBox');
	goFolderButton = document.getElementById('goFolderButton');
	goModuleButton = document.getElementById('goModuleButton');
	goServiceButton = document.getElementById('goServiceButton');
	includeBodyInput = document.getElementById('includeBodyInput');
	includeParamsInput = document.getElementById('includeParamsInput');
	includeRequestInput = document.getElementById('includeRequestInput');
	inputParseTypeInput = document.getElementById('inputParseTypeInput');
	languageP = document.getElementById('languageP');
	languageR = document.getElementById('languageR');
	languageRow = document.getElementById('languageRow');
	languageRules = document.getElementById('languageRules');
	methodGETInput = document.getElementById('methodGETInput');
	methodPOSTInput = document.getElementById('methodPOSTInput');
	methodRules = document.getElementById('methodRules');
	moduleBack = document.getElementById('moduleBack');
	moduleDescriptionInput = document.getElementById('moduleDescriptionInput');
	moduleNameAst = document.getElementById('moduleNameAst');
	moduleNameInput = document.getElementById('moduleNameInput');
	moduleNameRules = document.getElementById('moduleNameRules');
	moduleNext = document.getElementById('moduleNext');
	moduleRequired = document.getElementById('moduleRequired');
	moduleSelect = document.getElementById('moduleSelect');
	modulesRow = document.getElementById('modulesRow');
	moduleTitleInput = document.getElementById('moduleTitleInput');
	newFolderButton = document.getElementById('newFolderButton');
	newModuleButton = document.getElementById('newModuleButton');
	newModulesRow = document.getElementById('newModulesRow');
	newServiceButton = document.getElementById('newServiceButton');
	newServicesRow = document.getElementById('newServicesRow');
	outputParseTypeInput = document.getElementById('outputParseTypeInput');
	packageAddButton = document.getElementById('packageAddButton');
	packageDelButton = document.getElementById('packageDelButton');
	packageInput = document.getElementById('packageInput');
	packageSelect = document.getElementById('packageSelect');
	//paramsToDFInput = document.getElementById('paramsToDFInput');
	projectBack = document.getElementById('projectBack');
	projectBuildModal = document.getElementById('projectBuildModal');
	projectDescriptionInput = document.getElementById('projectDescriptionInput');
	projectNameAst = document.getElementById('projectNameAst');
	projectNameInput = document.getElementById('projectNameInput');
	projectNameRules = document.getElementById('projectNameRules');
	projectNext = document.getElementById('projectNext');
	projectPageTitle = document.getElementById('projectPageTitle');
	projectPropertiesTitle = document.getElementById('projectPropertiesTitle');
	projectRequired = document.getElementById('projectRequired');
	projectTitleInput = document.getElementById('projectTitleInput');
	serviceBack = document.getElementById('serviceBack');
	serviceDescriptionInput = document.getElementById('serviceDescriptionInput');
	serviceNameAst = document.getElementById('serviceNameAst');
	serviceNameInput = document.getElementById('serviceNameInput');
	serviceNameRules = document.getElementById('serviceNameRules');
	serviceNext = document.getElementById('serviceNext');
	servicePropertiesTitle = document.getElementById('servicePropertiesTitle');
	serviceRequired = document.getElementById('serviceRequired');
	serviceSelect = document.getElementById('serviceSelect');
	servicesRow = document.getElementById('servicesRow');
	serviceTitleInput = document.getElementById('serviceTitleInput');
	sourcePathInput = document.getElementById('sourcePathInput');
	sourceUpload = document.getElementById('sourceUpload');
	startLocalhostCheckBox = document.getElementById('startLocalhostCheckBox');
	statusPane = document.getElementById('statusPane');
	stopContainerButton = document.getElementById('stopContainerButton');
	titleFolder = document.getElementById('titleFolder');
	titleFolderPath = document.getElementById('titleFolderPath');
	titleModuleFolder = document.getElementById('titleModuleFolder');
	titleModulePath = document.getElementById('titleModulePath');
	titleModuleModule = document.getElementById('titleModuleModule');
	titleServiceFolder = document.getElementById('titleServiceFolder');
	titleServiceModule = document.getElementById('titleServiceModule');
	titleServicePath = document.getElementById('titleServicePath');
	titleServicePort = document.getElementById('titleServicePort');
	titleServiceService = document.getElementById('titleServiceService');
	uploadRequired = document.getElementById('uploadRequired');
	workerRules = document.getElementById('workerRules');
	workersInput = document.getElementById('workersInput');
	workersRow = document.getElementById('workersRow');

	// Set input event handlers
	projectDescriptionInput.addEventListener('input', projectInput);
	projectNameInput.addEventListener('input', projectInput);
	projectTitleInput.addEventListener('input', projectInput);
	folderDescriptionInput.addEventListener('input', folderInput);
	folderNameInput.addEventListener('input', folderInput);
	folderTitleInput.addEventListener('input', folderInput);
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

	functionSelect.addEventListener('input', serviceInput);
	functionSelectRules.addEventListener('input', serviceInput);
	includeBodyInput.addEventListener('input', serviceInput);
	includeParamsInput.addEventListener('input', serviceInput);
	includeRequestInput.addEventListener('input', serviceInput);
	inputParseTypeInput.addEventListener('input', serviceInput);
	methodGETInput.addEventListener('input', serviceInput);
	methodPOSTInput.addEventListener('input', serviceInput);
	outputParseTypeInput.addEventListener('input', serviceInput);
	//paramsToDFInput.addEventListener('input', serviceInput);
	serviceDescriptionInput.addEventListener('input', serviceInput);
	serviceNameInput.addEventListener('input', serviceInput);
	serviceNameRules.addEventListener('input', serviceInput);
	serviceTitleInput.addEventListener('input', serviceInput);

	// Set the handler for submitting the data when Enter is pressed.
	//submitFunction = null;
	//document.onkeypress = submit;


}

//Display project properties.
function onProjectProps() {

	changed = false;

	goModal('projectPropertiesModal');

}

// Switch modal
function switchModal(nextModalID) {

	// Hide all the modals.
	modals.forEach(function(modalID, index, array) {
		//var modal = document.getElementById(modalID);
		var modal = $('#' + modalID);
		if (modal)
			//modal.style.display = 'none';
			modal.modal('hide');
	});

	// No changes made in the next modal.
	changed = false;

	// Show the next modal, if any.
	if (nextModalID) {
		/*
		var modalScreen = document.getElementById(nextModalID);
		if (modalScreen)
			modalScreen.modal({});
		*/
		currentModal = $('#' + nextModalID);
		//currentModal = document.getElementById(nextModalID);
		currentModal.modal({});
	}
	// Otherwise, if no modal reload page with project name.
	// That way, if project page gets reloaded, it will remember the project!
	else if (currentModal) {
		currentModal.modal('hide');
		/*
		var params = new URLSearchParams(window.location.search);
		if (!params.has('projectname')&&project&&project['projectName'])
			window.location.search += (window.location.search ? '&': '?') + 'projectname=' + project['projectName'];
		*/
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

// Populates the folder select list
function popFolderSelect() {

	deleteChildNodes(folderSelect);

	// Check for valid project and name
	if (!project)
		return;

	// Get the folders in the project.
	var folders = project['folders'];
	if (!folders)
		return;
		
	// Load the folders into the pick list.
	var keys = Object.keys(folders);
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

	// Set the folder select list to the last one visited, if any.
	setSelected(folderSelect, folderName);

}

// Populates project properties screen
function popProjectProps() {

	// Populate project properties
	projectPageTitle.innerHTML = 'New Project';
	projectPropertiesTitle.innerHTML = 'Project Properties';
	projectNameInput.value = '';
	projectNameInput.disabled = false;
	projectNameInput.focus();
	projectNameRules.innerHTML = nameRules;
	projectNameRules.style.color = 'black';
	projectNameAst.innerHTML = asterisk;
	projectNameAst.style.color = 'black';
	projectRequired.style.color = 'black';
	projectTitleInput.value = '';
	projectDescriptionInput.value = '';

	// Disable the Save button
	disableButton(projectNext, newProject&&!folderName);
	
	// Check for valid project and name
	if (!newProject&&!project)
		return false;

	// Try to get the project name
	projectName = project? project['projectName']: null;
	if (!newProject&&!projectName)
		return false;

	// Populate the folder select list
	popFolderSelect();

	// Set handler to set focus on projectNameInput.
	$('#projectPropertiesModal').on('shown.bs.modal', function () {
	    $('#projectNameInput').focus();
	});

	if (projectName) {

		// Populate project properties
		projectPageTitle.innerHTML = 'Project ' + projectName;
		projectPropertiesTitle.innerHTML = 'Project Properties';
		projectNameRules.innerHTML = '';
		projectNameInput.value = projectName;
		projectNameInput.disabled = true;
		projectNameAst.innerHTML = '';
		projectTitleInput.focus();
		var projectTitle = project['projectTitle'];
		var projectDescription = project['projectDescription'];
		if (projectTitle)
			projectTitleInput.value = projectTitle;
		if (projectDescription)
			projectDescriptionInput.value = projectDescription;

		// Set handler to set focus on projectTitleInput.
		$('#projectPropertiesModal').on('shown.bs.modal', function () {
		    $('#projectTitleInput').focus();
		});

		// Get the folders in the project.
		var folders = project['folders'];
		if (!folders) {
			folders = {}
			project['folders'] = folders
		}
			
	}

	setProjectButtons();

	disableFolderSelect()

	return true;

}

//Shows or hides the folder path on the folder properties screen
function showFolderPath(folderName2, folderType2) {
	
	if (folderName2) {
		if (folderType=='content') {
			var port = project['nginxPort'];
			port = port? (port=='80'? '': ':' + port): '';
			titleFolder.innerHTML = 'http://&ltdomain or ip&gt' + port + '/web/' + folderName2;
		}
		else
			titleFolder.innerHTML = '/' + folderName2;
		titleFolderPath.style.visibility = 'visible';
	}
	else
		titleFolderPath.style.visibility = 'hidden';

}

//Shows or hides the module path on the module properties screen
function showModulePath(folderName2, moduleName2) {
	
	if (folderName2&&moduleName2) {
		titleModuleFolder.innerHTML = folderName2;
		titleModuleModule.innerHTML = moduleName2;
		titleModulePath.style.visibility = 'visible';
	}
	else
		titleModulePath.style.visibility = 'hidden';
	
}

// Returns the service URL
function buildServicePath(folderName2, moduleName2, serviceName2) {

	if (!(folderName2&&moduleName2&&serviceName2))
		return;

	var port = project['nginxPort'];
	port = port? (port=='80'? '': ':' + port): '';

	return 'http://&ltdomain or ip&gt' + port + '/services/' + folderName2 + '/' + moduleName2 + '/' + serviceName2 + '/';
	
}

//Shows or hides the folder path on the folder properties screen
function showServicePath(folderName2, moduleName2, serviceName2) {
	
	if (folderName2&&moduleName2&&serviceName2) {
		var port = project['nginxPort'];
		port = port? (port=='80'? '': ':' + port): '';
		titleServicePort.innerHTML = port;
		titleServiceFolder.innerHTML = folderName2;
		titleServiceModule.innerHTML = moduleName2;
		titleServiceService.innerHTML = serviceName2;
		titleServicePath.style.visibility = 'visible';
	}
	else
		titleServicePath.style.visibility = 'hidden';
	
}

// Adds a message to the build status pane
function addStatusMessage(messageText, indent) {

	var span = document.createElement('span');
	span.innerHTML = messageText + '<br>';
	if (indent)
		span.style.marginLeft = indent;
	statusPane.appendChild(span);

}

// Scrolls the build status pane to the bottom.
function statusScrollBottom() {
	
	statusPane.scrollTop = statusPane.scrollHeight;	
	
}

// Clears the build status pane
function clearStatus() {
	
	deleteChildNodes(statusPane);
	
}

// Prepare the folder properties screen
function prepFolderScreen() {

	// Initialize screen items
	showFolderPath(null, folderType);
	folderNameInput.value = '';
	folderNameInput.disabled = false;
	folderNameInput.focus();
	folderTitleInput.value = '';
	folderDescriptionInput.value = '';
	folderNameRules.innerHTML = nameRules;
	folderNameRules.style.color = 'Black';
	folderNameAst.innerHTML = asterisk;
	folderNameAst.style.color = 'Black';
	languageRules.style.color = 'Black';
	uploadRequired.style.color = 'Black';
	workerRules.style.color = 'Black';
	folderRequired.style.color = 'Black';
	codeFolder.checked = true;
	contentFolder.checked = false;
	languageR.checked = false;
	languageP.checked = false;
	sourcePathInput.innerHTML = '';
	sourceUpload.value = '';
	uploadRequired.innerHTML = '&nbsp;*';
	workersInput.value = 2;

	// Set handler to set focus on folderNameInput.
	$('#folderPropertiesModal').on('shown.bs.modal', function () {
	    $('#folderNameInput').focus();
	});

	deleteChildNodes(moduleSelect);

	folderPropertiesModal.className = 'modal';

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

	changed = false;

	// Prepare the folder properties screen
	prepFolderScreen();

	setFolderButtons();

	folderType = null;
	//folderTypeRow.style.visibility = newProject? 'hidden': 'visible';

	// If folder name doesn't exist, we're done
	if (folderName) {

		// If can't find folder, that's an error.
		var folder = folders[folderName]
		if (!folder)
			return false;

		// Get the folder type
		folderType = folder['folderType'];
		folderType = !folderType? 'code': folderType;

		// Set subtitle to /foldername
		showFolderPath(folderName, folderType);

		// Populate the folder name
		folderNameInput.value = folderName;
		folderNameInput.disabled = true;
		folderNameRules.innerHTML = '';
		folderNameAst.innerHTML = '';
		folderTitleInput.focus();
		folderTitleInput.value = folder['folderTitle'];
		folderDescriptionInput.value = folder['folderDescription'];

		// Set handler to set focus on folderTitleInput.
		$('#folderPropertiesModal').on('shown.bs.modal', function () {
		    $('#folderTitleInput').focus();
		});

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

		// Handle folder type
		if (folderType=='content') {
			codeFolder.checked = false;
			contentFolder.checked = true;
		}
		folderTypeRow.disabled = true;

		// Set programming language
		language = folder['language'];
		if (language) {
			if (language == 'R')
				languageR.checked = true;
			else
				languageP.checked = true;
		}

		// Handle workers
		var workers = folder['workers'];
		workersInput.value = workers? workers: 2;

		// Handle modules
		var modules = folder['modules'];

		// Load the modules into the pick list.
		var keys = Object.keys(modules);
		keys.forEach( function (key, index) {

			// Create a new pick list item and add the project to it.
			var option = document.createElement('option');
			moduleSelect.appendChild(option);
			var module = modules[key];
			label = key
			if (module['moduleTitle'])
				label += ' - ' + module['moduleTitle'];
			option.innerHTML = label;
			option.setAttribute('value', key);

			// If only one project, select it by default.
			if (keys.length==1) {
				selectedModuleName = key;
				option.selected = true;
			}
			
		});

		// Set the module select list to the last one visited, if any.
		setSelected(moduleSelect, moduleName);

	}

	if (!newProject)
		folderPropertiesModal.className = 'modal fade';

	enableCodeFolderProps(!folderType||folderType&&folderType!='content');
	//disableModuleSelect();

	return true;
	
}

// Prep the module properties screen
function prepModuleScreen() {

	// Prep the module name, title, and description inputs
	showModulePath(null, null);
	moduleNameInput.value = '';
	moduleNameInput.disabled = false;
	moduleNameInput.focus();
	moduleNameRules.innerHTML = nameRules;
	moduleNameRules.style.color = 'Black';
	moduleNameAst.innerHTML = asterisk;
	moduleNameAst.style.color = 'Black';
	fileSelectRules.style.color = 'Black';
	moduleRequired.style.color = 'Black';
	moduleTitleInput.value = '';
	moduleDescriptionInput.value = '';

	// Set handler to set focus on moduleNameInput.
	$('#modulePropertiesModal').on('shown.bs.modal', function () {
	    $('#moduleNameInput').focus();
	});

	// Initially list of services is hidden and button disabled
	deleteChildNodes(serviceSelect);

	// Prep the package input items
	deleteChildNodes(packageSelect);
	packageInput.value = '';
	packageAddButton.disabled = true;
	packageDelButton.disabled = true;

	/*
	// Prep the path input items
	deleteChildNodes(pathSelect);
	pathInput.value = '';
	pathAddButton.disabled = true;
	pathDelButton.disabled = true;
	*/

	deleteChildNodes(fileSelect);

	// Disable the Save button
	disableButton(moduleNext, true);

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
	if (!fileNames||fileNames.length==0) {
		alert('The folder contains no files.');
		goModal('folderPropertiesModal');
		return true;
	}

	changed = false;

	// Prep the module properties screen
	prepModuleScreen();
	
	setModuleButtons();
	
	// Get the modules collection
	var modules = folder['modules'];
	if (!modules) {
		modules = {};
		folder['modules'] = modules;
	}

	// Populate the Source File pulldown
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

	// If existing module, can't edit source file.
	fileSelect.disabled = moduleName? true: false;

	// Populate module data if exists
	if (moduleName) {

		// If module can't be found, that's an error
		var module = modules[moduleName];
		if (!module)
			return false;

		// Display module path
		showModulePath(folderName, moduleName);

		// If module name exists, can't be changed
		moduleNameInput.value = moduleName;
		moduleNameInput.disabled = true;
		moduleNameRules.innerHTML = '';
		moduleNameAst.innerHTML = '';

		// Populate module title
		var moduleTitle = module['moduleTitle'];
		moduleTitle = moduleTitle? moduleTitle: '';
		moduleTitleInput.value = moduleTitle;
		moduleTitleInput.focus();

		// Populate module description
		var moduleDescription = module['moduleDescription'];
		moduleDescription = moduleDescription? moduleDescription: '';
		moduleDescriptionInput.value = moduleDescription;

		// Set handler to set focus on moduleTitleInput.
		$('#modulePropertiesModal').on('shown.bs.modal', function () {
		    $('#moduleTitleInput').focus();
		});

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
		var keys = Object.keys(services);
		keys.forEach( function (key, index) {

			// Create a new pick list item and add the project to it.
			var option = document.createElement('option');
			serviceSelect.appendChild(option);
			var service = services[key];
			label = key
			if (service['serviceTitle'])
				label += ' - ' + service['serviceTitle'];
			option.innerHTML = label;
			option.setAttribute('value', key);

			// If only one project, select it by default.
			if (keys.length==1) {
				selectedServiceName = key;
				option.selected = true;
			}
			
		});

		// Set the service select list to the last one visited, if any.
		setSelected(serviceSelect, serviceName);

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

		language = folder['language'];

		/*
		// Add paths (Python only)
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
		*/

	}

	disableServiceSelect();

	return true;
	
}

// Prep the service properties screen
function prepServiceScreen() {

	// Prep the module name, title, and description inputs
	showServicePath(null, null, null);
	serviceNameInput.value = '';
	serviceNameInput.disabled = false;
	serviceNameInput.focus();
	serviceNameRules.innerHTML = nameRules;
	serviceNameRules.style.color = 'Black';
	serviceNameAst.innerHTML = asterisk;
	serviceNameAst.style.color = 'Black';
	serviceNameRules.style.color = 'Black';
	functionSelectRules.style.color = 'Black';
	serviceRequired.style.color = 'Black';
	serviceTitleInput.value = '';
	serviceDescriptionInput.value = '';
	methodPOSTInput.checked = true;
	methodGETInput.checked = false;
	includeBodyInput.checked = true;
	includeParamsInput.checked = false;
	//paramsToDFInput.checked = false;
	//paramsToDFInput.disabled = true;
	includeRequestInput.checked = false;

	// Set handler to set focus on serviceNameInput.
	$('#servicePropertiesModal').on('shown.bs.modal', function () {
	    $('#serviceNameInput').focus();
	});

	deleteChildNodes(functionSelect);

	deleteChildNodes(inputParseTypeInput);
	deleteChildNodes(outputParseTypeInput);

	var option = null;

	// Populate pull down lists for input and output conversions.
	if (language=='R') {

		option = document.createElement('option');
		inputParseTypeInput.appendChild(option);
		option.innerHTML = 'Jsonlite Defaults';
		option.setAttribute('value', 'default');
		option.selected = true;

		/*
		option = document.createElement('option');
		inputParseTypeInput.appendChild(option);
		option.innerHTML = 'R Data Frame';
		option.setAttribute('value', 'dataframe');
		*/
		
		option = document.createElement('option');
		outputParseTypeInput.appendChild(option);
		option.innerHTML = 'Jsonlite Defaults';
		option.setAttribute('value', 'default');
		
		option = document.createElement('option');
		outputParseTypeInput.appendChild(option);
		option.innerHTML = "Do Not Convert";
		option.setAttribute('value', 'none');

	}
	else {
		
		option = document.createElement('option');
		inputParseTypeInput.appendChild(option);
		option.innerHTML = 'Python List/Dictionary (Default)';
		option.setAttribute('value', 'default');
		
		option = document.createElement('option');
		inputParseTypeInput.appendChild(option);
		option.innerHTML = 'Pandas DataFrame';
		option.setAttribute('value', 'dataframe');
		
		option = document.createElement('option');
		inputParseTypeInput.appendChild(option);
		option.innerHTML = 'Numpy Array';
		option.setAttribute('value', 'array');
		
		option = document.createElement('option');
		inputParseTypeInput.appendChild(option);
		option.innerHTML = "Do Not Parse";
		option.setAttribute('value', 'none');

		option = document.createElement('option');
		outputParseTypeInput.appendChild(option);
		option.innerHTML = 'Default JSON Conversion';
		option.setAttribute('value', 'default');

		option = document.createElement('option');
		outputParseTypeInput.appendChild(option);
		option.innerHTML = 'Pandas DataFrame';
		option.setAttribute('value', 'dataframe');
		
		option = document.createElement('option');
		outputParseTypeInput.appendChild(option);
		option.innerHTML = "String Version of Object";
		option.setAttribute('value', 'none');

	}

	setSelected(inputParseTypeInput, 'default');
	setSelected(outputParseTypeInput, 'default');

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

	// Get the language
	language = folder['language'];
	language = language? language: 'Python';

	// Get the list of filenames
	var functionNames = module['functionNames']
	if (!functionNames||functionNames.length==0) {
		alert('The module contains no ' + language + ' functions.');
		goModal('modulePropertiesModal');
	}

	changed = false;

	// Prep the service properties screen
	prepServiceScreen();

	setServiceButtons();

	// Get the modules collection
	var services = module['services'];
	if (!services) {
		services = {};
		module['services'] = services;
	}

	// Populate the Function pulldown
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
	
	// Populate module data if exists
	if (serviceName) {

		// If module can't be found, that's an error
		var service = services[serviceName];
		if (!service)
			return false;

		// Display service path
		showServicePath(folderName, moduleName, serviceName);

		// If service name exists, can't be changed
		serviceNameInput.value = serviceName;
		serviceNameInput.disabled = true;
		serviceNameRules.innerHTML = '';
		serviceNameAst.innerHTML = '';

		// Populate service title
		var serviceTitle = service['serviceTitle'];
		serviceTitle = serviceTitle? serviceTitle: '';
		serviceTitleInput.focus();
		serviceTitleInput.value = serviceTitle;

		// Populate service description
		var serviceDescription = service['serviceDescription'];
		serviceDescription = serviceDescription? serviceDescription: '';
		serviceDescriptionInput.value = serviceDescription;

		// Set handler to set focus on serviceTitleInput.
		$('#servicePropertiesModal').on('shown.bs.modal', function () {
		    $('#serviceTitleInput').focus();
		});

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
		//paramsToDF = service['paramsToDF'];
		includeRequest = service['includeRequest'];
		inputParseType = service['inputParseType'];
		outputParseType = service['outputParseType'];
		includeBodyInput.checked = includeBody? true: false;
		includeParamsInput.checked = includeParams? true: false;
		//paramsToDFInput.checked = paramsToDF? true: false;
		includeRequestInput.checked = includeRequest? true: false;
		setSelected(inputParseTypeInput, inputParseType);
		setSelected(outputParseTypeInput, outputParseType);

	}

	checkServiceProperties();
	
	return true;

}



function popBuildScreen() {
	
	// Make sure the project exists
	if (!project)
		return false;

	// Get the project name and folders
	projectName = project['projectName'];
	var folders = project['folders'];
	if (!projectName||!folders)
		return false;

	// Add the status of the connection or container as appropriate.
	if (dockerConnected&&containerID) {
		addStatusMessage('The following container is associated with this project:', null);
		addStatusMessage(containerID, '20px');
		addStatusMessage('Status is ' + containerStatus, '20px');
	}
	else if (containerStatus == 'unableToConnect') {
		addStatusMessage('Unable to connect to Docker:', null);
		addStatusMessage(containerDetail, '20px');
	}

	// Display the project name and title, if any.
	var projectTitle = project['projectTitle'];
	addStatusMessage('Project to be built:  ' + projectName + (projectTitle? ' - ' + projectTitle: ''), null);
	addStatusMessage('Folders:', null);

	// Loop through the folders
	var folderKeys = Object.keys(folders);
	folderKeys.forEach(function(folderKey, index) {

		// Get the folder
		var folder = folders[folderKey];
		if (!folder)
			return false;

		var folderTitle = folder['folderTitle'];
		addStatusMessage(folderKey + (folderTitle? ' - ' + folderTitle: ''), '20px');

		var folderType2 = folder['folderType'];
		var sourcePath = folder['sourcePath'];
		if (folderType2&&folderType2=='content') {
			addStatusMessage('Static content', '40px');
			if (sourcePath)
				addStatusMessage('Source=' + sourcePath, '40px');
			var port = project['nginxPort'];
			port = port? (port=='80'? '': ':' + port): '';
			addStatusMessage('http://&ltdomain or ip&gt' + port + '/web/' + folderKey, '40px');
			return;
		}

		var modules = folder['modules'];
		var moduleKeys = Object.keys(modules);
		if (moduleKeys.length > 0)
			addStatusMessage('Services:', '40px');
		moduleKeys.forEach(function(moduleKey, index) {

			// Get the folder
			var module = modules[moduleKey];
			if (!module)
				return false;

			var services = module['services'];
			var serviceKeys = Object.keys(services);
			serviceKeys.forEach(function(serviceKey, index) {

				// Get the folder
				var service = services[serviceKey];
				if (!service)
					return false;

				var serviceTitle = project['serviceTitle'];
				addStatusMessage(serviceKey + (serviceTitle? ' - ' + serviceTitle: '') + ':', '60px');
				addStatusMessage(buildServicePath(folderKey, moduleKey, serviceKey), '80px');

			});

		});

	});

	addStatusMessage('', null);

	// Set the state of the buttons.
	setBuildButtons();

	// Find build property values based on project and defaults
	buildImageValue = project['buildImage'];
	startLocalhostValue = project['startLocalhostCheckBox'];
    imageTags = project['imageTags'];
	image = (imageTags&&imageTags.length)? imageTags[0]: null;

	// Build image unless specified otherwise
	buildImageValue = buildImageValue==false? false: true;
	// Don't start container unless explicitly specified
	startLocalhostValue = !!startLocalhostValue;

	// Populate build checkbox properties
	buildDisabled = (containerStatus == 'unableToConnect');
	buildImageCheckBox.checked = buildImageValue;
	startLocalhostCheckBox.checked = startLocalhostValue;
	buildImageCheckBox.disabled = buildDisabled;
	startLocalhostCheckBox.disabled = !buildImageValue||buildDisabled;
	
	built = false;
	//running = false;

	if (newProject)
		projectBuildModal.className = 'modal';
	else
		projectBuildModal.className = 'modal fade';
		
	return true;
	
}



// Populates build screen
function popBuildProps() {

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	var url = baseURL + "getstatus" + '/' + projectName;
	xhr.open("GET", url);
	xhr.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and process it.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {
				containerDetail = data['detail'];
				dockerConnected = data.succeeded;
				if (dockerConnected) {
					
					// Record container status and ID
					containerStatus = data['status'];
					containerID = data['containerID'];
					containerErrMsg = null;
					
				}
				else {

					containerStatus = data['error'];
					containerID = null;
					containerErrMsg = data['errorMsg'];

				}

				running = !!containerID;
				
				if (dockerConnected || containerStatus=='unableToConnect') {
					if (popBuildScreen())
						switchModal('projectBuildModal');
					else
					{
						alert('An error occurred while loading build parameters.');
						onExitProject();
					}
				}
				else {
					alert('Error getting Docker status:\n' + containerDetail);
					onExitProject();
				}
				
			}
			else {
				alert('Error getting Docker status:\nNo data returned');
				onExitProject();
			}

		} else {
			alert('Error getting Docker status:\nHTTP ' + xhr.status);
			onExitProject();
		}

	}

	// Send the request.
	xhr.send();
	
}

// Handle the results from back end project operations.
function goModal(nextModalID) {

	// If no modal and the current project exists, not a new project.
	if (!nextModalID && project)
		newProject = false;

	// Populate project properties screen.
	if (!nextModalID||nextModalID=='projectPropertiesModal') {
		if (popProjectProps())
			switchModal(nextModalID);
		else
			{
				alert('An error occurred while loading the project.');
				onExitProject();
			}
	}
	// Populate folder properties screen.
	else if (nextModalID=='folderPropertiesModal') {
		if (popFolderProps())
			switchModal(nextModalID);
		else
			{
				alert('An error occurred while loading the folder.');
				onExitProject();
			}
	}
	// Populate module properties screen.
	else if (nextModalID=='modulePropertiesModal') {
		if (popModuleProps())
			switchModal(nextModalID);
		else
			{
				alert('An error occurred while loading the module.');
				onExitProject();
			}
	}
	// Populate service properties screen.
	else if (nextModalID=='servicePropertiesModal') {
		if (popServiceProps())
			switchModal(nextModalID);
		else
			{
			alert('An error occurred while loading the service.');
			onExitProject();
		}
	}
	// Populate build screen.
	else if (nextModalID=='projectBuildModal')
		popBuildProps();
	
}

// Saves an existing project
function updateProject(nextModalID) {

	// Prepare the request doc
	var request = {'data': {'project': project}};

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.open("POST", baseURL + "updateproject/" + projectName);
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {
				if (data.succeeded) {
					project = data['project'];
					// Populate the folder select list
					popFolderSelect();
					goModal(nextModalID);
				}
				else
					alert(data['errorMsg']);
			}
		} 
		else
			alert('Error updating project');

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Captures project properties and writes the modified document to the service.
function writeProject(project1, overwrite, cancel) {

	// Handle cancel for new project (go back to main screen)
	if (newProject&&cancel) {
		onExitProject();
		return;
	}

	// Identify the next screen.
	var nextModalID = newProject? 'folderPropertiesModal': null;

	// If no change, just go to the next screen
	if (!changed)
		goModal(nextModalID);

	projectRequired.style.color = 'Black';

	// Get the project name and check it.
	var newProjectName = projectNameInput.value;

	// Check the project name.
	if (!newProjectName) {
		projectNameAst.style.color = 'Red';
		projectRequired.style.color = 'Red';
	}
	else if (!checkName(newProjectName)) {
		if (!cancel) {
			projectNameRules.style.color = 'Red';
			return;
		}
		else
			switchModal(null);
	}
	else {
		projectNameAst.style.color = 'Black';
		projectNameRules.style.color = 'Black';
	}

	// Prepare the project to write to the service.
	var project2 = project1? JSON.parse(JSON.stringify(project1)): null;
	if (!project2)
		project2 = {
				'projectName': newProjectName,
				'timestamp': timestamp
		};

	project2['projectTitle'] = projectTitleInput.value;
	project2['projectDescription'] = projectDescriptionInput.value;
	if (!project2['folders'])
		project2['folders'] = {};
	
	// Check that the project has a name.  This should never happen.
	if (!project2['projectName'])
		return;

	// Record the project name
	projectName = newProjectName;

	// Define the request, including the project.
	var request = {
		'data': {
			'project': project2,
			'overwrite': overwrite
		}
	};

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	if (newProject&&!folderName)
		xhr.open("POST", baseURL + "createproject/" + projectName);
	else
		xhr.open("POST", baseURL + "updateproject/" + projectName);
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {

				if (data.succeeded) {
					project = data['project'];
					popProjectProps();

					// Populate folder properties on the page
					goModal(nextModalID);
					// Notify that project created.
					if (newProject&&!folderName)
						alert('Project created.');

				}
				else {
					// Otherwise, handle the error.
					var error = data['error']
					if (error) {
						// If the project already exists and not cancelling, prompt whether to overwrite and try again.
						if  (error=='projectExists') {
							if (!cancel&&confirm("Project exists.  Overwrite?"))
								writeProject(project1, true, false);
						}
						else
							alert(data['errorMsg']);
					}
					else
						alert('Error creating project');
						
				}
			}
			else
				alert(response['error']);

		} else {
			alert('Error creating project');
		}

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Keep new folder properties.
// nextModalID - ID of modal to which to navigate.
function onKeepFolderProps(nextModalID) {

	// If no change, just go to the next screen
	if (!changed)
		goModal(nextModalID);

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
	folderRequired.style.color = 'Black';

	// Check if name populated, try to get the folder
	var folder = null;
	var newFolderName = null;
	if (!edit) {
		newFolderName = folderNameInput.value;
		if (!newFolderName) {
			folderNameAst.style.color = 'Red';
			folderRequired.style.color = 'Red';
			failed = true;
		}
		else if (!checkName(newFolderName)) {
			folderNameRules.style.color = 'Red';
			failed = true;
		}
		else {
			folderNameAst.style.color = 'Black';
			folderNameRules.style.color = 'Black';
		}
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
	if (!edit&&!files.length || edit&&!sourcePath) {
		failed = true;
		uploadRequired.style.color = 'Red';
		folderRequired.style.color = 'Red';
	}
	else
		uploadRequired.style.color = 'Black';

	// Check if language populated
	language = languageR.checked? 'R':
		languageP.checked? 'Python': null;
	if (!language&&!contentFolder.checked) {
		failed = true;
		languageRules.style.color = 'Red';
		folderRequired.style.color = 'Red';
	}
	else
		languageRules.style.color = 'Black';

	// Check if workers populated
	var workers = parseInt(workersInput.value);
	workers = workers? workers: 2;
	if (!workers||workers < 1 || workers > 1024) {
		failed = true;
		workerRules.style.color = 'Red';
		folderRequired.style.color = 'Red';
	}
	else
		workerRules.style.color = 'Black';

	// If data validation failure, don't do anything.
	if (failed)
		return false;

	// Check if OK to overwrite.
	if (!edit&&folder&&!confirm('Folder exists.  Overwrite?'))
		return;

	// Create the folder if needed
	if (!edit&&newFolderName) {
		folderName = newFolderName;
		folder = {}
		folders[folderName] = folder;
	}		

	// Handle folder title and description
	folder['folderTitle'] = folderTitleInput.value;
	folder['folderDescription'] = folderDescriptionInput.value;

	// Handle folder type
	folderType = !contentFolder.checked? 'code': 'content';
	folder['folderType'] = folderType;

	// Populate folder attributes
	folder['language'] = language;
	folder['sourcePath'] = sourcePath? sourcePath: null;
	folder['workers'] = workers;
	if (!folder['modules'])
		folder['modules'] = {};

	// Prepare the request doc
	var request = {'data': {'project': project}};

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.open("POST", baseURL + "updateproject/" + projectName);
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {
				if (data.succeeded) {
					project = data['project'];

					// Populate the folder select list
					popFolderSelect();
	
					// If files to upload, upload them.
					if (files&&files.length>0) {

						// Populate the multipart form data.
						var formData = new FormData();
						for (var i = 0; i < files.length; i++)
					    	formData.append('files', files[i]);
	
						// Prepare the request
						var xhr2 = new XMLHttpRequest();
						xhr2.open("POST", baseURL + "uploadfolder/" + projectName + '/' + folderName);
						xhr2.setRequestHeader('Content-type','application/octet-stream');
		
						// Define the callback function.
						xhr2.onload = function () {
		
							// Get the response, check HTTP status.
							if (xhr2.status == "200") {
		
								// Retrieve the response and check whether the request succeeded.
								var response2 = JSON.parse(xhr2.responseText);
								var data2 = response2['data'];
								if (data2) {
									if (data2.succeeded) {
										project = data2['project'];
										// Update the project
										//goModal(nextModalID);
										updateProject(nextModalID);
									}
									else
										alert(data2['errorMsg']);
								}
								else
									alert(response2['error']);
	
							}
							else
								alert('Error uploading files');
	
						}
						xhr2.send(formData);
	
					}
					else {
						// Go to the module properties page
						project = data['project'];
						goModal(nextModalID);
					}
				}
				else
					alert(data['errorMsg']);
			}
			else
				alert(response['error']);

		}
		else
			alert('Error updating project');

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Keep new module properties.
function onKeepModuleProps(nextModalID) {

	// If no change, just go to the next screen
	if (!changed)
		goModal(nextModalID);

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

	moduleRequired.style.color = 'Black';

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
		if (!newModuleName) {
			failed = true;
			moduleNameAst.style.color = 'Red';
			moduleRequired.style.color = 'Red';
		}
		else if (!checkName(newModuleName)) {
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
		moduleRequired.style.color = 'Red';
		fileSelectRules.style.color = 'Red';
	}
	else
		fileSelectRules.style.color = 'Black';

	// Add the specified packages.
	var packages = [];
	for (var i=0; i<packageSelect.length; i++)
		packages.push(packageSelect[i].value);

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
	if (!module['services'])
		module['services'] = {};

	// Prepare the request doc
	var request = {'data': {'project': project}};

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.open("POST", baseURL + "updatemodule/" + projectName + '/' + folderName + "/" + moduleName);
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {
				if (data.succeeded) {
					project = data['project'];
					goModal(nextModalID);
				}
				else
					alert(data['errorMsg']);
			}
		} else {
			alert('Error updating project');
		}

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Keep new service properties.
function onKeepServiceProps(nextModalID) {

	// If no change, just go to the next screen
	if (!changed)
		goModal(nextModalID);

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

	serviceRequired.style.color = 'Black';

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
		if (!newServiceName) {
			failed = true;
			serviceNameAst.style.color = 'Red';
			serviceRequired.style.color = 'Red';
		}
		else if (!checkName(newServiceName)) {
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
	//var paramsToDF = paramsToDFInput.checked;
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
	//service['paramsToDF'] = paramsToDF;
	service['includeRequest'] = includeRequest;
	service['inputParseType'] = inputParseType;
	service['outputParseType'] = outputParseType;

	// Update the project
	updateProject(nextModalID);
	
}

// Cancel the build.
function cancelBuild() {

	var modal = document.getElementById('projectBuildModal');
	modal.style.display = 'none';

}

// Tries to retrieve
function getProject() {

	// Get the project name query parameter
	var params = new URLSearchParams(window.location.search);	
	var paramProjectName = params.get('projectname');
	timestamp = params.get('timestamp');

	// Assume a new project
	newProject = true;

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	/*
	var url = baseURL + "getproject_"
	// Add either the project name or timestamp to the URL.
	if (paramProjectName)
		url += "?projectname=" + paramProjectName;
	else if (timestamp)
		url += "?timestamp=" + timestamp;
	*/
	var url = baseURL + "getproject/"
	url += (paramProjectName? paramProjectName: '~') + '/';
	url += (timestamp? timestamp: '0');

	// Add extra timestamp to prevent caching.
	//url += "&timestamp2=" +  Date.now();
	xhr.open("GET", url);
	xhr.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and process it.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {
				if (data.succeeded) {
					project = data['project'];

					// If project exists
					if (project) {
	
						// Not a new project
						newProject = false;
	
						// Go to the main screen
						projectName = paramProjectName;
						goModal(null);
	
						// Populate the folder select list
						popFolderSelect();
	
					}
					else {
			
						projectPageTitle.innerHTML = 'New Project';
						projectPropertiesTitle.innerHTML = 'New Project';
						onProjectProps();
		
					}
				
				}
				else {

					// Display error message.
					var errorMsg = data['errorMsg'];
					console.error(errorMsg);
					var detail = data['detail'];
					console.error(detail);
					alert(errorMsg);
	
					// Return to the main page
					onExitProject();
	
				}

			}

		} else {

			// Display error message.
			console.error(xhr.responseText);
			alert("Error retrieving project");

			// Return to the main page
			onExitProject();

		}

	}

	// Send the request.
	xhr.send();

}

// Handler for the folder Go button
function onGoFolder(newFolder) {

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
	//popFolderProps();
	//switchModal('folderPropertiesModal');
	goModal('folderPropertiesModal');

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
	var homeURL = 'index.html?timestamp=' + Date.now();
	homeURL += '&notitle=true';

	// Try to include the latest project name if possible, so it can be preselected
	if (project&&project['projectName']) {
		homeURL += '&projectname=' + project['projectName'];
	}

	// Check to see if container is running.  If so, offer to stop it.
	if (running&&confirm('A container for this project is currently running.  Would you like to stop it?'))
		stopContainer(null, homeURL);
	else
		// Navigate to the home page
		window.location.assign(homeURL);
	
}

// Check the project name on change
function onChangeProjectName() {

	// Get the project name and check it.
	var projectName2 = projectNameInput.value;
	if (!checkName(projectName2)) {
		projectNameRules.style.color = 'Red';
	}
	else {
		projectNameRules.style.color = 'Black';
	}

}

// Check the folder name on change
function onChangeFolderName() {

	// Get the folder name and check it.
	var folderName2 = folderNameInput.value;
	if (!checkName(folderName2)) {
		document.getElementById('folderNameRules').style.color = 'Red';
		showFolderPath(null, folderType);
	}
	else {
		document.getElementById('folderNameRules').style.color = 'Black';
		showFolderPath(folderName2, folderType);
	}
	
}

//Check the folder name on change
function onChangeModuleName() {

	// Get the folder name and check it.
	var moduleName2 = moduleNameInput.value;
	if (!checkName(moduleName2)) {
		moduleNameRules.style.color = 'Red';
		showModulePath(null, null);
	}
	else {
		moduleNameRules.style.color = 'Black';
		showModulePath(folderName, moduleName2);
	}
	
}

//Check the folder name on change
function onChangeServiceName() {

	// Get the folder name and check it.
	var serviceName2 = serviceNameInput.value;
	if (!checkName(serviceName2)) {
		serviceNameRules.style.color = 'Red';
		showServicePath(null, null, null);
	}
	else {
		serviceNameRules.style.color = 'Black';
		showServicePath(folderName, moduleName, serviceName2);
	}
	
}

// Go to the selected module
function onGoModule(newModule) {

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
	//popModuleProps();
	//switchModal('modulePropertiesModal');
	//goModal('modulePropertiesModal');
	onKeepFolderProps('modulePropertiesModal');

}

// Go to the selected service
function onGoService(newService) {

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
	//popServiceProps();
	//switchModal('servicePropertiesModal');
	//goModal('servicePropertiesModal');
	onKeepModuleProps('servicePropertiesModal');

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
		//paramsToDFInput.disabled = false;
		arguments.push('HTTP query parameters');
	}
	//else
	//	paramsToDFInput.disabled = true;

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

	//changed = true;

}

// Checks the values of build properties and sets build screen elements appropriately.
// TODO:  IMPLEMENT THIS!  ENABLE/DISABLE startLocalhostCheckBox ACCORDING TO buildImageCheckBox
function checkBuildProperties() {

	startLocalhostCheckBox.disabled = !buildImageCheckBox.checked;

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

// Handle the Next/Save button in the Project Properties screen.
function onProjectNext() {

	// Create or save the project
	if (newProject)
		writeProject(project, !!folderName, false);
	else
		writeProject(project, true, false);

}

// Handles cancel button on Project Properties screen.
function onProjectCancel() {

	// Create the project
	if (newProject)
		writeProject(null, false, true);
	else if (!changed||confirm('Discard changes?'))
		switchModal(null);

}

//Handle the Next/Save button in the Project Properties screen.
function onFolderNext() {

	var modalID = (newProject&&folderType!='content')? 'modulePropertiesModal': null;
	onKeepFolderProps(modalID);

}

// Handles back button on Folder Properties screen.
function onFolderBack() {

	var modalID = newProject? 'projectPropertiesModal': null;
	
	if (newProject&&changed)
		onKeepFolderProps(modalID);
	else if (!changed||confirm('Discard changes?'))
		goModal(modalID);

}

//Handle the Next/Save button in the Module Properties screen.
function onModuleNext() {

	var modalID = newProject? 'servicePropertiesModal': 'modulePropertiesModal';
	onKeepModuleProps(modalID);

}

// Handles back button on Module Properties screen.
function onModuleBack() {

	var modalID = 'folderPropertiesModal';

	if (newProject&&changed)
		onKeepModuleProps(modalID);
	else if (!changed||confirm('Discard changes?')) {
		//switchModal(modalID);
		//popFolderProps();
		goModal(modalID);
	}

}

//Handle the Next/Save button in the Service Properties screen.
function onServiceNext() {

	var modalID = newProject? 'projectBuildModal': 'servicePropertiesModal';
	onKeepServiceProps(modalID);

}

// Handles back button on Service Properties screen.
function onServiceBack() {

	var modalID = 'modulePropertiesModal';

	if (newProject&&changed)
		onKeepServiceProps(modalID);
	else if (!changed||confirm('Discard changes?')) {
		//popModuleProps();
		//switchModal(modalID);
		goModal(modalID);
	}

}

//Handles cancel button on folder, module, and service properties screens.
function onCancel() {

	if (!changed||confirm('Discard changes?'))
		//switchModal(null);
		goModal(null);

}

// Checks whether the package input element is populated to enable/disable the add button.
// TODO:  DELETE - NOT USED!
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
		setModuleButtons();
	}
	packageAddButton.disabled = true;

}

// Deletes a package if one is selected.
function onPackageDel() {

	// Delete the currently selected item, if any
	if (packageSelect.selectedIndex >= 0) {
		delSelected(packageSelect);
		changed = true;
		setModuleButtons();
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
		setProjectButtons();
	}
	
}

// Event handler for updating folder properties
function folderInput(event) {
	
	if (!changed) {	
		changed = true;
		setFolderButtons();
	}
	
}

// Event handler for updating module properties
function moduleInput(event) {
	
	if (!changed) {	
		changed = true;
		setModuleButtons();
	}
	
}

// Event handler for updating service properties
function serviceInput(event) {
	
	if (!changed) {	
		changed = true;
		setServiceButtons();
	}
	
}

// Event handler for package name input
function onPackageInput(event) {
	
	/*
	if (!changed) {	
		changed = true;
		setModuleButtons();
	}
	*/
	packageAddButton.disabled = !packageInput.value;
	
}

//Event handler for path name input
function onPathInput(event) {
	
	if (!changed) {	
		changed = true;
		setModuleButtons();
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

//Enable/disable the folder select and buttons.
function disableFolderSelect() {

	if (folderSelect.length) {
		folderSelect.disabled = false;
		disableButton(goFolderButton, false);
		disableButton(delFolderButton, false);
		folderSelectLabel.style.color = enabledTextColor;
	}
	else {
		folderSelect.disabled = true;
		disableButton(goFolderButton, true);
		disableButton(delFolderButton, true);
		folderSelectLabel.style.color = disabledTextColor;
	}

}

//Enable/disable the module select and buttons.
function disableModuleSelect() {

	if (!newProject&&moduleSelect.length) {
		moduleSelect.disabled = false;
		disableButton(goModuleButton, false);
		disableButton(delModuleButton, false);
	}
	else {
		moduleSelect.disabled = true;
		disableButton(goModuleButton, true);
		disableButton(delModuleButton, true);
	}

	disableButton(newModuleButton, newProject);

}

//Enable/disable the service select and buttons.
function disableServiceSelect() {

	if (!newProject&&serviceSelect.length) {
		serviceSelect.disabled = false;
		disableButton(goServiceButton, false);
		disableButton(delServiceButton, false);
	}
	else {
		serviceSelect.disabled = true;
		disableButton(goServiceButton, true);
		disableButton(delServiceButton, true);
	}

	disableButton(newServiceButton, newProject);

}

//Set labels and enables/disables bottom buttons on project properties screen.
function setProjectButtons() {
	
	// Disable the Save button if the project screen has not been saved and it's not a new project with a folder specified
	disableButton(projectNext, !changed&&!(newProject&&projectName));

	// Change button labels appropriately
	if (newProject) {
		projectNext.innerHTML = 'Next';
		projectBack.innerHTML = 'Back';
	}
	else {
		projectNext.innerHTML = 'Save';
		//projectBack.innerHTML = changed? 'Cancel': 'Back';
	}

}

//Set labels and enables/disables bottom buttons on folder properties screen.
function setFolderButtons() {

	// Disable the Save button
	disableButton(folderNext, !changed);

	// Change button labels appropriately
	if (newProject&&folderType!='content') {
		folderNext.innerHTML = 'Next';
		folderBack.innerHTML = 'Back';
	}
	else {
		folderNext.innerHTML = 'Save';
		//folderBack.innerHTML = changed? 'Cancel': 'Back';
	}

}

//Set labels and enables/disables bottom buttons on project properties screen.
function setModuleButtons() {
	
	// Disable the Save button
	disableButton(moduleNext, !changed&&!(newProject&&moduleName));

	// Change button labels appropriately
	if (newProject) {
		moduleNext.innerHTML = 'Next';
		moduleBack.innerHTML = 'Back';
	}
	else {
		moduleNext.innerHTML = 'Save';
		//moduleBack.innerHTML = changed? 'Cancel': 'Back';
	}

}

//Set labels and enables/disables bottom buttons on service properties screen.
function setServiceButtons() {
	
	// Disable the Save button
	disableButton(serviceNext, !changed&&!(newProject&&serviceName));

	// Change button labels appropriately
	if (newProject) {
		serviceNext.innerHTML = 'Next';
		serviceBack.innerHTML = 'Back';
	}
	else {
		serviceNext.innerHTML = 'Save';
		//serviceBack.innerHTML = changed? 'Cancel': 'Back';
	}

}

//Set labels and enables/disables bottom buttons on build screen.
function setBuildButtons() {

	// Change button labels appropriately
	cancelBuildButton.innerHTML = newProject? 'Back': 'Cancel';
	//buildProjectButton.innerHTML = built? (newProject? 'Finish': 'Close'): 'Build';
	//buildProjectButton.innerHTML = newProject? 'Finish': 'Build';
	buildProjectButton.innerHTML = newProject&&built? 'Finish': 'Build';
	disableButton(stopContainerButton, !running);

}

// Handler for delFolderButton.
function onDelFolder() {

	folderName = getSelected(folderSelect);
	// If no folder selected, do nothing.
	if (!project||!folderName)
		return;

	// Check for folders collection
	var folders = project['folders'];
	if (!folders)
		return;

	// Confirm delete
	if (confirm('Delete folder ' + folderName +
		'?  This will delete any directories or files that have been uploaded for the folder.')) {
		// Remove the folder from the pick list
		delSelected(folderSelect);
		// Delete the folder from the folders collection
		delete folders[folderName];
		// Disable the folder select as needed
		disableFolderSelect();
		// Update the project
		// TODO:  NEED TO CALL deleteFolder INSTEAD!!!
		updateProject(null);
	}

}

// Handler for delModuleButton.
function onDelModule() {

	// If no module selected, do nothing.
	moduleName = getSelected(moduleSelect);
	if (!project||!folderName||!moduleName)
		return;

	// Check for folders collection
	var folders = project['folders'];
	if (!folders)
		return;
	
	// Get the folder
	folder = folders[folderName];
	if (!folder)
		return;

	// Check for modules collection
	var modules = folder['modules'];
	if (!modules)
		return;
	
	// Confirm delete
	if (confirm('Delete module ' + moduleName + '?')) {
		// Remove the module from the pick list
		delSelected(moduleSelect);
		// Delete the module from the modules collection
		delete modules[moduleName];
		// Disable the module select as needed
		disableModuleSelect();
		// Set the button labels and enable/disable appropriately
		setFolderButtons();
	}	

}

//Handler for delServiceButton.
function onDelService() {

	// If no module selected, do nothing.
	serviceName = getSelected(serviceSelect);
	if (!project||!folderName||!moduleName||!serviceName)
		return;

	// Check for folders collection
	var folders = project['folders'];
	if (!folders)
		return;
	
	// Get the folder
	folder = folders[folderName];
	if (!folder)
		return;

	// Check for modules collection
	var modules = folder['modules'];
	if (!modules)
		return;
	
	// Get the folder
	module = modules[moduleName];
	if (!module)
		return;

	// Check for services collection
	var services = module['services'];
	if (!services)
		return;

	// Confirm delete
	if (confirm('Delete service ' + serviceName + '?')) {
		// Remove the service from the pick list
		delSelected(serviceSelect);
		// Delete the service from the services collection
		delete services[serviceName];
		// Disable the service select as needed
		disableServiceSelect();
		// Set the button labels and enable/disable appropriately
		setModuleButtons();
	}	

}

// Saves and builds an existing project
function buildProject() {

	// Check that project exists and has a name
	if (!project)
		return;

	projectName = project['projectName'];
	if (!projectName)
		return;

	// Save build options to the project
	project['buildImage'] = buildImageCheckBox.checked;
	project['startLocalhost'] = startLocalhostCheckBox.checked;

	// Prepare the request doc
	var request = {'data': {'project': project}};
	var buildRun = !buildImageCheckBox.checked? 'project': (!startLocalhostCheckBox.checked? 'build': 'run')

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.open("POST", baseURL + "buildproject/" + projectName + '/' + buildRun);
	xhr.setRequestHeader('Content-type','application/json; charset=utf-8');

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {
				if (data.succeeded) {
					project = data['project'];
					// Populate the folder select list
					popFolderSelect();
					addStatusMessage('Project ' + projectName + ' built successfully!', null);
					
					var imageTags = project['imageTags'];
					var imageID = project['imageID'];
					if (imageTags && imageID) {
						addStatusMessage('Container image ' + projectName + ' built successfully:', null);
						addStatusMessage('Image ID ' + imageID.substring(7,1000), '20px');
					}
					
					var containerName = project['containerName'];
					var containerID = project['containerID'];
					var nginxPort = project['nginxPort'];
					nginxPort = nginxPort? nginxPort: 80;

					if (containerName && containerID) {
						running = true;
						addStatusMessage('Container ' + containerName + ' started on port ' + nginxPort + ':', null);
						addStatusMessage('Container ID ' + containerID, '20px');
					}

					built = true;
					statusScrollBottom();
					setBuildButtons();

				}
				else
					alert(data['errorMsg']);
			}
			else
				alert(response['error']);
		} 
		else
			alert('Error building project');

	}

	// Send the request.
	var contentJSON = JSON.stringify(request);
	xhr.send(contentJSON);
	
}

// Stops the container of the current project
function stopContainer(nextModalID, exitURL) {

	// Check that project exists and has a name
	if (!project)
		return;

	projectName = project['projectName'];
	if (!projectName)
		return;

	// Prepare the XHR request.
	var xhr = new XMLHttpRequest();
	xhr.open("GET", baseURL + "stopcontainer/" + projectName);
	xhr.setRequestHeader("Cache-Control", "no-cache, no-store, max-age=0");

	// Define the callback function.
	xhr.onload = function () {

		// Get the response, check HTTP status.
		if (xhr.status == "200") {

			// Retrieve the response and check whether the request succeeded.
			var response = JSON.parse(xhr.responseText);
			var data = response['data'];
			if (data) {
				if (data.succeeded) {
					project = data['project'];
					running = false;
					// Populate the folder select list
					popFolderSelect();
					addStatusMessage('Container stopped!', null);
					statusScrollBottom();
					setBuildButtons();
					alert('Container stopped.');
					if (exitURL)
						window.location.assign(exitURL);
					elif (nextModalID!='projectBuildModal')
						goModal(nextModalID);
						
				}
				else
					alert(data['errorMsg']);
			}
			else
				alert(response['error']);
		} 
		else
			alert('Error stopping container');

	}

	// Send the request.
	xhr.send();
	
}

// Handler for stopContainerButton 
function onStopContainer() {
	
	stopContainer('projectBuildModal', null);
	
}

//Checks whether the package input element is populated to enable/disable the add button.
function onBuildInputChange() {

	if (!changed)
		changed = true;

}

// Build the project
function onBuildProject(){

	if (!project)
		return;

	if (newProject) {
		if (built)
			goModal(null);
		else
			buildProject();			
	}
	else {
		if (confirm('Any previous build of project ' + projectName + ' will be deleted or overwritten.  Also, any running containers for this project will be stopped and deleted.  Proceed?'))
			buildProject();
		else
			addStatusMessage('Project build cancelled.', null);
			statusScrollBottom();
	}

}

// Cancel the build
function onCancelBuild() {

	var modalID = newProject? 'servicePropertiesModal': null;

	if (newProject&&changed) {
		
		//project['buildProject'] = buildProjectCheckBox.checked;
		project['buildImage'] = buildImageCheckBox.checked;
		project['startLocalhost'] = startLocalhostCheckBox.checked;
		
		updateProject(null);
		
	}
	else if (!changed||confirm('Discard changes?')) {
		goModal(modalID);
	}

}

// Go to the build screen for the project
function onGoBuild() {

	// Clear the status pane
	clearStatus();

	goModal('projectBuildModal');

}

// Enables or disables folder properties for code.
function enableCodeFolderProps(isCodeFolder) {

	if (!isCodeFolder) {
		languageR.disabled = true;
		languageP.disabled = true;
		workersInput.disabled = true;
		languageRules.style.visibility = 'hidden';
		workerRules.style.visibility = 'hidden';
		moduleSelect.disabled = true;
		disableButton(goModuleButton, true);
		disableButton(delModuleButton, true);
		disableButton(newModuleButton, true);
	}
	else {
		languageR.disabled = false;
		languageP.disabled = false;
		workersInput.disabled = false;
		languageRules.style.visibility = 'visible';
		workerRules.style.visibility = 'visible';
		disableModuleSelect();
	}

}

// Responds to changes of folder type.
function checkFolderType() {

	// Check the folder type.
	folderType = !contentFolder.checked? 'code': 'content';

	// Enable/disable folder properties fields and buttons
	enableCodeFolderProps(folderType!='content');
	setFolderButtons();

	return;

}

