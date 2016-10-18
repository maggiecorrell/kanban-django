var $save = $('#save')

$.ajax({
  url: '/api/card'
})

$.ajax({
  url: '/api/category'
})


$input.appendTo($form)

   $form.submit((function (x) {
    var $board = {
      name: board_name,
      categories_set: categories_set,
    };
    $.ajax({
        type: "POST",
        data :JSON.stringify(board),
        url: "api/board_detail",
        contentType: "application/json"
    });
});

$input.appendTo($form)

   $form.submit((function (y) {
    var $cat = {
      cards_set: cards_set,
      name: category_name,
    };
    $.ajax({
        type: "POST",
        data :JSON.stringify(cat),
        url: "api/category",
        contentType: "application/json"
    });
});

$input.appendTo($form)

   $form.submit((function (z) {
    var $card = {
      activity: activity,
    };
    $.ajax({
        type: "POST",
        data :JSON.stringify(card),
        url: "api/card",
        contentType: "application/json"
    });
});
