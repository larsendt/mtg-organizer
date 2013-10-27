#!/usr/bin/env python

import sqlite3
import os

DB_FILE = "../data/cards.sqlite"
B = "../static_web/i/cards/"

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute("SELECT name, printing, multiverseid FROM reference_cards")
data = c.fetchall()

for (name, printing, i) in data:
    if not os.path.exists(os.path.join(B, i+".jpg")):
        print "No image for %s : %s : %s" % (name, printing, i)


