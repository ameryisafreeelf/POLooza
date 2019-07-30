"""Map Reddit timestamp to year of post."""

from sys import stdin

SECONDS_PER_YEAR = 31556926

for line in stdin:
    line = line.split('\t')
    if len(line) != 6:
        continue
    docid = line[0]
    try:
        seconds = float(line[4])
    except:
        continue
    year = int(1970 + seconds / SECONDS_PER_YEAR)
    print('{0}\t{1}'.format(docid, year))

