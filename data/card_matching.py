#!/usr/bin/env python

import json
import os
import shutil
import difflib

B = "../static_web/i/cards/"

with open("AllSets-x.json", "r") as f:
    data = json.load(f)

for key in data:
    for card in data[key]["cards"]:
        cardpath = os.path.join(B, key, card["name"] + ".full.jpg")
        if os.path.exists(cardpath):
            dst = os.path.join(B, str(card["multiverseid"]) + ".jpg")
            print "Copying '%s' to '%s'" % (cardpath, dst)
            shutil.copyfile(cardpath, dst)
        else:
            print "No card for", card["name"], "(%s, %d)" % (data[key]["name"], card["multiverseid"])
            basedir = os.path.join(B, key)
            if not os.path.exists(basedir):
                print "No set for", key
                continue
            possibilities = os.listdir(basedir)
            close_matches = difflib.get_close_matches(card["name"], possibilities, cutoff=0.3, n=4)
            if len(close_matches) > 0:
                print "close matches are:"
                for idx, m in enumerate(close_matches):
                    print "\t", idx, ":", m
                inp = raw_input("Choose an index (-1 if no match): ")
                try:
                    idx = int(inp)
                except:
                    continue

                if idx >= 0 and idx < len(close_matches):
                    dst = os.path.join(B, str(card["multiverseid"]) + ".jpg")
                    src = os.path.join(B, key, close_matches[idx])
                    print "Copying '%s' to '%s'" % (src, dst)
                    shutil.copyfile(src, dst)
            else:
                print "No close matches for", cardpath
                raw_input("Enter to continue")
