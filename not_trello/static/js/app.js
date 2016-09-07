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
      name: board-name,
      categories_set: categories_set,
    };
    $.ajax({
        type: "POST",
        data :JSON.stringify(board),
        url: "api/board",
        contentType: "application/json"
    });
});

$input.appendTo($form)

   $form.submit((function (y) {
    var $cat = {
      cards_set: cards_set,
      name: cat_name,
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
