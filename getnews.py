#!/usr/bin/env python3

import feedparser
import re

#China Digital Times
a = feedparser.parse('https://chinadigitaltimes.net/chinese/feed/')

for post in a.entries:
	d = post.published_parsed
	t = post.title+'.txt'
	c = re.sub(r'\\n', '\n', str(post.summary))
	f = open(str(d[0])+'-'+str(d[1])+'/'+t, "w+")
	f.write(re.sub(r"\[\{'type': 'text/html', 'language': None, 'base': 'https://chinadigitaltimes\.net/chinese/feed/', 'value': '|<.*?>|&nbsp;|&copy(.*\n)*|Feed.*", '', c))
	f.close()

