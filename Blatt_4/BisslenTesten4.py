# Musterloesung zu Blatt 2, Aufg. 2.2
''' Haeufigkeitsverteilung beim Wuerflen
    (kurze Loesung, array mit Zufallszahl als Index)
.. author:: Guenter Quast <g.quast@kit.edu>
'''

import numpy as np
import matplotlib.pyplot as plt


n=10
xi = np.random.rand(n)
z1=(np.sqrt(n/12.))
print z1
print xi

exit()

'''
n=3
N=1000



z1 =  np.int32(6*np.random.rand(N) + 1)
z2 =  np.int32(6*np.random.rand(N) + 1)
z3 =  np.int32(6*np.random.rand(N) + 1)

h= np.float32(z1+z2+z3)/n

def fgauss(a, mu, sigma):
    return (np.exp(-(a-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)


a = np.arange(0., 7., 0.1)
plt.plot(a, fgauss(a,mu=mu,sigma=sigma), 'r-')      


c, bins, patches = plt.hist(h, n*5+1, normed=1, facecolor='g', log=False, alpha=0.5)


# 3) grafische Darstellung als Balkendiagramm mit bar():
#plt.bar(x, z, width=0.1, align='center', color='g', alpha=0.7)
#   und noch ein wenig verschoenern ...
plt.xlabel(r'$Gew\"urfelte Zahl$', size='x-large')
plt.ylabel(r'$H\"aufigkeit$', size='x-large')


#plt.show()
'''
n=2
xi = np.random.rand(n)
z1=(np.sum(xi)-n*0.5)/np.sqrt(n/12)
print z1