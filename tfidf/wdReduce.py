#!/usr/bin/env python
# Revised by Matthew MacEachern
# 2017-10-6

import sys
import re
from math import log

currWord = None
wordFreq = 1				#this variable will track number of documents the currWord appears in
cache = []


# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing white space
	line = line.strip()
	# split the line into words
	word, docCount = line.split('\t', 1)
	#print('word:%s docCount: %s' % (word, docCount))
	docName, count = line.split(' ', 1)

	if currWord == word:
		wordFreq = wordFreq + 1
		cache.append(line)
	else:								#a new word has been detected, clear the cache and append the tfidf
		if currWord != None:
			for item in cache:					#word\tdocumentName count
				w, dC = item.split('\t', 1)
				dN, c = dC.split(' ', 1)
				tfidf = float(c) * log(20/wordFreq)
				print('%s,%s\t%s' % (w, dN, tfidf))


		currWord = word 				#change currentWord to the newly deteced word
		cache = []						#clear the cache for the new word
		cache.append(line)
		wordFreq = 1

for item in cache:					#clear the cache one final time
	w, dC = item.split('\t', 1)
	dN, c = dC.split(' ', 1)
	tfidf = float(c) * log(20/wordFreq)
	print('%s,%s\t%s' % (w, dN, tfidf))
	