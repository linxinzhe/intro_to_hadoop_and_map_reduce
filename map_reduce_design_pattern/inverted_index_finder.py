#!/usr/bin/python
# above is necessary for hadoop streaming

import sys

word = "fantastic"

for line in sys.stdin:
    data_mapped = word.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue

    this_key, this_index = data_mapped

    if this_key == word:
        print this_index
