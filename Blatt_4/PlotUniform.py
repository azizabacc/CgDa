#!/usr/bin/python

# -------- PlotUniform.py ------------------------------------------
# Description: example showing
#              - how to define and fill a histogram with
#                 uniform random numbers
#              - use matplotlib to plot histogram and function
#              - calculate statistical information from histogram array
#
# Author:      G. Quast   Dec. 2013
# dependencies: PYTHON v2.7, numpy, matplotlib.pyplot
# last modified:
# --------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


# define a function (straight line)
def fpol1(x, a=1., b=0.):
    return (a*x + b)


def histstat(binc, bine):
    # calculate mean of a histogram with bincontents binc and bin edges bine
    bincent = (bine[1:]+bine[:-1])/2    # determine bincenters
    mean = sum(binc*bincent)/sum(binc)
    rms = np.sqrt(sum(binc*bincent**2)/sum(binc) - mean**2)
    return mean, rms


# generate some data
ndat = 1000
randat = np.random.rand(ndat)

# plot data as histogram
nbin = 20
binc, bine, patches = plt.hist(randat, nbin, normed=0,
                               facecolor='g', log=False, alpha=0.5)
# make plot nicer:
plt.xlabel('random number')  # axis labels
plt.ylabel('frequency')
plt.title('Histogram of uniform random numbers')  # title

# calculate histogram mean and rms from histogram array
hmean, hsigma = histstat(binc, bine)    # get mean and RMS
print "mean, sigma = ", hmean, hsigma

# plot
a = 0
b = np.float(ndat)/np.float(nbin)
x = np.arange(0, 1., 0.005)
plt.plot(x, fpol1(x, a, b), 'b-')             # plot function
plt.text(0.5, b*1.1, r'constant function', fontsize=14, color='b')

plt.grid(True)  # show a grid for orientation
plt.show()      # now display everything on the screen
