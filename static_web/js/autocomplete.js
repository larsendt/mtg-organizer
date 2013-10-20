$(document).ready(function() {
    setup_autocomplete();
});

var selected_card_id = 0;

function setup_autocomplete() {
    $("#prefix").keyup(function(event) {
        if(event.which == 38 || event.which == 40 || event.which == 13) {
            return false;
        }

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
            data: {prefix: prefix},
            cache: false
        });

        request.done(function(response, textStatus, jqXHR) {
            $("#request-status").html("Idling...");
            var cards_obj = JSON.parse(response);
            update_suggestions(cards_obj);
        });

        request.fail(function(jqXHR, textStatus, errorThrown) {
            $("#request-status").html("Error! " + textStatus);
        });
    });

    $("#prefix").keydown(function(event) {
        if(event.which == 38) {
            select_prev_card();
            return false;
        }
        else if(event.which == 40) {
            select_next_card();
            return false;
        }
        else if(event.which == 13) {
            var card = selected_card();
            if(card) {
                window.location.href = "/card/?" + $.param(card);
            }
            return false;
        }
        return true;
    });
}

function select_next_card() {
    if(selected_card_id < $("#card-suggestions").children().length - 1) {
        $("#card-suggestions").children().eq(selected_card_id).attr("id", "");
        selected_card_id += 1;
        $("#card-suggestions").children().eq(selected_card_id).attr("id", "selected-card");
    }
}

function select_prev_card() {
    if(selected_card_id > 0) {
        $("#card-suggestions").children().eq(selected_card_id).attr("id", "");
        selected_card_id -= 1;
        $("#card-suggestions").children().eq(selected_card_id).attr("id", "selected-card");
    }
}

function selected_card() {
    if($("#card-suggestions").children().length > 0) {
        var card = $("#card-suggestions").children("div").eq(selected_card_id);
        name = card.children("span").eq(0).html();
        printing = card.children("span").eq(1).html();
        return {name:name, printing:printing};
    }
    else {
        return null;
    }
}

function update_suggestions(suggestions) {
    $("#card-suggestions").html("");
    for(idx in suggestions.cards) {
        card = suggestions.cards[idx];
        $("#card-suggestions").append(card_container(card));
    }
    $("#card-suggestions div").first().attr("id", "selected-card");
    selected_card_id = 0;
}

function card_container(card) {
    return "<div class=\"card\"><span class=\"card-name\">" +
        card.name + "</span> :: <span class=\"card-printing\">" + card.printing + "</span></div>";
}
