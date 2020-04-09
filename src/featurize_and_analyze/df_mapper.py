#!/anaconda3/bin/python
"""
Mapper for df model.

@author: crain
"""

from sys import stdin
from string import punctuation

for line in stdin:
    row = line.split('~')
    if len(row) != 8:
        continue
    docid, words = row[0], row[1]
    for word in words.split():
        print('{0}~1'.format(word.lower().strip(punctuation)))
