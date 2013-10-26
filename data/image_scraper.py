#!/usr/bin/env python

import requests
import lxml.html
import base64
import os


# new phyrexia http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/newphyrexia/spoiler
# innistrad https://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/innistrad/cig
# dark ascension http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/darkascension/cig
# return to ravnica http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/returntoravnica/cig
# gatecrash http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/gatecrash/cig
# dragon's maze https://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/dragonsmaze/cig
# theros http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/theros/cig
# avacyn restored http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/avacynrestored/cig
# m12 http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2012/cig
# m13 http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2013/cig
# m14 http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/magic2014coreset/cig
# mirrodin beseiged http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/mirrodinbesieged/spoiler

IMG_DIR = "card_images/"
URL = "http://www.wizards.com/magic/tcg/article.aspx?x=mtg/tcg/worldwake/spoiler"
SET = "Worldwake"

directory = os.path.join(IMG_DIR, SET)
if not os.path.exists(directory):
    os.mkdir(directory)

doctext = requests.get(URL).text
dom = lxml.html.fromstring(doctext)
imgs = dom.xpath("//img[@class='article-image'][@title]")
img_urls = map(lambda x: (x.attrib["title"], x.attrib["src"]), imgs)

for (name, url) in img_urls:
    fname = os.path.join(IMG_DIR, SET, base64.b64encode(name.encode("utf-8"), "_-"))

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
