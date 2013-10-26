#!/usr/bin/env python

import requests
import lxml.html
import os
import sqlite3
import time

GATHERER = "http://gatherer.wizards.com/Handlers/Image.ashx?multiverseid=%s&type=card"
DB_FILE = "cards.sqlite"
IMG_FOLDER = "cards/"

if not os.path.exists(IMG_FOLDER):
    os.mkdir(IMG_FOLDER)

conn = sqlite3.connect(DB_FILE)
c = conn.cursor()
c.execute("SELECT name, multiverseid FROM reference_cards")

for (name, mid) in c.fetchall():
    path = os.path.join(IMG_FOLDER, mid + ".jpg")
    if os.path.exists(path):
        print "Skipped", path
    else:
        time.sleep(0.5)
        print "Getting", GATHERER % mid
        r = requests.get(GATHERER % mid)
        print "Writing", path, name
        with open(path, "w") as f:
            f.write(r.content)


