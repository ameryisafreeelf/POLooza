#!/usr/bin/env python
# Profiler reducer to get maximum number of candidate votes by year.

import sys

CURRENT_YEAR = None
YEAR = None
CURRENT_MAX = 0

for line in sys.stdin:
    line = line.strip()
    if not len(line):
        continue
    YEAR, votecount = line.split('\t', 1)
    try:
        votecount = int(votecount)
    except ValueError:
        continue
    if CURRENT_YEAR == YEAR:
        CURRENT_MAX = max(votecount, CURRENT_MAX)
    else:
        if CURRENT_YEAR:
            print('{0}\t{1}'.format(CURRENT_YEAR, CURRENT_MAX))
        CURRENT_MAX = votecount
        CURRENT_YEAR = YEAR

if CURRENT_YEAR == YEAR:
    print('{0}\t{1}'.format(CURRENT_YEAR, CURRENT_MAX))
