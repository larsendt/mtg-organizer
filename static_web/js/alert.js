$(document).ready(function() {
    var request = $.ajax({
        url: "/new_set.json",
        type: "get",
        cache: false
    });

    request.done(function(response, textStatus, jqXHR) {
        console.log("Loaded new set data");
        console.log(response);
        if(response.new_set) {
            $("#alert").html("<span>New set: " + response.new_set + ". See <a href=\"http://mtgjson.com/\">mtgjson.com</a></span>");
            $("#alert").css("visibility", "visibile");
        }
        else {
            $("#alert").html("");
            $("#alert").css("visibility", "hidden");
        }
    });

    request.fail(function(jqXHR, textStatus, errorThrown) {
        console.log("Failed to load new set data");
        console.log(textStatus);
    });
});
