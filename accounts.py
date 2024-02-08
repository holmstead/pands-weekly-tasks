# this program reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

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

# print last 4 characters now, updated to use splicing
# https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/
# array[start:stop:step]
#print(account_number[-4:])

# now print a load of Xs before the last 4 numbers
# its 6 Xs in this case, but would be better to count the array length and subtract 4 from it
number_of_xs = len(account_number)-4
#print('X' * number_of_xs)

# combine the Xs and the last 4 digits
# remove space between Xs and the 4 numbers using sep=""
# found sep="" example here: https://www.geeksforgeeks.org/gfact-50-python-end-parameter-in-print/
print('X' * number_of_xs, account_number[-4:], sep="")

# if i put a space in the input it gets put in the output as well
# next step would be to make sure to remove any spaces so that we dont get something like XXXXXX8 90
# from the labs: rawString.strip().lower()
# called normalisation
# i think it only works for leading and trailing spaces though
# string.replace() method looks good for this
# whatever is in the first argument gets replaced with whats in the second argument
account_number_without_spaces = account_number.replace(" ", "")
print(account_number_without_spaces)
