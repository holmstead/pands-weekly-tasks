'''
This program displays:
- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
'''

# https://numpy.org/doc/stable/index.html
from numpy import random
import numpy as np
# import submodule from matplotlib for plotting
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
Next we use normal() method on the "initialized generator object" to get a Gaussian distributiuon of random floats [1.0]
'''
# generate array of size 1000  
# loc is mean, scale is std deviation 
rand_array = rng.normal(loc=5.0, scale=2.0, size=1000)

# print the array to the console
#print(rand_array)

# test if mean and std dev are what required
print(f"Mean of distribution:\t\t {rand_array.mean()}")
print(f"Std deviation of distribution:\t {rand_array.std()}")


# set up the canvas
# (N, n) sets how many subplots: N row, n columns
fig, ax = plt.subplots(1, 1) 

# plot a histogram of the array [1.2][1.3]
ax.hist(rand_array, bins= 10, edgecolor='black', label='Normal Distribution')


'''
Now do the function plotting
Function:  h(x)=x3
'''

# creat dictionary for x and y vaolues
data = {'x':[], 'y':[]}

# calculate the function for x from zero to ten
for i in range(0, 10):
    # append to dictionary
    data['x'].append(i)
    data['y'].append(i ** 3)


# plot the function on the same axis as the histogram
ax.plot(data['x'], data['y'], color='blue', label='h(x) = x^3')

# add a legend to the figure
ax.legend()

# decorate plot
ax.set_xlabel('Values / x')
ax.set_ylabel('Frequency / h(x)')

# display figure containing histogram and plot
plt.show()


'''
References

[1.0] https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.normal.html#numpy.random.Generator.normal
[1.2] https://realpython.com/python-matplotlib-guide/
[1.3] https://matplotlib.org/stable/gallery/statistics/hist.html
'''