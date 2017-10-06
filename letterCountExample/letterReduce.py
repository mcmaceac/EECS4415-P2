#!/usr/bin/env python
# Revised by Parke Godfrey
# 2017-09-25

import sys

currLetter = None
currCount  = 0
letter     = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input
    letter, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number,
        # so silently ignore this line
        continue

    # this only works if the INPUT is sorted by key!
    if currLetter == letter:
        currCount += count
    else:
        if currLetter:
            # write result to STDOUT
            print('%s\t%s' % (currLetter, currCount))
        currCount  = count
        currLetter = letter

# do not forget to output the last letter if needed!
if currLetter == letter:
    print('%s\t%s' % (currLetter, currCount))

