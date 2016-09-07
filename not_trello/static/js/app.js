var $doing = $('#doing');
var $BTN1 = $('#export-btn-1');
var $done = $('#done');
var $BTN2 = $('#export-btn-2');
var $todo = $('#todo');
var $BTN3 = $('#export-btn-3');
var $blocked = $('#blocked');
var $BTN4 = $('#export-btn-4');
var $save = $('#save')

$.ajax({
  url: '/api/card'
})

$.ajax({
  url: '/api/board'
})

$.ajax({
  url: '/api/category'
})

$($BTN1).click(function(){
  var $clone = $done.find('#hide1').clone(true).removeClass('hide');
  $done.find('table1').append($clone);
});

$($BTN2).click(function(){
  var $clone = $doing.find('#hide2').clone(true).removeClass('hide');
  $doing.find('table2').append($clone);
});

$($BTN3).click(function(){
  var $clone = $todo.find('#hide3').clone(true).removeClass('hide');
  $todo.find('table3').append($clone);
});
$($BTN4).click(function(){
  var $clone = $blocked.find('#hide4').clone(true).removeClass('hide');
  $blocked.find('table4').append($clone);
});

// var $content1 = $('#content1');
//
// $('#save').on('click', function(){
//   var editedContent   = $content1.html();
//   localStorage.newContent = editedContent;
// });
//
// if(localStorage.getItem('newContent')) {
//   theContent.html(localStorage.getItem('newContent'));
// }
