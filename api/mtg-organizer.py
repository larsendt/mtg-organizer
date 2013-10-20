#!/usr/bin/env python

import web
import database
import json

urls = (
        "/api/cards/?", "card_api"
)

app = web.application(urls, globals())

class card_api:
    def GET(self):
        inp = web.input()
        if "prefix" in inp:
            results = database.reference_cards_by_name_prefix(inp["prefix"])[0:10]
            squashed = [{"name":i["name"], "printing":i["printing"]} for i in results]
            return json.dumps({"status":"ok", "cards":squashed})
        else:
            return json.dumps({"status":"error", "error":"Prefix parameter required"})

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
