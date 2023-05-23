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
import matplotlib.animation as anim, sys

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
x = np.arange(0., 60., 0.1)
fig=plt.figure(1,figsize=(7.5,7.5))
ax=fig.add_subplot(1,1,1)
ax.set_ylim(0.,0.3)
ax.set_xlabel('$\\mu$') # axis labels
ax.set_ylabel('probability(-density)')

fig.text(0.58, 0.71, \
r'$-\,f(x)=\frac{1}{\sqrt{2\,\pi}\sigma}\,\exp{\left(\frac{-(x-\mu)^2}{2\sigma^2}\right)}$',\
     fontsize=14, color='r')
fig.text(0.58, 0.78, \
            r'$-\,P(k;\mu)=\frac{\mu^k}{k!} \, \exp{-\mu}$',\
     fontsize=14, color='b')
fig.text(0.55, 0.85, \
r'$-\,B(k;N,p)= \binom{N}{k} \, p^k (1-p)^{N-k}~,k=1,\ldots,n$',\
     fontsize=14, color='g')

partxt=fig.text(0.4, 0.5, ' ',fontsize=14)
p = 0.1 # set parameter p of Binomial distribution 
txt='$p=$%.1f \n $N=\\mu/p$ \n $\\sigma=\\sqrt{\\mu}$' %(p)
partxt.set_text(txt)
def animate(n):
  if n<200:
    mu = (float(n)/20.) + 1.
  else:
    mu = (float(n)/10.)-10.
      
  sigma = np.sqrt(mu)
  n = mu/p
  lines = ax.plot(x, fGauss(x,mu,sigma), 'r-', x, fPoisson(x,mu), 'b-', x, fBinomial(x,n,p), 'g-') 

  return lines
   
print('\n*==* script ' + sys.argv[0]+' executing')
ani=anim.FuncAnimation(fig, animate, 500, interval=50, blit=True,
                         init_func=None, fargs=None, repeat=False)
plt.show()

