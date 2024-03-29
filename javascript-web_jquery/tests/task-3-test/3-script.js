const jQuery = window.jQuery;

jQuery(document).ready(function () {
	// Attach click event listener to DIV#red_header
	jQuery("div#red_header").click(function () {
		// Add the .red class to the <header> element
		jQuery("header").addClass("red");
	});
});
