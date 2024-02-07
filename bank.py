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
print(f'The sum of these is \u20AC{float(euros):.2f}')