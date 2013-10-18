#!/usr/bin/env python

import web
import database

urls = (
        "/api/cards/?", "card_api"
)

app = web.application(urls, globals())

class card_api:
    def GET(self):
        inp = web.input()
        if "prefix" in inp:
            ret_str = ""
            results = database.reference_cards_by_name_prefix(inp["prefix"])
            ret_str += "%d results\n\n" % len(results)
            squashed = [{"name":i["name"], "printing":i["printing"]} for i in results]
            ret_str += "\n\t".join(sorted(map(lambda x: " -- ".join(reversed(x.values())), squashed)))
            return ret_str
        else:
            return "Prefix param is required"

if __name__ == "__main__":
    web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()
