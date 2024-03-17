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

'''
That was the old 'RandomState' way using randint(), new way is 'Generator'
    - https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.Generator

Use default_rng() method 'random number generator' to generate a random ffloat which we will then use to produce useful distributions
    - https://numpy.org/doc/stable/reference/random/generator.html#numpy.random.default_rng

From the docs: "default_rng is the recommended constructor for the random number class Generator"
    - https://numpy.org/doc/stable/reference/random/generator.html

Returns an "initialized generator object".

You can give a seed number for pseudorandom numbers
'''
# use generator for random number, seeded by entropy from the operating system
rng = np.random.default_rng(seed=None)
print(rng)

'''
Next we use normal() method on the "initialized generator object" to get a Gaussian distributiuon of random floats
 - https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal
'''
# generate array of size 1000  
# loc is mean, scale is std deviation 
#rand_array = rng.normal(loc=5, scale=2.0, size=1000)

# try standard_normal()
rand_array = rng.standard_normal(mean=5, std=2, size=1000)

# print the array to the console
print(rand_array)

# test if mean and std dev are what i want
print(f"Mean of distribution:\t\t {rand_array.mean()}")
print(f"Std deviation of distribution:\t {rand_array.std()}")

# plot a histogram of the array
#  - https://realpython.com/python-matplotlib-guide/
#  - https://matplotlib.org/stable/gallery/statistics/hist.html
plt.hist(rand_array, bins= 10, edgecolor='black')

# decorate the plot
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Random Numbers')

# display teh plot
plt.show()