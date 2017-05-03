#!/usr/bin/python
# above is necessary for hadoop streaming

import sys


def run():
    for line in sys.stdin:
        data = line.strip().split(" ")
        if len(data) == 10:
            ip, identity_client, username_client, date, time_zone, http_method, page, http_protocol, status_code, object_size = data
            print "{0}\t{1}".format(page, 1)


if __name__ == '__main__':
    try:
        run()
    except Exception as e:
        import traceback, StringIO

        fakeeWriteable = StringIO.StringIO()

        traceback.print_exc(None, file=fakeeWriteable)
        msg = ""
        msg += "------------------------------------------------------\n"
        msg += "----theTraceback: -----------\n"
        msg += fakeeWriteable.getvalue() + "\n"
        msg += "------------------------------------------------------\n"

        sys.stderr.write(msg)

        raise e
