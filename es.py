# This program reads in a text file and outputs the number
# of e's it contains.
# Takes the filename from an argument on the command line
# e.g. python3 es.py example.txt

import sys      # used to take arguements in terminal
# https://docs.python.org/3/library/sys.html
# we gonna use sys.argv specifically to pass in arguement

# initialise empty variable to store the e count
e_count = 0

try:
    with open(sys.argv[1], "r") as inf:         #[1]
    # read file line by line
        for line in inf:
            # E/e are two different characters
            # make everything lowercase to make search easier
            line = line.lower()
            #print(line)

            # iterate over each character in each line
            for char in line:
                #print(char)
                # check if the character is e
                if (char == "e"):
                    # add to the e_count variable
                    e_count += 1
    print(e_count)

except FileNotFoundError:
    print("File not found, try again.", end="\n")

'''
[1] Open the file (example.txt) in read-only mode
I'm using "with open" way as it automatically 
closes the file after.
- https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
Lets open the file and use some built-in string methods
- https://docs.python.org/3/library/stdtypes.html#string-methods
'''




