#!/usr/bin/env python
# script py.py
''' calculate area of a circle with MC method,
with graphical illustration
.. author:: Guenter Quast <g.quast@kit.edu>
'''

# dependencies:  PYTHON v2.7, numpy, matplotlib
# last modified:
# -------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import sys
import scipy.special as sp

# ---- main Program starts here -----

npoints = 10000
n=4#n-te Dimension
N=100


def Nin(ndim,npoints=10000):
    ninp=0.
    noutp=0.
    #ins = np.zeros((ndim,npoints))
    #outs= np.zeros((ndim,npoints))
    for i in range(npoints):
        rvec=np.random.rand(ndim)
        if np.sum(rvec**2) <=1.:
    #for j in range(n):
    #    ins[j,i]=rvec[j]
            ninp+=1
        else:
    #for k in range(n):
    #    outs[k,i]=rvec[k]
            noutp+=1    
    v=np.array([ninp,noutp])
    return v
 
#plt.hist(ninp)    
# Binominalverteilung hinzuziehen zur varaianz berechnung
def volkug(inp,outp,dim):
    volseg = inp/(inp+outp)
    volkug = volseg*2**dim
    return volkug


def varvol(dim,inp,npoints=10000):
    p=inp/npoints
    var=npoints*p*(1.-p)
    volseg2 = np.sqrt(var)/npoints
    volkug2 = volseg2*2**dim
    return volkug2


    
    

def VofSphere(d, r=1.):
    V = r**d * np.pi**(d/2.) / sp.gamma(d/2. + 1.)
    return V    

#plotten

y=np.zeros(11) 
y2=np.zeros(11)
varianz=np.zeros(11)
x3=np.zeros(11)
for i in range(11):
    n=i
    Ninp=Nin(n,npoints)
    varianz[i]=varvol(n,Ninp[0],npoints=10000)
    y[i]=volkug(Ninp[0],Ninp[1],n)
    y2[i]=VofSphere(n,r=1.)
    x3[i]=Ninp[0]
print x3
print varianz

   
x=np.arange(0,10.1,1)
print x
print y


plt.plot(y)
plt.plot(y2)

plt.errorbar(x,y , yerr=varianz, fmt='ro')
'''
fig = plt.figure(figsize=(7.5,7.5, 7.5))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(inside, , s=1, color='green')
ax.scatter(outside, outsidey, s=1, color='red')

'''
'''

volseg = ninp/(ninp+noutp)
volkug = volseg*2**n
print('\n*==* script ' + sys.argv[0]+' executing')
print('   Total number of random points %i' %(inpoints+outpoints))
print('   Points inside circle '), ninp
print('   Volumen  Kugelsegment '),volseg
print('   Volumen der Hyperkugel '),volkug
#print('   ==> pi= %.3f' % pi)
'''


plt.title('Volumen einer Kugel')
plt.xlabel('n-te Dimension', size='x-large')
plt.ylabel('Volumen', size='x-large')
plt.xlim(0., 10.5)
plt.legend(loc='upper right')
plt.grid(True)
plt.show()