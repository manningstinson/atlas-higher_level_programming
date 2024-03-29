/* global $ */

$(document).ready(function () {
  // Attach click event listener to DIV#add_item
  $('#add_item').click(function () {
    // Create a new <li> element
    const newItem = $('<li>Item</li>');
    // Append the new <li> element to UL.my_list
    $('ul.my_list').append(newItem);
  });
});
