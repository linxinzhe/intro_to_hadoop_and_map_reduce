#!/usr/bin/python
# above is necessary for hadoop streaming

import csv
import string
import sys


def run():
    is_first_line = True
    tab_count = 0

    reader = csv.reader(sys.stdin, delimiter="\t")
    specials = ',.!?:;"()<>[]#$=-/'
    trans = string.maketrans(specials, ' ' * len(specials))

    for line in reader:
        if is_first_line:
            tab_count = len(line)
            is_first_line = False
            continue

        if len(line) == tab_count:
            node_id, body = line[0], line[4]
            body = body.translate(trans)
            words = body.strip().split()
            for word in words:
                print "{0}\t{1}".format(word.lower(), node_id)


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
