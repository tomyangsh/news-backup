#!/usr/bin/env python3

import feedparser
import re
import os
import time

#China Digital Times
a = feedparser.parse('https://chinadigitaltimes.net/chinese/feed/')

for post in a.entries:
	d = post.published_parsed
	t = post.title+'.md'
	c = re.sub(r'\\n', '\n\n', str(post.content))
	p = str(time.strftime("%Y-%m", d))
	if not os.path.exists(p):
		os.makedirs(p)
	f = open(p+'/'+t, "w+")
	f.write(re.sub(r"\[\{'type': 'text/html', 'language': None, 'base': 'https://chinadigitaltimes\.net/chinese/feed/', 'value': '|<.*?>|The post.*\}\]", '', c))
	f.close()

