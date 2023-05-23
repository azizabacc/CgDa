#!/usr/bin/python 

# -------- Gauss.py ------------------------------------------
# Description: example showing 
#              - how to define a function
#              - read data from text file
#              - generate a histogram
#              - use matplotlib to plot histogram and function
# Author:      G. Quast   Oct. 2013
# dependencies: PYTHON v2.7, numpy, matplotlib.pyplot 
# last modified: 
#--------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
 
# define a function (Gauss distribution)
def fgauss(x,norm=1.,mu=0.,sigma=1.):
    return (norm*np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)
 

# set parameters for Gaussian distribtion
mu=0
sigma=1

# parameters for histogram 
nbins=100
xmin,xmax=-4., 4.
nbins=100
bine=np.linspace(xmin,xmax,nbins+1)    # bin edges for histogram
bincenters=(bine[:-1] + bine[1:])/2.
width=0.95*(bine[1]-bine[0])
bincont=np.zeros(nbins)

# define and plot initial graph
fig, ax = plt.subplots()
ax.set_xlim(xmin,xmax)
ax.set_ylim(0.,0.55)
ax.set_xlabel('x') # axis labels
ax.set_ylabel('probability density')
ax.set_title('Histogram of Gauss distribution') # title
fig.text(0.15, 0.8,
r'$f(x) = \frac{1}{\sqrt{2\,\pi}\sigma}\,\exp{\left(\frac{-(x-\mu)^2}{2\sigma^2}\right)}$', \
fontsize=14, color='g') # a nicely type-set formula of the function
plt.grid(True) # show a grid for orientation 
# plot Gauss distribution
xvals = np.arange(xmin, xmax, 0.1) 
ax.plot(xvals, fgauss(xvals,norm=1.,mu=mu,sigma=sigma), 'g-', lw=2)             

# code relevant to parts of figure to animate

def init():
# plot initial histogram as bar graph
  h=ax.bar(bincenters,bincont,align='center',width=width,facecolor='b',alpha=0.5) 
  return h

# number of randoms per iteration
nr=50
def data_gen():
  # generate random numbers and re-calculate bin contents of histogram
  cnt=0
  bincont=np.zeros(nbins)
  while cnt<200:
    cnt+=1
    data=np.random.normal(size=nr)  
    bc,be = np.histogram(data,bine,normed=1) # histogram data
    bincont+=bc
    yield (cnt*nr, bincont/cnt)

def animate((n, bcont)):
# plot histogram as bar graph
  h=ax.bar(bincenters,bcont,align='center',width=width,facecolor='b',alpha=0.5)
  return h

# 
ani = anim.FuncAnimation(fig, animate, data_gen, init_func=init,
                               interval=50, blit=True, repeat=False)

plt.show()  # now display everything on the screen



