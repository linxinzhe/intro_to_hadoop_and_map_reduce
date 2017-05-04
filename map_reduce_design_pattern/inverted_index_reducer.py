#!/usr/bin/python
# above is necessary for hadoop streaming

import sys


def run():
    oldKey = None
    index_list = []

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        this_key, this_index = data_mapped

        if this_key != oldKey:
            if oldKey:
                print "{0}\t{1}".format(oldKey, index_list)
            oldKey = this_key
            index_list = []
        else:
            index_list.append(this_index)


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
