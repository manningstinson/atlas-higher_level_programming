/* global $ */

$(document).ready(function () {
  // Attach click event listener to DIV#update_header
  $('#update_header').click(function () {
    // Update the text of the <header> element
    $('header').text('New Header!!!');
  });
});
