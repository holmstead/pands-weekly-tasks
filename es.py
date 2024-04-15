# This program reads in a text file and outputs the number
# of e's it contains.
# Takes the filename from an argument on the command line
# e.g. python3 es.py example.txt

import sys      # used to take arguements in terminal


# define variable with the letter to count
letter = "e"

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


# create main() function
def main():
    # Check if two arguements were passed in to python
    # i.e. the script name 'es.py' and the textfile name 'example.txt'
    if len(sys.argv) != 2:
        print("Usage: python es.py <filename>\nExiting.")
        # kill the program if we didnt get 2 args
        sys.exit(1)
    else:
        try:
            with open(sys.argv[1], "r") as inf:
                print(letter_count(inf, letter))
        except FileNotFoundError:
            print("File not found.\nExiting.", end="\n")


if __name__ == "__main__":
    main()