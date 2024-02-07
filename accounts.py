# theis program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# get user input, saves input as a string 
account_number = input("Please enter an 10 digit account number: ")

#print(account_number)

# first, attempt to print only last 4 characters
# "strings are arrays" - https://www.w3schools.com/python/python_strings.asp

# array can be navigated using indices
# arrays start at zero in python
# the below code prints the first character of the array
#print(account_number[0])

# how to print last character of an array? negative indexing
# https://www.askpython.com/python/list/negative-indexing

# print last character of the array
#print(account_number[-1])

# print last 4 characters now
#print(account_number[-4], account_number[-3], account_number[-2], account_number[-1])

# that printed the last 4 numbers but with spaces between, i want to remove spaces
# found example here: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/

#print(account_number[-4], account_number[-3], account_number[-2], account_number[-1], sep="")

# now print a load of Xs before the last 4 numbers
# its 6 Xs in this case, but would be better to count the array length and subtract 4 from it
number_of_xs = len(account_number)-4
#print('X' * number_of_xs)

# combine the Xs and the last 4 digits
print('X' * number_of_xs, account_number[-4], account_number[-3], account_number[-2], account_number[-1], sep="")