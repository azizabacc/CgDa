#!/usr/bin/python
#
# -------- Covariance.py ---------------------------------------
# Description: repeatedly fill a histogram with 10000 uniformly
#              distributed random numbers and study distributions
#              and correlations of bin contents.
# Author:      G. Quast   Nov. 2013
# dependencies: PYTHON v2.7, numpy, matplotlib.pyplot
# last modified:
# ---------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp
import Histogram


# Verteilungen aus Vorlesungsbeispielen
# ---------------------------------------


# Binomial distribution
def fBinomial(x, n, p):
    k = np.around(x)
    return sp.binom(n, k) * p**k * (1.-p)**(n-k)


# Poisson distribution
def fPoisson(x, mu):
    k = np.around(x)
    return (mu**k)/np.exp(mu)/sp.gamma(k+1.)


# Gauss distribution
def fGauss(x, mu=0., sigma=1.):
    return (np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)


# ---------------------------------------------------------------
# Aufgabenteil:
###############
#
def cov(x1, x2):
    cov = 0
    cor = 0
    return cov, cor


# ------------------------------------------------------------
# 1. generate uniform distributions
# -------------------------------------------------------------
N = 100  # 2000
nexp = 10000
hbins = np.arange(0, 6)  # hbins=np.arange(0,101)
nbins = len(hbins)-1

b1 = np.zeros(nexp)
b2 = np.zeros(nexp)
b3 = np.zeros(nexp)
b4 = np.zeros(nexp)
b5 = np.zeros(nexp)
# loop over experiments
for i in range(nexp):
    # generate and histogram data
    x=np.random.rand(N)
    bc, be = np.histogram(x, nbins)
    # store bin contents
    b1[i]=bc[0]
    b2[i]=bc[1]
    b3[i]=bc[2]
    b4[i]=bc[3]
    b5[i]=bc[4]
#             end loop over experiments





# statistical analyis of bin contents
b1hist=np.histogram(b1)
b2hist=np.histogram(b2)
b3hist=np.histogram(b3)
b4hist=np.histogram(b4)
b5hist=np.histogram(b5)

#
def mean(a):
  return np.sum(a)/len(a)

def variance(a):
    v=np.sum((a-mean(a))**2)/len(a)
    return v

def sigma(a):
    s= np.sqrt(variance(a))
    return s

#aufgabenteil b
def cov(a,b):
    return (1./(len(a))*np.sum((a-mean(a))*(b-mean(b))))
            
def kore(a,b):
    return (cov(a,b)/(sigma(a)*sigma(b)))

print b2
#  print covariance of b2 and b4
kore24=kore(b4,b2)
print(' kore: %f'%kore24)

# two-dimensional histogram of contents in bin 2 and 4
plt.hist2d(b2,b4, normed=1)
plt.colorbar()
#aufgabenteil b ende


#aufgabwenteil a
'''
plt.hist(b2, normed=1, facecolor='g', log=False, alpha=0.5)
mu = mean(b2)
sigma = np.sqrt(variance(b2))
print mu
print sigma
a = np.arange(0, 40, 0.1)
plt.plot(a, fGauss(a,mu,sigma), 'r-')

'''

# show plot of 1/2 d distribution

plt.show()