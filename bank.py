# get user input, saves input as a string 
amount1 = input("Enter amount1 (in cent): ")
amount2 = input("Enter amount2 (in cent): ")

# you cant do arithmetic on strings, so convert string inputs to floats
amount1_float = float(amount1)
amount2_float = float(amount2)

# add the two amounts together
cents = amount1_float + amount2_float

# convert cents to euros.
euros = cents / 100.0

# fstrings seems to be a newer way of formatting outputs
# note that the euro sign is in Unicode (\u20AC)
# https://docs.python.org/3/howto/unicode.html
# https://home.unicode.org/
# take a look at using \N{name} eg \N{euro sign}
print(f'The sum of these is \u20AC{float(euros):.2f}')