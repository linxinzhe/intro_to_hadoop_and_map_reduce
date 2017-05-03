#!/usr/bin/python

import sys

totalCount = 0
HIT_IP = "10.99.99.186"

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCount = data_mapped

    if thisKey == HIT_IP:
        totalCount += int(thisCount)

print "Hit IP:", HIT_IP, " Count:", totalCount
