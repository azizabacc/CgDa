#!/usr/bin/python 

# -------- Gauss.py ------------------------------------------
# Description: example showing 
#              - how to define a function
#              - generate (Gaussian) random numbers
#              - generate a histogram
#              - use matplotlib to plot histogram and function
# Author:      G. Quast   Apr. 2016
# dependencies: PYTHON v2.7, numpy, matplotlib.pyplot 
# last modified: 
#--------------------------------------------------------------

'''
Fragen Tutor:
wieso war sigma auf 1s und nicht nur auf 1 unter was bewirkt dass?
'''


import numpy as np
import matplotlib.pyplot as plt
 
# define a function (Gauss distribution)
def fgauss(a, mu, sigma):
    return (np.exp(-(a-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)

#set parameters for Gaussdistribtion
mu = 2.
sigma = 1.  # 1s ??

# generate random Gaussian numbers with mean 0 and variance 1
data =sigma* np.random.randn(100)+mu

# Aufgabenteil 3.3b
for i in range(1000):
    x =sigma* np.random.normal(9)+mu
    m =np.sum(x)/9
    np.histogram=(m)
print(m)

# plot data as histogram 
n, bins, patches = plt.hist(data, normed=1, facecolor='g', log=False, alpha=0.5) # plot data

# make plot nicer:
# axis labels
plt.xlabel('x') 
plt.ylabel('probability density')
# title
plt.title('Histogram of Gauss distribution')

# plot Gauss distraibution
#x = np.arange(-4., 4., 0.1)
#plt.plot(x, fgauss(x,mu,sigma), 'r-')             # plot function 

# a nicely type-set formula of the function
plt.text(1, 0.4, 
         r'$f(x) = \frac{1}{\sqrt{2\pi}\sigma}\,\exp{\left(\frac{-(x-\mu)^2}{2\sigma^2}\right)}$',
         fontsize=14, color='b')

plt.grid(True) # show a grid for orientation 
plt.show()     # now display everything on the screen

