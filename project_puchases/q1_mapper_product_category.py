#!/usr/bin/python
# above is necessary for hadoop streaming

import sys

for line in sys.stdin:
    data = line.strip().split("\t")
    if len(data) == 6:
        data, time, store, item, cost, payment = data
        print "{0}\t{1}".format(item, cost)
