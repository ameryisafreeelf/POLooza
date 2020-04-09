"""
Mapper for tf model.

@author: crain
"""

from sys import stdin
from string import punctuation

for line in stdin:
    row = line.split('~')
    if len(row) != 8:
        continue
    docid, words = row[1], row[2]
    if len(docid) != 7 or len(words) < 2:
        continue
    for word in words.split():
        print('{0}, {1}\t1'.format(docid, word.lower().strip(punctuation)))
