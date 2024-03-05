# This program reads in a text file and outputs the number
# of e's it contains.
# Takes the filename from an argument on the command line
# e.g. python3 es.py example.txt

import sys      # used to take arguements in terminal
# https://docs.python.org/3/library/sys.html
# we gonna use sys.argv specifically

# open the file (example.txt) in read-only mode
with open(sys.argv[1], "r") as inf:
    # read entire file as a string
    contents = inf.read()

print(contents)