#!/usr/bin/python 

# -------- basicDistributions.py ------------------------------------------
# Description: example showing 
#              - how to define a function
#              - use matplotlib to plot histograms and function
# Author:      G. Quast   Dec. 2013
# dependencies: PYTHON v2.7, numpy, scipy.special, matplotlib.pyplot 
# last modified: 
#  
#--------------------------------------------------------------

import numpy as np, matplotlib.pyplot as plt, scipy.special as sp

#Binomial distribution
def fBinomial(x,n,p):
  k=np.around(x)
  return sp.binom(n,k) * p**k * (1.-p)**(n-k)

# Poisson distribution
def fPoisson(x,mu):
  k=np.around(x)
  return (mu**k)/np.exp(mu)/sp.gamma(k+1.)

# Gauss distribution
def fGauss(x,mu=0.,sigma=1.):
    return (np.exp(-(x-mu)**2/2./sigma**2)/np.sqrt(2.*np.pi)/sigma)

# ---------------------------------------------------------------

# plot basic distributions
mu=50.
sigma=np.sqrt(mu)
x = np.arange(20, 80., 0.1)
fig,ax=plt.subplots(1,1)
ax.set_ylim(0.,0.065)
ax.plot(x, fGauss(x,mu,sigma), 'r-')   
ax.plot(x, fPoisson(x,mu), 'b-')       
p=0.1
n=mu/p
ax.plot(x, fBinomial(x,n,p), 'g-') 
#     make plot nicer:
ax.set_xlabel('k') # axis labels
ax.set_ylabel('probability density')

fig.text(0.58, 0.71, \
r'$-\,f(x)=\frac{1}{\sqrt{2\,\pi}\sigma}\,\exp{\left(\frac{-(x-\mu)^2}{2\sigma^2}\right)}$',\
fontsize=14, color='r')

fig.text(0.58, 0.78, \
            r'$-\,P(k;\mu)=\frac{\mu^k}{k!} \, \exp{-\mu}$',\
fontsize=14, color='b')

fig.text(0.55, 0.85, \
r'$-\,P(k;n,p)= \binom{n}{k} \, p^k (1-p)^{n-k}~,k=1,\ldots,n$',\
fontsize=14, color='g')

fig.text(0.15, 0.85, \
         r'$\mu=50, \, \, p=0.1, n=\mu/p, \, \sigma=\sqrt{\mu}$',\
fontsize=14)

# finally, show the plots on the screen
plt.show()
