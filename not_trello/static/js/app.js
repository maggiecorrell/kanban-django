<script>
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
  url: '/api/Board'
})

$('.table-add').click(function () {
  var $clone = $done.find('#hide1').clone(true).removeClass('hide table-line');
  $done.find('table').append($clone);
});
$('.table-add').click(function () {
  var $clone = $doing.find('#hide2').clone(true).removeClass('hide table-line');
  $doing.find('table').append($clone);
});
$('.table-add').click(function () {
  var $clone = $todo.find('#hide3').clone(true).removeClass('hide table-line');
  $todo.find('table').append($clone);
});
$('.table-add').click(function () {
  var $clone = $blocked.find('#hide4').clone(true).removeClass('hide table-line');
  $blocked.find('table').append($clone);
});


// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$save.click(function () {
  var $rows = $doing.find('tr:not(:hidden)');
  var headers = [];
  var data = [];

  // Get the headers (add special header logic here)
  $($rows.shift()).find('th:not(:empty)').each(function () {
    headers.push($(this).text().toLowerCase());
  });

  // Turn all existing rows into a loopable array
  $rows.each(function () {
    var $td = $(this).find('td');
    var h = {};

    // Use the headers from earlier to name our hash keys
    headers.forEach(function (header, i) {
      h[header] = $td.eq(i).text();
    });

    data.push(h);
  });


</script>
