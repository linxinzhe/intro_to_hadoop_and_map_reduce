#!/usr/bin/python
# above is necessary for hadoop streaming

import sys

d = dict()
for line in sys.stdin:
    key_value = line.strip().split("\t")
    if key_value[0] and key_value[1]:
        d[key_value[0]] = int(key_value[1])

sorted_list = sorted(d, key=d.get, reverse=True)[:3]

for item in sorted_list:
    print item, d[item]
