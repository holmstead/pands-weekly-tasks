# This program asks the user to input any positive 
# integer and outputs the successive values of the 
# following calculation;
# The program calculates the next value by taking 
# the current value and, if it is even, divides it 
# by two, but if it is odd, multiplys it by three and 
# adds one.
# The program ends if the current value is one

# Get user input, saves input as an 'int' type
number_to_check = int(input("Please enter a positive integer: "))

# The modulo operator can be used to determine if a given integer is even or odd
# https://www.freecodecamp.org/news/the-python-modulo-operator-what-does-the-symbol-mean-in-python-solved/

# Start a while loop (sentinel controlled loop)that 
# Will run only if n does not equal one
while number_to_check != 1:
    # Check if the remainder of the number when divided 
    # by two is equal to zero
    if number_to_check % 2 == 0: 
        # If the remainder is zero then it was
        # an even number
        #print(f'{number_to_check} is even')
        # Now do the even number math on it
        number_to_check = (number_to_check / 2)
        # print the result of the math to console
        #print(f'divided by 2 = {number_to_check}')
        # Use the 'end' parameter of the print function
        # to print across console
        print(int(number_to_check), end=' ')
    else:
        #print(f'{number_to_check} is odd')
        number_to_check = (number_to_check * 3) + 1
        #print(f'multiplied by 3 and add 1 = {number_to_check}')
        # Use the 'end' parameter of the print function
        # to print across console
        print(int(number_to_check), end=' ')
