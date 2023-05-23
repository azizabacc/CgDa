#!/usr/bin/env python
# script animate_GaussFunction.py
''' example of a simpe animation: animated Gauss distributions
.. author:: Guenter Quast <g.quast@kit.edu>
'''

# dependencies:  PYTHON v2.7, numpy, matplotlib
# last modified: 
#--------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import sys

# define a function (Gauss distribution)
def fgauss(x,norm=1.,mu=0.,sigma=1.):
    return (norm*np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)

##### ---- main Program starts here -----
if __name__ == "__main__":

  fig=plt.figure(figsize=(7.5,7.5))
  ax=fig.add_subplot(1,1,1)
  ax.grid(True)
  ax.text(0.4,1.05,\
    r'$N(x) = \frac{1}{\sqrt{2\,\pi}\sigma}\,\exp{\left(\frac{-(x-\mu)^2}{2\sigma^2}\right)}$',\
    transform=ax.transAxes, size='xx-large')
  ax.set_xlabel('x')
  ax.set_ylabel('N(x)')
  ax.set_ylim(0.,0.8)
  partxt = ax.text(0.55, 0.93, ' ', transform=ax.transAxes,size='x-large',
                    color='b', backgroundcolor='white')
  x=np.linspace(-4.,6.,200)
  mu=0.
  sig=1.
  y=fgauss(x,1.,mu,sig)
  graph, = ax.plot(x,y,'-', color='g', lw=3)

  def animate(n):
    global mu,sig
    if n<25:
      mu=-float(n)/25.
    elif n<150:
      mu = -1. + (float(n)-25.)/25. 
    elif n<225:
      mu = 4. - (float(n)-150.)/25.
    elif n<275:
      mu=1.
      sig = 1. + (float(n)-225.)/25.
    elif n<325:
      sig= 3. - (float(n)-275.)/25.
    elif n<=375:
      sig= 1. - (float(n)-325.)/100.
    else:
      sig=0.5          
    y=fgauss(x,1.,mu,sig)
    graph, = ax.plot(x,y,'-', color='blue', lw=2)
    txt='$\\mu=$ %.2f  $\\sigma=$ %.2f' %(mu,sig)
    partxt.set_text(txt)
    return graph, partxt

  print('\n*==* script ' + sys.argv[0]+' executing')
  ani=anim.FuncAnimation(fig, animate, 400, interval=50, blit=True,
                         init_func=None, fargs=None, repeat=False)
  plt.show()
