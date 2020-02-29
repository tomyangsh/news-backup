#!/usr/bin/env python3

import feedparser
import re
#import html2text

a = feedparser.parse('https://chinadigitaltimes.net/chinese/feed/')
#h = html2text.HTML2Text()
#h.ignore_links = True

for post in a.entries:
	d = post.published_parsed
	t = post.title+'.txt'
	c = re.sub(r'\\n', '\n', str(post.content))
#	cc = h.handle(c)
	f = open(str(d[0])+'-'+str(d[1])+'/'+t, "w+")
	f.write(re.sub(r"\[\{'type': 'text/html', 'language': None, 'base': 'https://chinadigitaltimes\.net/chinese/feed/', 'value': '|<.*?>|&nbsp;|&copy(.*\n)*|Feed.*", '', c))
	f.close()
