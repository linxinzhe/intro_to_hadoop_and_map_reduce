#!/usr/bin/python
# above is necessary for hadoop streaming

import sys


def run():
    oldKey = None
    count = 0

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisCount = data_mapped

        if thisKey != oldKey:
            if oldKey:
                print "{0}\t{1}".format(oldKey, count)
            oldKey = thisKey
            count = 1
        else:
            count += 1


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
