'''
This program prompts the user and reads in two money amounts (in cent), adds the two amounts, then prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
'''

# get user input, saves input as a string 
amount1 = input("Enter amount1 (in cent): ")
amount2 = input("Enter amount2 (in cent): ")

# create function to add cents then convert to euro
def add_cents(amount1_int, amount2_int):
    # add the two amounts together
    # convert strings to integers first
    cents = int(amount1) + int(amount2)

    # convert cents to euros
    euros = cents / 100

    #print(f'The sum of these is \u20AC{float(euros):.2f}')
    return euros

#add_cents(amount1, amount2)

# print result using fstrings
# unicode used for the euro sign
# call the function inside the print statement
print(f'The sum of these is \u20AC{float(add_cents(amount1, amount2)):.2f}')

