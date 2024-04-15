'''
This program displays:
- a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
- and a plot of the function  h(x)=x3 in the range 0 to 10, 
on the one set of axes.
'''

from numpy import random
import numpy as np
# import submodule from matplotlib for plotting
import matplotlib.pyplot as plt


# use generator for random number, seeded by entropy from the operating system
rng = np.random.default_rng(seed=None)
print(rng)

# next we use normal() method on the "initialized generator object" to get a Gaussian distributiuon of random floats
# generate array of size 1000  
# loc is mean, scale is std deviation 
rand_array = rng.normal(loc=5.0, scale=2.0, size=1000)

# print the array to the console
#print(rand_array)

# test if mean and std dev are what required
print(f"Mean of distribution:\t\t {rand_array.mean()}")
print(f"Std deviation of distribution:\t {rand_array.std()}")

# create dictionary for x and y values
data = {"x":[], "y":[]}

# calculate the function for x from zero to ten
for i in range(0, 10):
    # append to dictionary
    data["x"].append(i)
    data["y"].append(i ** 3)


# plot the function h(x)=x3 and histogram on the same axis
# XKCD style plots
with plt.xkcd():
    # set up the figure 
    # (N, n) N rows, n columns
    fig, ax = plt.subplots(1, 1) 

    # plot a histogram of the array
    # labels are for the legend
    ax.hist(rand_array, bins= 10, edgecolor="black", label="Normal Distribution")

    # plot the line on the same axes
    ax.plot(data["x"], data["y"], color="blue", label="h(x) = x^3")
    
    # add a legend to the figure
    ax.legend()

    # decorate plot
    ax.set_xlabel("Values / x")
    ax.set_ylabel("Frequency / h(x)")

    # set x-axis limits as xkcd is not very consistent with its x-limits
    ax.set_xlim(0, 10)
    
# auto adjust layout
plt.tight_layout()

# display figure containing histogram and plot
plt.show()
plt.close()