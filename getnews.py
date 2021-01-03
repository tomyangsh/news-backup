#!/usr/bin/env python3

import feedparser
import re
import os
import time

#China Digital Times
a = feedparser.parse('https://chinadigitaltimes.net/chinese/feed/')

for post in a.entries:
	d = post.published_parsed
	t = re.sub(r'\/', '', post.title)+'.md'
	c = re.sub(r'\\n', '\n\n', str(post.content))
	e = re.sub(r'<img.*?src="', '![GitHub](', c)
	g = re.sub(r'" .*?/>', ')', e)
	p = str(time.strftime("%Y-%m", d))
	if not os.path.exists(p):
		os.makedirs(p)
	f = open(p+'/'+t, "w+")
	f.write('# '+post.title+'\n\n'+time.strftime("%Y-%m-%d", d)+'\n\n'+re.sub(r"\[\{'type': 'text/html', 'language': None, 'base': 'https://chinadigitaltimes\.net/chinese/feed/', 'value': '|<.*?>|The post.*\}\]", '', g))
	f.close()

