#!/bin/bash
rm -f AllSets-x.json
wget http://mtgjson.com/json/AllSets-x.json && ./json_importer.py


