"""
Mapper for tf-idf model.

@author: crain
"""

from sys import stdin

for line in stdin:
    line = line.split('\t')
    if len(line) != 2:
        continue
    key, freq = line[0], line[1]
    if ', ' in key:
        temp = key.split(', ')
        if len(temp) != 2:
            continue
        docid, word = temp[0], temp[1]
        print('{0}, {1}\t{2}'.format(word, docid, freq))
    else:
        print('{0}\t{1}'.format(key, 1 / float(freq)))

