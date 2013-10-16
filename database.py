import sqlite3
import os

DB_FILE = "cards.sqlite"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE owned_cards (name text,
                                           power text,
                                           toughness text,
                                           type text,
                                           types text,
                                           subtypes text,
                                           cost text,
                                           cmc text,
                                           colors text,
                                           rarity text,
                                           text text,
                                           printing text)""")

    c.execute("""CREATE TABLE reference_cards (name text,
                                               power text,
                                               toughness text,
                                               type text,
                                               types text,
                                               subtypes text,
                                               cost text,
                                               cmc text,
                                               colors text,
                                               rarity text,
                                               text text,
                                               printing text,
                                               PRIMARY KEY (
                                                   name,
                                                   printing)
                                                   ON CONFLICT REPLACE)""")

    conn.commit()
    conn.close()
    print "Initialized database", DB_FILE

def add_owned_cards(cards):
    _add_cards(cards, "owned_cards")

def add_reference_cards(cards):
    _add_cards(cards, "reference_cards")

def _add_cards(cards, db_name):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    for card in cards:
        query_data = (card["name"], card["power"], card["toughness"],
                      card["type"], card["types"], card["subtypes"],
                      card["cost"], card["cmc"], card["colors"],
                      card["rarity"], card["text"], card["printing"])
        try:
            c.execute("INSERT INTO %s VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" % db_name, query_data)
        except sqlite3.OperationalError as e:
            print "Error:", e
            print "======================"
            print "Failed on card:"
            print query_data
            raise e

    conn.commit()
    conn.close()

def owned_cards_by_name_prefix(prefix):
    return _cards_by_name_prefix(prefix, "owned_cards")

def reference_cards_by_name_prefix(prefix):
    return _cards_by_name_prefix(prefix, "reference_cards")

def _cards_by_name_prefix(prefix, db_name):
    print "Selecting by prefix '%s'" % prefix
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM %s WHERE name LIKE ?" % db_name, (prefix + "%",))
    data = c.fetchall()
    conn.close()

    return [dict(zip(["name", "power", "toughness", "type",
                      "types", "subtypes", "cost", "cmc",
                      "colors", "rarity", "text", "printing"], d)) for d in data]


if __name__ == "__main__":
    cards = [{"name":"Llanowar Elves",
              "power":"1",
              "toughness":"1",
              "type":"Elf",
              "types":"Elf",
              "subtypes":"Elf",
              "cost":"{G}",
              "cmc":"1",
              "colors":"Green",
              "rarity":"Common",
              "text":"Tab to add {G} to your mana pool.",
              "printing":"Onslaught"}]

    init_db()
    add_reference_cards(cards)
    print reference_cards_by_name_prefix("ll")

