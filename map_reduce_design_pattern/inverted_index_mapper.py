#!/usr/bin/python
# above is necessary for hadoop streaming

import csv
import re
import sys


def run():
    is_first_line = True
    tab_count = 0
    still_one_line = ""

    reader = csv.reader(sys.stdin, delimiter="\t")
    for line in reader:
        if is_first_line:
            tab_count = len(line)
            is_first_line = False
            continue

        if len(line) == tab_count:
            node_id, body = line[0], line[4]
            words = set(re.split("[^A-Za-z]+", body.lower()))
            for word in words:
                if word:
                    print "{0}\t{1}".format(word, node_id)


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
