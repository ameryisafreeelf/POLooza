#!/usr/bin/env python
# Cleaner mapper to drop write-in candidates' data.
# NOTE: still fixing ill-formed output.

import sys


for line in sys.stdin:
    key = line
    line = line.split(',')
    value = line[-4].lower()
    if value == 'true':
        value = 1
    else:
        value = 0
    print('{0}\t{1}'.format(key, value))
