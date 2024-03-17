'''
This program displays:
- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
'''

from numpy import random

# genertae an array of size 1000, containing numbers up to 100
rand_array = random.randint(100, size=(1000))

print(rand_array)