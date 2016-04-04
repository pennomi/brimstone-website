import sys

from mudblood.mudblood import render_string

infilepath, w, h, outfilepath = sys.argv[1:]
with open(infilepath) as infile:
    template_string = infile.read()
render_string(template_string, w, h, outfilepath)
