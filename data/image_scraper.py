#!/usr/bin/env python

import requests
import lxml.html
import base64
import os


URLS = [
    #("New Phyrexia", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/newphyrexia/spoiler"),
    #("Innistrad", "https://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/innistrad/cig"),
    #("Dark Ascension", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/darkascension/cig"),
    #("Return to Ravnica", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/returntoravnica/cig"),
    #("Gatecrash", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/gatecrash/cig"),
    #("Dragon's Maze", "https://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/dragonsmaze/cig"),
    #("Theros", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/theros/cig"),
    #("Avacyn Restored", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/avacynrestored/cig"),
    #("Magic 2012", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2012/cig"),
    #("Magic 2013", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2013/cig"),
    #("Magic 2014", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2014coreset/cig"),
    #("Mirrodin Beseiged", "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/mirrodinbesieged/spoiler"),
    ("Commander", "http://www.wizards.com/magic/tcg/productarticle.aspx?x=mtg/tcg/commander/cig"),
]

IMG_DIR = "card_images/"

for (SET, URL) in URLS:
    if not os.path.exists(IMG_DIR):
        os.mkdir(IMG_DIR)

    directory = os.path.join(IMG_DIR, SET)
    if not os.path.exists(directory):
        os.mkdir(directory)

    doctext = requests.get(URL).text
    dom = lxml.html.fromstring(doctext)
    imgs = dom.xpath("//img[@class='article-image'][@title]")
    img_urls = map(lambda x: (x.attrib["title"], x.attrib["src"]), imgs)

    for (name, url) in img_urls:
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_' "
        name = name.replace(u"\u2019", "'").replace(u"\u00e6", "AE")
        if name.startswith("Akroma"):
            print name.encode("utf-8")
        tmpname = ""
        for char in name:
            if name.startswith("Akroma"):
                print char
            if char in chars:
                tmpname += char
        fname = os.path.join(IMG_DIR, SET, tmpname)

        while os.path.exists(fname):
            fname += "+"

        if url.endswith(".jpg") or url.endswith(".JPG") or url.endswith(".jpeg"):
            fname += ".jpg"
        elif url.endswith(".png") or url.endswith(".PNG"):
            fname += ".png"
        else:
            print "Unknown extension for url:", url[-6:]

        print "Downloading '%s' to %s" % (name, fname)

        data = requests.get(url).content
        with open(fname, "w") as f:
            f.write(data)
