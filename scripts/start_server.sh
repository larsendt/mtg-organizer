#!/bin/bash

spawn-fcgi -d ../api -f ../api/mtg-organizer.py -a 127.0.0.1 -p 55055
