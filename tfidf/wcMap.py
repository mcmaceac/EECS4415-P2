#!/usr/bin/env python
# Revised by Matthew MacEachern
# 2017-10-6

import sys
import re
import os

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing white space
	line = line.strip()
	# split the line into words
	words = filter(None, re.split('[\W+_]', line))
	# write out word paired with count of 1
	for word in words:
		# write the results to STDOUT
		# tab-delimited; word documentName 1
		print('%s %s\t%s' % (word.lower(), os.environ['mapreduce_map_input_file'], 1))