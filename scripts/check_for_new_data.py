#!/usr/bin/env python

import os
import requests
import re
import sys
import json

VERSION_FILE = "../data/set_version.txt"
ALERT_FILE = "../static_web/new_set.json"
MTG_URL = "http://mtgjson.com/"

def local_version():
    if os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "r") as f:
            return f.read().split()[0]
    else:
        return None


#<h2>Current Version: <span class="value">1.7</span></h2>
def remote_version():
    r = requests.get(MTG_URL)
    matches = re.findall("<span class=\"value\">(\d+.\d+)</span>", r.text)
    return matches[0]

l = local_version()
r = remote_version()

if l != r:
    sys.stderr.write("ALURT!!!!!!!!!!!!!!\n\n")
    sys.stderr.write("NEW MTG DATA SET VERSION! (new: %s, have: %s)\n\n" % (r, l))
    sys.stderr.write("GET DEM DATA SETS!!!!!\n")
    with open(ALERT_FILE, "w") as f:
        json.dump({"new_set":r, "have_set":l}, f)
else:
    with open(ALERT_FILE, "w") as f:
        json.dump({"new_set":None, "have_set":l}, f)
