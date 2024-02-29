'''
This program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
'''

# get user input, save input as a string 
account_number = input("Please enter an 10 digit account number: ")

# create function to redact account number
def redact_acc_number(account_number):
    # strip spaces from input
    # string.replace() method replaces whatever is in the first argument with whatevers in the second argument
    account_number_without_spaces = account_number.replace(" ", "")

    # determine number of X to print
    number_of_Xs = len(account_number_without_spaces)-4

    # print redacted account number
    print('X' * number_of_Xs, account_number_without_spaces[-4:], sep="")

# call function
redact_acc_number(account_number)

'''
"strings are arrays" 
    - https://www.w3schools.com/python/python_strings.asp

Printed last 4 characters uses splicing:
    - https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/
    
    array[start:stop:step]

Array can be navigated using indices
    Arrays start at zero in python
    The below code prints the first character of the array
        print(account_number[0])

How to print last character of an array? negative indexing
 - https://www.askpython.com/python/list/negative-indexing

Removed space between Xs and the 4 numbers using sep=""
Example found here: 
    - https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

    print('X' * number_of_Xs, account_number[-4:], sep="")
    
'''