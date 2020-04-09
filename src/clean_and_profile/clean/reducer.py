#!/usr/bin/env python
# Cleaner reducer to drop write-in candidates.
# NOTE: still fixing ill-formed output.

import sys


for line in sys.stdin:
    line = line.strip()
    if not len(line):
        continue
    datum, is_writein = line.split('\t', 1)
    try:
        is_writein = int(is_writein)
    except ValueError:
        continue
    if not is_writein:
        print('{0}'.format(datum))
