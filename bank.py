'''
This program prompts the user and reads in two money amounts (in cent), add the two amounts, then prints out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 
'''

# get user input, saves input as a string 
amount1 = input("Enter amount1 (in cent): ")
amount2 = input("Enter amount2 (in cent): ")

# create function to add cents and convert to euro
def add_cents(amount1_int, amount2_int):
    # add the two amounts together
    # convert strings to integers first
    cents = int(amount1) + int(amount2)

    # convert cents to euros
    euros = cents / 100

    # print result using fstrings
    # unicode used for the euro sign
    print(f'The sum of these is \u20AC{float(euros):.2f}')

add_cents(amount1, amount2)


'''
fstrings seems to be a newer way of formatting outputs.
Note that the euro sign is in Unicode (\u20AC)
- https://docs.python.org/3/howto/unicode.html
- https://home.unicode.org/
Take a look at using \N{name} eg \N{euro sign}
Note that euros is rounded to 2 decimal places using .2f

Should add exception handling, in case unexpected data types entered.
'''