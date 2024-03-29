'''
A square root function using Newtons method.
Newtons method is an iterative method which finds roots of functions. It draws tangent lines and tries to get to zero through iteration.

See Equation 4.9.1 in link below:

    - https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/04%3A_Applications_of_Derivatives/4.09%3A_Newtons_Method
    
See the square root example on Wikipedia:

    - https://en.wikipedia.org/wiki/Newton's_method#Square_root

we can write x = sqrt(a)

so x^2 = a 

or write it as x^2 - a = 0

derivative of that is 2x

perfomr the math on the guess

then use the result to put back into the equation

compare the new result with the first result

each time the difference will get smaller and smaller as it converges toward the correct answer

closer to zero is closer to correct answer

'''

# define function
def get_square_root(a):
    # You have to give it a guess number to start with 
    guess = 2

    # we need a loop to iterate
    while True:
        # apply the formaula
        y = guess - (guess**2 - a) / (2 * guess)
        #print(y)

        # check for convergence to zero
        diff = guess - y
        #print(f"Difference: {diff}")
        #print(abs(diff))
        #print()

        # check convergence precision
        if abs(diff) < 0.00001:
            # exit the loop by returning y
            print(f"the square root is approximately: {y}")
            return y

        # y now needs to be the new guess in the next iteration
        guess = y
    

# call teh function
get_square_root(67)

# check the result
import math
print(f"Built in method says: {math.sqrt(67)}")
