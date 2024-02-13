# this program asks the user to input any positive integer and outputs the successive values of the following calculation:
# the program calculates the next value by taking the current value and, if it is even, divides it by two, but if it is odd, multiplys it by three and adds one
# the program ends if the current value is one

# get user input, saves input as an 'int' type
number_to_check = int(input("Please enter a positive integer: "))

# the modulo operator can be used to determine if a given integer is even or odd
# https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/

while number_to_check != 1:
    if ((number_to_check % 2) == 0):
        # "positive integer" is divided by 2 and the 
        # remainder is returned, if its zero then it is
        # an even number
        print(f'{number_to_check} is even')
        number_to_check = (number_to_check / 2)
        print(f'divided by 2 = {number_to_check}')
    else:
        print(f'{number_to_check} is odd')
        number_to_check = (number_to_check * 3) + 1
        print(f'multiplied by 3 and add 1 = {number_to_check}')

