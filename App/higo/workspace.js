/* TODO: Change toolbox XML ID if necessary. Can export toolbox XML from Workspace Factory. */
var toolbox = document.getElementById("toolbox");

var options = { 
	toolbox : toolbox, 
	collapse : true, 
	comments : true, 
	disable : true, 
	maxBlocks : Infinity, 
	trashcan : true, 
	horizontalLayout : false, 
	toolboxPosition : 'start', 
	css : true, 
	media : 'https://blockly-demo.appspot.com/static/media/', 
	rtl : false, 
	scrollbars : true, 
	sounds : true, 
	oneBasedIndex : true, 
	grid : {
		spacing : 20, 
		length : 1, 
		colour : '#888', 
		snap : true
	}
};

/* Inject your workspace */ 
var workspace = Blockly.inject("blocklyDiv", options);

/* Load Workspace Blocks from XML to workspace. Remove all code below if no blocks to load */


var create = function(){
	Blockly.JavaScript.addReservedWords('code');
	var code = Blockly.JavaScript.workspaceToCode(workspace);

	// now what do you do want to do with code...?
	alert(code);
}