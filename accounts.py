# theis program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

# get user input, saves input as a string 
account_number = input("Please enter an 10 digit account number: ")

print(account_number)

# first, attempt to print only last 4 characters
# "strings are arrays" - https://www.w3schools.com/python/python_strings.asp

# array can be navigated using indices
# arrays start at zero in python
# the below code prints the first character of the array
print(account_number[0])

# how to print last character of an array?