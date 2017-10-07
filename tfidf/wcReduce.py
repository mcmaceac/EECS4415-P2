#!/usr/bin/env python
# Revised by Matthew MacEachern
# 2017-10-6

import sys

currWord  = None
currCount = 0
word      = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    word, count = line.split('\t', 1)           #word in this case is the word and it the doc it came from
    onlyWord, docName = line.split(' ', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number,
        # so silently ignore this line
        continue

    # this only works if the INPUT is sorted by key!
    if currWord == word:
        currCount += count
    else:
        if currWord:
            # write result to STDOUT
            print('%s\t%s' % (currWord, currCount))
        currCount = count
        currWord  = word

# do not forget to output the last word if needed!
if currWord == word:
    print('%s\t%s' % (currWord, currCount))