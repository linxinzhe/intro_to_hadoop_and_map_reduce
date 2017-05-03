#!/usr/bin/python
import sys

# only work for test
if __name__ == "__main__":
    a = """
/
/favicon.ico
/
/assets/js/lowpro.js
/assets/css/reset.css
/assets/css/960.css
/assets/css/the-associates.css
/assets/js/the-associates.js
/assets/js/lightbox.js
/assets/img/search-button.gif
    """
    import StringIO

    stringio = StringIO.StringIO(a)
    sys.stdin = stringio

HIT_PAGE = "/"
hit_page_count = 0
for line in sys.stdin:
    page = line.strip()  # get rid of "\n"
    if page:
        if HIT_PAGE == page:
            hit_page_count += 1

print "Hit Page:{}\tCount:{}".format(HIT_PAGE, hit_page_count)
