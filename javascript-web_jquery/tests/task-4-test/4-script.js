const jQuery = window.jQuery;

jQuery(document).ready(function () {
	// Attach click event listener to DIV#toggle_header
	jQuery("#toggle_header").click(function () {
		// Toggle the classes 'red' and 'green' on the <header> element
		jQuery("header").toggleClass("red green");
	});
});
