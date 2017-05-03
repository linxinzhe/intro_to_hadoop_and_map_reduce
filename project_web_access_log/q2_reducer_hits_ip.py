#!/usr/bin/python
# above is necessary for hadoop streaming

import sys


def run():
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
