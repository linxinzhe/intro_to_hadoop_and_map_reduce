#!/usr/bin/python
# above is necessary for hadoop streaming

import sys

totalCount = 0
HIT_PAGE = "/assets/js/the-associates.js"

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    thisKey, thisCount = data_mapped

    if thisKey == HIT_PAGE:
        totalCount += int(thisCount)

print "Hit Page:", HIT_PAGE, " Count:", totalCount
