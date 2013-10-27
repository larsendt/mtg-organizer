#!/usr/bin/env python

import web
import database
import json

urls = (
        "/api/card/?", "card_api",
        "/api/cards/?", "cards_api",
)

app = web.application(urls, globals())

class cards_api:
    def GET(self):
        inp = web.input()
        if "prefix" in inp:
            results = database.reference_cards_by_name_prefix(inp["prefix"])[0:50]
            squashed = [{"name":i["name"], "printing":i["printing"]} for i in results]
            return json.dumps({"status":"ok", "cards":squashed})
        else:
            return json.dumps({"status":"error", "error":"Prefix parameter required"})

class card_api:
    def GET(self):
        inp = web.input()
        if "name" in inp and "printing" in inp:
            card = database.reference_card(inp["name"], inp["printing"])
            if card is not None:
                return json.dumps(card)
            else:
                return json.dumps({"status":"error", "error":"Card not found"})
        else:
            return json.dumps({"status":"error", "error":"Name and prefix parameters required"})

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
