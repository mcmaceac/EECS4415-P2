#!/usr/bin/env python
# Revised by Matthew MacEachern
# 2017-10-6

import sys
import re

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing white space
	line = line.strip()
	# split the line into words
	wordDoc, count = line.split('\t', 1)
	word, docName = wordDoc.split(' ', 1)

	#word is now the key so the words will be grouped together (by key)
	print('%s\t%s %s' % (word, docName, count))