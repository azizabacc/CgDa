import numpy as np
import matplotlib.pyplot as plt
import sys
'''
nbins=6
N=10
#x=np.int32(np.random.rand(N)*6+1)
x=(1,2,3,4,5,6,1,3,2,1)
bc, be = np.histogram(x, nbins, normed=1)
y=np.array([x,x])
print y*2

print x
print bc,be
n, bins, patches = plt.hist(x, nbins, facecolor='g', log=False, alpha=0.5)
print (' jetzt zweiter teil:')
print (' n:  '), n
print (' bins '), bins
'''
#plt.show()

def var(inp,npoints=10000):
    #p=inp/npoints
    var=npoints*(inp/npoints)*(1.-(inp/npoints))
    return var


y=np.zeros(10) 
y2=np.zeros(10)
varianz=np.zeros(10)
x3=np.zeros(10)
for i in range(10):
    n=i+1
    Ninp=Nin(n,npoints)
    varianz[i]=var(Ninp[0],npoints=1000)
    y[i]=volkug(Ninp[0],Ninp[1],n)
    y2[i]=VofSphere(n,r=1.)
    x3[i]=Ninp[0]
#print x3
#print varianz

vari=10000.