#!/anaconda3/bin/python
"""
Reducer for tf model.

@author: crain
"""

from sys import stdin

CURRENT_DOCWORD = None
DOCWORD = None
CURRENT_COUNT = 0

for line in stdin:
    DOCWORD, count = line.split('\t')
    count = int(count)
    if CURRENT_DOCWORD == DOCWORD:
        CURRENT_COUNT += count
    else:
        if CURRENT_DOCWORD:
            print('{0}\t{1}'.format(CURRENT_DOCWORD, CURRENT_COUNT))
        CURRENT_COUNT = count
        CURRENT_DOCWORD = DOCWORD

if CURRENT_DOCWORD == DOCWORD:
    print('{0}\t{1}'.format(CURRENT_DOCWORD, CURRENT_COUNT))
