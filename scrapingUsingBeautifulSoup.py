#!/usr/bin/python
# Simple template file to parse HTML data, and scrap all links within the URL or website
# May be blocked on certain websites, use carefully

import urllib
from BeautifulSoup import *

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
