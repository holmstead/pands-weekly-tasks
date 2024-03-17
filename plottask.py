'''
This program displays:
- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
'''

# shttps://numpy.org/doc/stable/index.html
from numpy import random
import numpy as np
#
import matplotlib.pyplot as plt

# genertae an 1-D array of size 1000, containing numbers up to 100
#  - https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html
rand_array = random.randint(100, size=(1000))
#print(rand_array)

# use default_rng() function
# random number generator to produce useful distributions
#  - https://numpy.org/doc/stable/reference/random/generator.html
#  - https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal
# you can give a seed number
rng = np.random.default_rng(seed=None)
# loc is mean, scale is std deviation 
rand_array = rng.normal(loc=5, scale=1.0, size=1000)

# try standard_normal()
#rand_array = rng.standard_normal(1000)

# print the array to the console
print(rand_array)

# test if mean and std dev are what i want
print(rand_array.mean())

# plot a histogram of the array
#  - https://realpython.com/python-matplotlib-guide/
#  - https://matplotlib.org/stable/gallery/statistics/hist.html
plt.hist(rand_array, bins= 10, edgecolor='black')


# display teh plot
plt.show()