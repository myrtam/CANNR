/*
CANNR TM analytics container building tool common Javascript functions.
Copyright 2020 Pat Tendick ptendick@gmail.com
All rights reserved
Maintainer Pat Tendick ptendick@gmail.com
 */

// Global variables related to the current project
const baseURL = '/services/tool/services/';
const nameRules = 'Lower case letters, numbers, dashes, and underscores, &le;30 characters.';
const asterisk = '&nbsp;*';
const disabledButton = 'disabled-button';
const enabledButton = 'enabled-button';
const enabledTextColor = '#000000';
const disabledTextColor = '#909090';


//Remove all child nodes
function deleteChildNodes(node) {

	if (!node)
		return;
	
	while (node.firstChild)
		node.removeChild(node.firstChild);

}

//Returns the first selected item from a select list
function getSelected(selectList) {

	// Find the first selected item.
	for (var i=0; i<selectList.length; i++) {
		var option = selectList[i];
		if (option.selected)
			return option.value;
	}
	return null;
	
}

// Adds an item to a pick list
function addSelect(selectList, label, value) {

	// Create a new pick list item and add it to the list.
	var option = document.createElement('option');
	selectList.appendChild(option);

	// Set the label and value.
	option.innerHTML = label;
	option.setAttribute('value', value);

}

// Deletes the selected item, if any, from a select list
function delSelected(selectList) {

	var selectedIndex = selectList.selectedIndex;
	if (selectedIndex >= 0)
		selectList.remove(selectedIndex);
	
}

// Selects the item with value
function setSelected(selectList, value) {

	// Check that the value exists in the list.
	if (value&&selectList.querySelector('[value="' + value + '"]'))
		// Set the value.
		selectList.value = value;
	/*
    // Find the first selected item.
	for (var i=0; i<selectList.length; i++) {
		var option = selectList[i];
		option.selected = (option.value==value);
	}
	*/
	
}

// Checks to see that the name is a value project/folder/module/service name.
function checkName(name) {

	if (name.length == 0 || name.length > 30)
		return false;

    if (name.search(/[^a-z0-9_-]/) >= 0)
        return false;
    
    return true
	
}

// Enable or disable a button.  disable=true disables the button, disable=false enables it.
function disableButton(button, disable) {

	// If button not defined, nothing to do.
	if (!button)
		return;
	
	// Disable the button.
	button.disabled = disable;
	button.className = disable? disabledButton: enabledButton;	
	
}
/*
// Handler that executes the appropriate function when the user presses Enter.
function submit(event){
	var keyEvent = event||window.event;
	var keyCode = (keyEvent.keyCode||keyEvent.which);
	if (submitFunction && (keyCode==13||keyCode==3))
		submitFunction();
}
*/

// Returns true if and only if value is contained in string.
function containedIn(value, string) {

	return string.indexOf(value) < 0? false: true;
	
}

// Detect the user's browser
function detectBrowser() {

    var userAgent = navigator.userAgent.toUpperCase();

    if (containedIn("OPR", userAgent))
        return "Opera";

    if (containedIn("CHROME", userAgent)||containedIn("CRIOS", userAgent))
        return "Chrome";

    if (containedIn("FIREFOX", userAgent)||containedIn("FXIOS", userAgent))
        return "Firefox";

    if (containedIn("EDG", userAgent))
        return "Edge";

    if (containedIn("MSIE", userAgent)||containedIn("TRIDENT", userAgent))
        return "IE";

    if (containedIn("MACINTOSH", userAgent)||containedIn("IPHONE", userAgent)
    	||containedIn("IPAD", userAgent)||containedIn("IPOD", userAgent))
        return "Safari";

    return "Unknown";

}

// Returns whether browser supported or not, displays error message if not supported.
function browserSupported() {

	// Check browser, show error message if not compatible.
	var browser = detectBrowser();
	if (browser=="IE"||browser=="Unknown") {
		alert("Browser not supported.  Please use Chrome, Firefox, or Safari.");
		return false;
	}

	return true;
	
}


