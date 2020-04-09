#!/usr/bin/env python
# Profiler mapper to get maximum number of candidate votes by year.

import sys


for line in sys.stdin:
    line = line.split(',')
    key, value = line[0], line[-4]
    try:
        key = int(key)
    except ValueError:
        continue
    try:
        value = int(value)
    except ValueError:
        continue
    print('{0}\t{1}'.format(key, value))
