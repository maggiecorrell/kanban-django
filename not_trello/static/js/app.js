var $save = $('#save')

<<<<<<< HEAD
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
=======
// $input.appendTo($form)

   $form.submit((function (x) {
    var $board = {
      name: board-name,
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603
      categories_set: categories_set,
    };
    $.ajax({
        type: "POST",
        data :JSON.stringify(board),
<<<<<<< HEAD
        url: "api/board_detail",
        contentType: "application/json"
    });
});

$input.appendTo($form)
=======
        url: "api/board",
        contentType: "application/json"
    });
  }));

// $input.appendTo($form)
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603

   $form.submit((function (y) {
    var $cat = {
      cards_set: cards_set,
<<<<<<< HEAD
      name: category_name,
=======
      name: cat_name,
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603
    };
    $.ajax({
        type: "POST",
        data :JSON.stringify(cat),
        url: "api/category",
        contentType: "application/json"
    });
<<<<<<< HEAD
});

$input.appendTo($form)
=======
}));

// $input.appendTo($form)
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603

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
<<<<<<< HEAD
});
=======
}));
>>>>>>> 29e68196d9f02d5ffaef9e49675ff541f5f1e603
