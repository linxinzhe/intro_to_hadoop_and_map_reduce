#!/usr/bin/python
# above is necessary for hadoop streaming

import sys
from datetime import datetime


def run():
    total_sales_list = [0] * 7
    total_sales_count = [0] * 7

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        this_key, this_sales = data_mapped

        weekday = datetime.strptime(this_key, "%Y-%m-%d").weekday()

        total_sales_list[weekday] += float(this_sales)
        total_sales_count[weekday] += 1

    for i in range(len(total_sales_list)):
        sales = total_sales_list[i]
        count = total_sales_count[i]
        print "weekday", i + 1, "total sales:", sales, "mean sales:", sales / count


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
