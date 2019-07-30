from sys import stdin

for line in stdin:
    if len(line.split('\t')) == 2:
        print(line)

