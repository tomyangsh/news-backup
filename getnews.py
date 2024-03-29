#!/usr/bin/env python3

import feedparser
import os
import time
import markdownify
import re

from bs4 import BeautifulSoup

#China Digital Times
feed = feedparser.parse('https://chinadigitaltimes.net/chinese/feed/')

for post in feed.entries:
    time_published = post.published_parsed
    title = post.title + '.md'
    content = post.content[0].value
    try:
        soup = BeautifulSoup(content, 'html.parser')
        soup.a.decompose()
        if soup.find_all('div', {'class': 'su-spoiler-title'}):
            soup.find_all('div', {'class': 'su-spoiler-title'})[0].decompose()
        md = re.sub(r'(\*\*.+\*\*)', r'\1 ', markdownify.markdownify(str(soup)))
        directory = str(time.strftime("%Y-%m", time_published))
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(directory + '/' + title, "w") as file:
            file.write(md)
    except:
        continue
