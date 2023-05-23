#!/usr/bin/python
#
"""
.. 3D Function Plotter
   G. Quast, May 2015
   Modifed and extended version from mplot3d tutorial, contourf3d_demo2 
"""

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np


# --- some function definitions ---------------------------------------------

# 2D-Gaussian normal distribution
def gauss2d(x, y, mx=0, my=0., sx=1., sy=1., rho=0.5):
  u1 = (x-mx)/sx
  u2 = (y-my)/sy
  a = 2.*np.pi*sx*sy*np.sqrt(1-rho**2)
  return np.exp(-(u1**2 + u2**2 -2*rho*u1*u2)/(2.*(1-rho**2)) ) / a

# rosenbrock "banana" function: f(x,y) = (a-x)^2 + b*(y-x^2)^2
def rosenbrock_function(x,y,par=[1.,100.]):
  a = par[0]       # a
  b = par[1]       # b
  return (a-x)**2+b*(y-x**2)**2

# modified rosenbrock function: f(x,y) = (x^2+y-a)^2 + (x+y^2-b)^2 + c(x+y)^2
def modified_rosenbrock_function(x,y, par=[11., 7., 0.1]):
  a = par[0]       # a, should be 11
  b = par[1]       # b, should be 7
  c = par[2]       # c, should be 0.1
  return (x**2+y-a)**2 + (x+y**2-b)**2 + c*(x+y)**2

# ---helper functions ---------------------------------------
def get_3Dfunction_data(xmin=1.,xmax=1.,ymin=-1.,ymax=1., 
    func=gauss2d, delta=0.05):
    '''
    get funtion values on 2D-grid
    return a tuple X, Y, Z
    '''
    x = np.arange(xmin, xmax, delta)
    y = np.arange(ymin, ymax, delta)
    X, Y = np.meshgrid(x, y)
    Z=f(X,Y)
    return X,Y,Z

def plot_3dfunction(X,Y,Z, mimax, 
       xlab="x", ylab="y", zlab="Gauss(x,y)", project=True):
    '''
    3D-plotting of adata in arrays X, Y and Z
    input: X, Y, Z   data arrays
           mimax     minimum and max ranges in x, y, z [[min],[max]]
           x(y,z)lab axis labels
           project   also plot projections along x, y, and z if True 
    '''
    from matplotlib import cm # color maps
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.ticklabel_format(axis='both', style='scientific',
                       scilimits=(-3,4), useOffset=False)
    if(project):
    # plot 3d as lines with projections
        surf=ax.plot_surface(X, Y, Z, rstride=3, cstride=3, alpha=0.3)
#        ax.contourf(X, Y, Z, zdir='x', offset=mimax[0][0], cmap=cm.coolwarm)
#        ax.contourf(X, Y, Z, zdir='y', offset=mimax[1][1], cmap=cm.coolwarm)
        ax.contourf(X, Y, Z, zdir='z', offset=mimax[1][2], cmap=cm.coolwarm)
    # OR plot 3d-surface with colour code ...
    else: 
        surf=ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, 
                    linewidth=0, antialiased=False)
        fig.colorbar(surf)
    ax.set_xlabel(xlab)
    ax.set_xlim(mimax[0][0], mimax[1][0])
    ax.set_ylabel(ylab)
    ax.set_ylim(mimax[0][1], mimax[1][1])
    ax.set_zlabel(zlab)
    ax.set_zlim(mimax[0][2], mimax[1][2])
    plt.show()
    return
  
# --------------------------------------------------------------------
if __name__ == '__main__':

# ---  example code illustrating usage
    
# first, choose a function and its ranges
    f=gauss2d
#    f=rosenbrock_function
#    f=modified_rosenbrock_function
    minx = -3.
    maxx = 3.
    miny = -3.
    maxy = 3.
    X, Y, Z = get_3Dfunction_data(xmin=minx, xmax=maxx, ymin=miny, ymax=maxy,
      func=f, delta=0.1)
    minz = np.amin(Z)
    maxz = np.amax(Z)
    # extend maximum and minimum range for plot    
    amin=np.array([minx,miny,minz]) 
    amax=np.array([maxx,maxy,maxz]) 
    borderf=0.15 # add 15% at borders
    pmin=amin-borderf*(amax-amin)
    pmax=amax+borderf*(amax-amin)
    plot_3dfunction(X,Y,Z,[pmin,pmax], project=True)
