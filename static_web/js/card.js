var card_name;
var card_printing;

function casting_cost_images(cost) {
    html = "<span>"
    costs = cost.split("{");
    for(i in costs) {
        c = costs[i].replace(/\}/gi, "").replace("/", "");
        if(c != "") {
            console.log("Cost: " + c);
            html += "<img src=\"/i/mana/" + c + ".svg\" class=\"mana\">";
        }
    }
    return html + "</span>";
}

function insert_icons(text) {
    icon_table = {
        "\\{G\\}": "<img src=\"/i/mana/G.svg\" class=\"inline-mana\">",
        "\\{W\\}": "<img src=\"/i/mana/W.svg\" class=\"inline-mana\">",
        "\\{U\\}": "<img src=\"/i/mana/U.svg\" class=\"inline-mana\">",
        "\\{R\\}": "<img src=\"/i/mana/R.svg\" class=\"inline-mana\">",
        "\\{B\\}": "<img src=\"/i/mana/B.svg\" class=\"inline-mana\">",
        "\\{0\\}": "<img src=\"/i/mana/0.svg\" class=\"inline-mana\">",
        "\\{1\\}": "<img src=\"/i/mana/1.svg\" class=\"inline-mana\">",
        "\\{2\\}": "<img src=\"/i/mana/2.svg\" class=\"inline-mana\">",
        "\\{3\\}": "<img src=\"/i/mana/3.svg\" class=\"inline-mana\">",
        "\\{4\\}": "<img src=\"/i/mana/4.svg\" class=\"inline-mana\">",
        "\\{5\\}": "<img src=\"/i/mana/5.svg\" class=\"inline-mana\">",
        "\\{6\\}": "<img src=\"/i/mana/6.svg\" class=\"inline-mana\">",
        "\\{7\\}": "<img src=\"/i/mana/7.svg\" class=\"inline-mana\">",
        "\\{8\\}": "<img src=\"/i/mana/8.svg\" class=\"inline-mana\">",
        "\\{9\\}": "<img src=\"/i/mana/9.svg\" class=\"inline-mana\">",
        "\\{10\\}": "<img src=\"/i/mana/10.svg\" class=\"inline-mana\">",
        "\\{11\\}": "<img src=\"/i/mana/11.svg\" class=\"inline-mana\">",
        "\\{12\\}": "<img src=\"/i/mana/12.svg\" class=\"inline-mana\">",
        "\\{13\\}": "<img src=\"/i/mana/13.svg\" class=\"inline-mana\">",
        "\\{14\\}": "<img src=\"/i/mana/14.svg\" class=\"inline-mana\">",
        "\\{15\\}": "<img src=\"/i/mana/15.svg\" class=\"inline-mana\">",
        "\\{16\\}": "<img src=\"/i/mana/16.svg\" class=\"inline-mana\">",
        "\\{17\\}": "<img src=\"/i/mana/17.svg\" class=\"inline-mana\">",
        "\\{18\\}": "<img src=\"/i/mana/18.svg\" class=\"inline-mana\">",
        "\\{19\\}": "<img src=\"/i/mana/19.svg\" class=\"inline-mana\">",
        "\\{20\\}": "<img src=\"/i/mana/20.svg\" class=\"inline-mana\">",
        "\\{T\\}": "<img src=\"/i/mana/T.svg\" class=\"inline-mana\">",
        "\\{G/W\\}": "<img src=\"/i/mana/GW.svg\" class=\"inline-mana\">",
        "\\{G/U\\}": "<img src=\"/i/mana/GU.svg\" class=\"inline-mana\">",
        "\\{B/R\\}": "<img src=\"/i/mana/BR.svg\" class=\"inline-mana\">",
        "\\{B/G\\}": "<img src=\"/i/mana/BG.svg\" class=\"inline-mana\">",
        "\\{W/U\\}": "<img src=\"/i/mana/WU.svg\" class=\"inline-mana\">",
        "\\{W/B\\}": "<img src=\"/i/mana/WB.svg\" class=\"inline-mana\">",
        "\\{R/G\\}": "<img src=\"/i/mana/RG.svg\" class=\"inline-mana\">",
        "\\{R/W\\}": "<img src=\"/i/mana/RW.svg\" class=\"inline-mana\">",
        "\\{U/B\\}": "<img src=\"/i/mana/UB.svg\" class=\"inline-mana\">",
        "\\{U/R\\}": "<img src=\"/i/mana/UR.svg\" class=\"inline-mana\">",
        "\\{2/G\\}": "<img src=\"/i/mana/2G.svg\" class=\"inline-mana\">",
        "\\{2/W\\}": "<img src=\"/i/mana/2W.svg\" class=\"inline-mana\">",
        "\\{2/U\\}": "<img src=\"/i/mana/2U.svg\" class=\"inline-mana\">",
        "\\{2/R\\}": "<img src=\"/i/mana/2R.svg\" class=\"inline-mana\">",
        "\\{2/B\\}": "<img src=\"/i/mana/2B.svg\" class=\"inline-mana\">",
        "\\{P/G\\}": "<img src=\"/i/mana/PG.svg\" class=\"inline-mana\">",
        "\\{P/W\\}": "<img src=\"/i/mana/PW.svg\" class=\"inline-mana\">",
        "\\{P/U\\}": "<img src=\"/i/mana/PU.svg\" class=\"inline-mana\">",
        "\\{P/R\\}": "<img src=\"/i/mana/PR.svg\" class=\"inline-mana\">",
        "\\{P/B\\}": "<img src=\"/i/mana/PB.svg\" class=\"inline-mana\">",
    };

    for(key in icon_table) {
        text = text.replace(new RegExp(key, "g"), icon_table[key]);
    }
    return text;
}

