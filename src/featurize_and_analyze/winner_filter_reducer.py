"""
Reducer for winners attached to a keyword.

@author: crain
"""

from sys import stdin

current_politician = None

for line in stdin:
    if '\t' not in line:
        continue
    word, value = line.split('\t')
    if 'is_winner: ' in value:
        if len(value_split()) == 2:
            is_winner = value.split()[1]
            current_politician = word
    elif ', ' in word and word.split(', ')[0] == current_politician:
        print('{0}\t{1}'.format(word, is_winner))
    else:
        print('{0}\t{1}'.format(word, -1))

