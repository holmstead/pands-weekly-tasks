# get user input, saves input as a string 
amount1 = input("Enter amount1 (in cent): ")
amount2 = input("Enter amount2 (in cent): ")

# you cant do arithmetic on strings, so convert string inputs to integers
# originally i used floats, but the math gets tricky with floats
amount1_int = int(amount1)
amount2_int = int(amount2)

# maybe next modify script to take input as integers directly
# add exception handling too, in case something other than integers entered

# add the two amounts together
cents = amount1_int + amount2_int

# convert cents to euros
euros = cents / 100

# fstrings seems to be a newer way of formatting outputs
# note that the euro sign is in Unicode (\u20AC)
# https://docs.python.org/3/howto/unicode.html
# https://home.unicode.org/
# take a look at using \N{name} eg \N{euro sign}
# note that euros is rounded to 2 decimal places using .2f
print(f'The sum of these is \u20AC{float(euros):.2f}')