#!/usr/bin/python
import sys

HIT_PAGE = "/assets/js/the-associates.js"
hit_page_count = 0
for line in sys.stdin:
    page = line.strip()  # get rid of "\n"
    if page:
        if HIT_PAGE == page:
            hit_page_count += 1

print "Hit Page:{}\tCount:{}".format(HIT_PAGE, hit_page_count)