function fmt(text) {
    return text.replace(/\n\n/gi, "<br>");
}

function set_card_image(multiverseid) {
    var url = "/i/cards/" + multiverseid + ".jpg";

    var request = $.ajax({
        url: url,
        type: "get",
    });

    request.done(function(response, textStatus, jqXHR) {
        $("#actual-card-image").attr("src", url);
    });

    request.fail(function(jqXHR, textStatus, errorThrown) {
        $("#actual-card-image").attr("src", "/i/cards/unknown.png");
    });
}

function set_card_rarity(rarity) {
    $("#card-rarity").html("<span>" + rarity + "</span>");

    if(rarity == "Mythic Rare") {
        $("#card-rarity").attr("class", "mythic-rare");
    }
    else if(rarity == "Rare") {
        $("#card-rarity").attr("class", "rare");
    }
    else if(rarity == "Uncommon") {
        $("#card-rarity").attr("class", "uncommon");
    }
    else if(rarity == "Common") {
        $("#card-rarity").attr("class", "common");
    }
    else {
        console.log("Unknown rarity: " + rarity);
    }
}


function set_card_power_toughness(power, toughness) {
    if(power && toughness) {
        $("#power-toughness").html("<span>" + power + "/" + toughness + "</span>");
        $("#power-toughness span").css("visibility", "visible");
    }
    else {
        $("#power-toughness span").css("visibility", "hidden");
    }
}


$(document).ready(function() {
    var url = $.url();
    var request = $.ajax({
        url: "/api/card/",
        type: "get",
        data: {name: url.param("name"),
               printing: url.param("printing")},
        cache: false
    });

    request.done(function(response, textStatus, jqXHR) {
        data = JSON.parse(response);
        console.log("Got card");
        console.log(data);

        $("#card-name").html("<p>" + data.name + "</p>");
        $("#card-printing").html("<p>" + data.printing + "</p>");
        $("#card-text").html("<p>" + insert_icons(fmt(data.text)) + "</p>");
        $("#card-flavor").html("<p>" + fmt(data.flavor) + "</p>");
        $("#card-cost").html(casting_cost_images(data.cost));
        $("#api-link").html("<a href=\"/api/card/?name=" + data.name + "&printing=" + data.printing + "\">View in API</a>");
        set_card_image(data.multiverseid);
        set_card_rarity(data.rarity);
        set_card_power_toughness(data.power, data.toughness);
    });

});
