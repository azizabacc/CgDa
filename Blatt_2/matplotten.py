import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim




# define a function
def parabel (x):
    return (x**2)




err =0.1
xm=np.array([1.,2.,3.,4.,])
ym=(xm**2)
dy=np.random.randn(4)
yn=(dy*0.1*xm**2+ym)
# set parameters for the function

# parameters for histogram 
nbins=100
xmin,xmax=0., 5.
ymax=xmax**2
nbins=100
bine=np.linspace(xmin,xmax,nbins+1)    # bin edges for histogram
bincenters=(bine[:-1] + bine[1:])/2.
width=0.95*(bine[1]-bine[0])
bincont=np.zeros(nbins)

# define and plot initial graph
fig, ax = plt.subplots()
ax.set_xlim(xmin,xmax)
ax.set_ylim(0.,ymax)
ax.set_xlabel('x') # axis labels
ax.set_ylabel('Langeweile')
ax.set_title('Normalparabel') # title

# Funktion nochmal angegebn
#fig.text(0.15, 0.8,
#r'$f(x) = \frac{1}{\sqrt{2\,\pi}\sigma}\,\exp{\left(\frac{-(x-\mu)^2}{2\sigma^2}\right)}$', \
#fontsize=14, color='g') # a nicely type-set formula of the function
plt.grid(True) # show a grid for orientation 

# plot function

xvals = np.arange(xmin, xmax, 0.1) 
ax.plot(xvals, parabel(xvals), 'g-', lw=2)  


x=np.linspace(0.,xmax,nbins)
y=(x**2)


# display on Screen
plt.plot(x,y)
plt.errorbar(xm,yn,yerr=1,fmt='bo') 
plt.show() 

