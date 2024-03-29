const jQuery = window.jQuery;

jQuery(document).ready(function () {
  // Attach click event listener to DIV#red_header
  jQuery('div#red_header').click(function () {
    // Update text color of the <header> element to red
    jQuery('header').css('color', '#FF0000');
  });
});
