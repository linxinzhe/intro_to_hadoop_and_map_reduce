#!/usr/bin/python
# above is necessary for hadoop streaming

import re
import sys


def run():
    is_first_line = True
    tab_count = 0
    still_one_line = ""

    for line in sys.stdin:
        if is_first_line:
            tab_count = len(line.strip().split("\t"))
            is_first_line = False
            continue

        still_one_line += line.strip()

        if line.strip().endswith('\"'):
            data = still_one_line.strip().split("\t")

            if len(data) == tab_count:
                node_id, body = data[0], data[4]
                words = set(re.split("[^A-Za-z]+", body.lower()))
                for word in words:
                    if word:
                        print "{0}\t{1}".format(word, node_id)
            still_one_line = ""


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
