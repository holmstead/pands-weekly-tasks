'''
This program prompts the user and reads in two money amounts (in cent), adds the two amounts, then prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
'''

import sys

# get user input, saves input as a string 
amount1 = input("Enter amount1 (in cent): ")
amount2 = input("Enter amount2 (in cent): ")

'''
Check if an integer was entered or not.
Called exception handling.
See below for Exception handling examples using while loops, and handling ValueErrors
 - https://www.freecodecamp.org/news/exception-handling-python/

ValueError is a built-in exception in python:
 - https://docs.python.org/3/library/exceptions.html
A ValueError is "raised when an operation or function receives an argument that has the right type but an inappropriate value, and the situation is not described by a more precise exception such as IndexError."
'''

try:
    int_value = int(amount1) and int(amount2)
    #print("Inputs are integers")
except ValueError:
    print("Please enter valid integers.\nExiting")
    sys.exit(1)

# create function to add cents then convert to euro
def add_cents(amount1_int, amount2_int):
    # add the two amounts together
    # convert strings to integers first
    cents = int(amount1) + int(amount2)

    # convert cents to euros
    # convert integer to float for decimal places
    euros = float(cents / 100)

    # return a variable containing the converted answer
    return euros


# print result using fstrings
# unicode used for the euro sign
# call the function inside the print statement
print(f'The sum of these is \u20AC{add_cents(amount1, amount2)}')

