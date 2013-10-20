var card_name;
var card_printing;

$(document).ready(function() {
    var url = $.url();
    card_name = url.param("name");
    card_printing = url.param("printing");

    $("#card-name").html(card_name);
    $("#card-printing").html(card_printing);
});
