#!env/bin/python

# Let Python do the heavy lifting for us
from collections import Counter

# Requests, be quiet!
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

import string
import sys
import wikipedia


if len(sys.argv) != 2:
  print "Usage: %s <word>" % sys.argv[0]
  exit(-1)

word = sys.argv[1]

page = wikipedia.page(word)

vec_space = Counter()

# Python tekkerz (not) - get the content
content = u''.join(page.content).encode('utf-8').strip();

# Remove punctuation
for punc in string.punctuation:
  content = content.replace(punc, '')

# Split
words = content.split()

# Remove the search term
words = filter(lambda x: x != word, words)

print Counter(words)


