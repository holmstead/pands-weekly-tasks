'''
This program reads in a 10 character account number and 
outputs the account number with only the last 4 digits 
showing (and the first 6 digits replaced with Xs).
'''

# create function to redact account number
# defaulted the function to disply 4 last digits
def redact_number(acc, visible_digits=4):
    # strip spaces from input
    # string.replace() method replaces whatever is in 
    # the first argument with whatevers in the second
    # argument
    acc_without_spaces = acc.replace(" ", "")
    # determine number of X to print
    number_of_Xs = len(acc_without_spaces) - visible_digits
    # print redacted account number
    # use slicing: array[start:stop:step]
    print('X' * number_of_Xs, acc_without_spaces[-visible_digits::], sep="")

# get user input, save input as a string 
acc = input("Please enter an 10 digit account number: ")

# call function
redact_number(acc)