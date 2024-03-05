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
    # print entrie contents in one go
    print(contents)

# lets open the file and use some built-in string methods
# https://docs.python.org/3/library/stdtypes.html#string-methods
with open(sys.argv[1], "r") as inf:
    # read file line by line
    for line in inf:
        # E/e are two different characters
        # make everything lowercase to make search easier
        line = line.lower()
        print(line)

        # iterate over each character in each line
        for char in line:
            print(char)


