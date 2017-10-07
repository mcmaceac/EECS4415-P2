#!/usr/bin/env python
# Revised by Matthew MacEachern
# 2017-10-6

import sys
import re

occur = 1
currWord = None

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing white space
	line = line.strip()
	# split the line into words
	wordDoc, count = line.split('\t', 1)
	word, docName = wordDoc.split(' ', 1)

	if currWord == word:
		occur = occur + 1
	else:						#we have reached the end of this word meaning occur is the #docs this word appears in
		occur = 1
		currWord = word
	print('%s#%s#%s#%s' % (word, occur, docName, count))
