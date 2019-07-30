#!/anaconda3/bin/python
"""
Reducer for df model.

@author: crain
"""

from sys import stdin

CURRENT_WORD = None
WORD = None
CURRENT_COUNT = 0

for line in stdin:
    WORD, count = line.split('\t')
    count = int(count)
    if CURRENT_WORD == WORD:
        CURRENT_COUNT += count
    else:
        if CURRENT_WORD:
            print('{0}\t{1}'.format(CURRENT_WORD, CURRENT_COUNT))
        CURRENT_COUNT = count
        CURRENT_WORD = WORD

if CURRENT_WORD == WORD:
    print('{0}\t{1}'.format(CURRENT_WORD, CURRENT_COUNT))
