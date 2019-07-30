"""
Mapper for tf model.

@author: crain
"""

from sys import stdin
from string import punctuation

for line in stdin:
    row = line.split('\t')
    if len(row) != 6:
        continue
    docid, words = row[0], row[1]
    for word in words.split():
        print('{0}, {1}\t1'.format(docid, word.lower().strip(punctuation)))
