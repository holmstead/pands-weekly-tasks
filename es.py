# This program reads in a text file and outputs the number
# of e's it contains.
# Takes the filename from an argument on the command line
# e.g. python3 es.py example.txt

import sys      # used to take arguements in terminal
# https://docs.python.org/3/library/sys.html
# we gonna use sys.argv specifically to pass in arguement

# create function to count instances of a given letter
def letter_count(inf, letter):
    # initialise variable to count instances
    letter_count = 0
    # create for loop to iterate through each line of textfile
    for line in inf:
        # uppercase and lowercase are different characters
        # make everything lowercase to make search easier
        line = line.lower()
        #print(line)
        # iterate over each character in each line
        for char in line:
        #print(char)
            # check if the character is e
            if (char == letter):
                # add to the letter_count variable
                letter_count += 1
    return letter_count

# Check if two arguements were passed in to python
# i.e. the script name 'es.py' and the textfile name
# 'example.txt'
# https://stackoverflow.com/questions/2626026/python-sys-argv-lists-and-indexes
if len(sys.argv) != 2:
    print("Usage: python es.py <filename>\nExiting.")
    # kill the program if we didnt get 2 args
    sys.exit(1)
else:
    try:
        with open(sys.argv[1], "r") as inf:     # [1]
            print(letter_count(inf, "e"))
    except FileNotFoundError:
        print("File not found.\nExiting.", end="\n")


'''
def check_args():
    if len(sys.argv) < 2:
        print("Usage: python es.py <filename>")
        print("Please try again.\nExiting.")
        # kill the program if we didnt get 2 args
        sys.exit(1)
    else:
        inf = sys.argv[1]
    return inf

inf = check_args()


# initialise empty variable to store the e count
e_count = 0

# try/except - try to open the given file
# if the file not found, message displayed to console
try:
    with open(sys.argv[1], "r") as inf:         #[1]
        # next check if the 2nd arguement was a textfile
        # check the extension, has to be .txt
        # https://stackoverflow.com/questions/5899497/how-can-i-check-the-extension-of-a-file

        if inf.endswith('.txt'):
            print("It's a text file.")
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
        else:
            print("It's not a text file.\nExiting.")
            sys.exit(1)
    print(f"Number of e's: {e_count}")

except FileNotFoundError:
    print("File not found.\nExiting.", end="\n")

'''




'''
[1] Open the file (example.txt) in read-only mode
I'm using the "with open" way as it automatically 
closes the file after.
- https://www.freecodecamp.org/news/with-open-in-python-with-statement-syntax-example/
Lets open the file and use some built-in string methods
- https://docs.python.org/3/library/stdtypes.html#string-methods

'''




