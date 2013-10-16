import sqlite3
import os

DB_FILE = "cards.sqlite"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""CREATE TABLE owned_cards (name text collate nocase not null,
                                           printing text not null,
                                           count integer not null,
                                           FOREIGN KEY(name) REFERENCES reference_cards(name)
                                           FOREIGN KEY(printing) REFERENCES reference_cards(printing)
                                           PRIMARY KEY(name, printing))""")

    c.execute("""CREATE TABLE reference_cards (name text collate nocase not null,
                                               power text,
                                               toughness text,
                                               type text not null,
                                               types text,
                                               subtypes text,
                                               cost text,
                                               cmc text,
                                               colors text,
                                               rarity text not null,
                                               text text,
                                               printing text not null,
                                               PRIMARY KEY (
                                                   name,
                                                   printing)
                                                   ON CONFLICT REPLACE)""")

    c.execute("CREATE INDEX reference_cards_name_index ON reference_cards (name collate nocase)")
    c.execute("CREATE INDEX owned_cards_name_index ON owned_cards (name collate nocase)")

    conn.commit()
    conn.close()
    print "Initialized database", DB_FILE

def add_owned_cards(cards):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    for card in cards:
        c.execute("SELECT * FROM owned_cards WHERE name = ? and printing = ?", (card["name"], card["printing"]))
        print c.fetchall()

def add_reference_cards(cards):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    for card in cards:
        query_data = (card["name"], card["power"], card["toughness"],
                      card["type"], card["types"], card["subtypes"],
                      card["cost"], card["cmc"], card["colors"],
                      card["rarity"], card["text"], card["printing"])
        try:
            c.execute("INSERT INTO reference_cards VALUES (?,?,?,?,?,?,?,?,?,?,?,?)" % table_name, query_data)
        except sqlite3.OperationalError as e:
            print "Error:", e
            print "======================"
            print "Failed on card:"
            print query_data
            raise e

    conn.commit()
    conn.close()

def owned_cards_by_name_prefix(prefix):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    c.execute("SELECT * FROM owned_cards WHERE name LIKE ?", (prefix + "%",))
    data = c.fetchall()
    conn.close()
    return data

def reference_cards_by_name_prefix(prefix):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT * FROM reference_cards WHERE name LIKE ?", (prefix + "%",))
    data = c.fetchall()
    conn.close()

    return [dict(zip(["name", "power", "toughness", "type",
                      "types", "subtypes", "cost", "cmc",
                      "colors", "rarity", "text", "printing"], d)) for d in data]

