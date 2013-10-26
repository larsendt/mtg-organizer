#!/usr/bin/env python
import json
import os
import sys
import base64

sys.path.append("../api")
import database

DATA_FILE = "AllSets-x.json"

def db_format(card):
    out_cards = []
    for printing in card["printings"]:
        out_card = {}
        out_card["name"] = card["name"]
        out_card["power"] = card.get("power", None)
        out_card["toughness"] = card.get("toughness", None)
        out_card["type"] = card["type"]
        out_card["types"] = ",".join(card.get("types", []))
        out_card["subtypes"] = ",".join(card["subtypes"]) if "subtypes" in card else None
        out_card["cost"] = card.get("manaCost", None)
        out_card["cmc"] = card.get("cmc", None)
        out_card["colors"] = ",".join(card.get("colors", []))
        out_card["rarity"] = card["rarity"]
        out_card["text"] = card.get("text", "")
        out_card["printing"] = printing
        out_card["multiverseid"] = card["multiverseid"]
        out_card["flavor"] = card.get("flavor", "")
        out_cards.append(out_card)
    return out_cards

def main():
    if not os.path.exists(database.DB_FILE):
        print "Initializing database '%s'..." % database.DB_FILE
        database.init_db()

    print "Loading data file '%s'..." % DATA_FILE
    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    all_cards = []

    for key in data:
        all_cards += data[key]["cards"]

    all_formatted_cards = []

    print "Formatting card entries..."
    for card in all_cards:
        all_formatted_cards += db_format(card)

    print "Inserting %d cards into the database..." % len(all_formatted_cards)
    database.add_reference_cards(all_formatted_cards)

    print "Done"

if __name__ == "__main__": main()
