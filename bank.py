'''
This program prompts the user and reads in two money amounts (in cent), adds the two amounts, then prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
'''

import sys

# get user input, saves input as a string 
amount1 = input("Enter amount1 (in cent): ")
amount2 = input("Enter amount2 (in cent): ")

# check if an integer was entered or not
# called exception handling
try:
    int_value = int(amount1) and int(amount2)
    print("Inputs are an integer")
except ValueError:
    print("Please enter valid integers.")
    sys.exit(1)

# create function to add cents then convert to euro
def add_cents(amount1_int, amount2_int):
    # add the two amounts together
    # convert strings to integers first
    cents = int(amount1) + int(amount2)

    # convert cents to euros
    # convert integer to float for decimal places
    euros = float(cents / 100)

    return euros


# print result using fstrings
# unicode used for the euro sign
# call the function inside the print statement
#print(f'The sum of these is \u20AC{add_cents(amount1, amount2)}')

