#!/usr/bin/env python3

import feedparser
import re

#China Digital Times
a = feedparser.parse('https://chinadigitaltimes.net/chinese/feed/')

for post in a.entries:
	d = post.published_parsed
	t = post.title+'.txt'
	c = re.sub(r'\\n', '\n', str(post.content))
	f = open(str(d[0])+'-'+str(d[1])+'/'+t, "w+")
	f.write(re.sub(r"\[\{'type': 'text/html', 'language': None, 'base': 'https://chinadigitaltimes\.net/chinese/feed/', 'value': '|<.*?>|&nbsp;|&copy(.*\n)*|Feed.*", '', c))
	f.close()

#Matters
a = feedparser.parse('http://155.138.236.181:1200/matters/latest')

for post in a.entries:
	d = post.published_parsed
	t = post.title+'.txt'
	c = re.sub(r'</p><p>', '\n', str(post.description))
	f = open(str(d[0])+'-'+str(d[1])+'/'+t, "w+")
	f.write(re.sub(r"<.*?>", '', c))
	f.close()

