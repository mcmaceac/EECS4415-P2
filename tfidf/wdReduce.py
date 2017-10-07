#!/usr/bin/env python
# Revised by Matthew MacEachern
# 2017-10-6

import sys
import re
from math import log

currWord = None
maxFreq = 0



# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing white space
	line = line.strip()
	word, ffc = line.split('#', 1)
	freq, fc = ffc.split('#', 1)
	file, count = fc.split('#', 1)
	
	if word == currWord:						#word has not changed, so we keep the maxFreq, which is the
		tfidf = float(count) * log(20/float(maxFreq)) #num of docs the word appears in
		print('%s,%s\t%s' %(word, file, tfidf))
	else:										#word is different, so we take the first freq which is the 
		currWord = word 						#number of documents the word appears in (maxFreq)
		maxFreq = freq
		tfidf = float(count) * log(20/float(maxFreq))
		print('%s,%s\t%s' %(word, file, tfidf))



	