#!/usr/bin/python
# above is necessary for hadoop streaming

import sys

for line in sys.stdin:
    data = line.strip().split(" ")
    if len(data) == 10:
        ip, identity_client, username_client, date, time_zone, http_method, page, http_protocol, status_code, object_size = data
        print "{0}\t{1}".format(page, 1)
