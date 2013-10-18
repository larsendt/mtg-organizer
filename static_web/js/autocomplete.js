$(document).ready(function() {
    autocomplete();
});

function autocomplete() {
    $("#prefix").keyup(function(event) {
        $("#request-status").html("Thinking...");

        var prefix = $("#prefix").val();

        if(prefix == "") {
            $("#card-suggestions").html("");
            $("#request-status").html("Idling...");
            return;
        }

        var request = $.ajax({
            url: "/api/cards",
            type: "get",
            data: {prefix: prefix}
        });

        request.done(function(response, textStatus, jqXHR) {
            $("#request-status").html("Idling...");
            $("#card-suggestions").html(response);
        });

        request.fail(function(jqXHR, textStatus, errorThrown) {
            $("#request-status").html("Error! " + textStatus);
        });
    });
}

