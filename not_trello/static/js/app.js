var $save = $('#save')

$.ajax({
  url: '/api/card'
})

$.ajax({
  url: '/api/category'
})

$(function (x) {
    var $board = {
      name: board-name,
    };
    $.ajax({
        type: "POST",
        data :JSON.stringify(board),
        url: "api/board",
        contentType: "application/json"
    });
});
