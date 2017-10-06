#!/usr/bin/env python
# Revised by Parke Godfrey
# 2017-09-24

import sys
import re

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    word, count = line.split('\t', 1)
    letters = re.sub('[^a-zA-Z]+', '', word)

    if len(letters) > 0:
        print('%s\t%s' % (letters[0], count))

