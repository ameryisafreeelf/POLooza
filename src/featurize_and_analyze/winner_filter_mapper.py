"""
Mapper for winners attached to a keyword.

@author: crain
"""

from sys import stdin

for line in stdin:
    if '\t' not in line:
        continue
    key, value = line.split('\t')
    if ', ' in key:
        docid, word = key.split(', ')
        print('{0}, {1}\t{2}'.format(word, docid, value))
    else:
        names = [name.lower() for name in key.split()]
        for name in names:
            print('{0}\tis_winner: {1}'.format(name, value))
