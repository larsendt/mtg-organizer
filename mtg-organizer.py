#!/usr/bin/env python

import database

while True:
    inp = raw_input("Card prefix: ")
    cards = database.reference_cards_by_name_prefix(inp)
    for card in cards:
        print " ", card["name"], "--", card["printing"]
