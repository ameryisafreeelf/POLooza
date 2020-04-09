#!/anaconda3/bin/python
"""
Reducer for tf-idf model.

@author: crain
"""

from sys import stdin

CURRENT_WORD = None
WORD = None
CURRENT_IDF = 0

for line in stdin:
    WORD, freq = line.split('\t')
    try:
        freq = float(freq)
    except:
        continue
    if ', ' in WORD:
        freq *= CURRENT_IDF
        print('{0}\t{1}'.format(WORD, freq))
    else:
        CURRENT_WORD = WORD
        CURRENT_IDF = freq

