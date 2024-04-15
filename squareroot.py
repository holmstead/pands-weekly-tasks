'''
A square root function using Newtons method.
Newtons method is an iterative method which finds roots 
of functions. It draws tangent lines and tries to get to 
zero through iteration.
'''

# create function to read integer from user, using
# exception handling 
def read_num():
    # initalise the variable, leave empty with False
    num = False
    # initiate while loop for try/except exception handling
    while (num == False):
        # try to get an int from user
        try:
            num = int(input("Enter an integer to determine the square root: "))
        # if you didnt get an int, we go around the while
        # loop again
        except ValueError:
            print("That was not a valid integer.", end=" ")
    return num

# define function to determine square root
def get_square_root(a):
    # You have to give it a guess number to start with 
    guess = a
    # we need a loop to iterate
    while True:
        # apply the formaula
        y = guess - (guess**2 - a) / (2 * guess)
        #print(y)
        # check for convergence to zero
        diff = guess - y
        #print(abs(diff))
        # check convergence precision
        if abs(diff) < 0.00001:
            # exit the while loop by returning y
            print(f"The square root is approximately: {y}")
            return y
        # y now needs to be the new guess in the next iteration
        guess = y
    
# call function to get number from user
num = read_num()

# call the function
get_square_root(num)

# check the result
import math
print(f"Built in method says: {math.sqrt(num)}")
