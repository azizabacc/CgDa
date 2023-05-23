# Musterloesung zu Blatt 2, Aufg. 2.2
''' Haeufigkeitsverteilung beim Wuerflen
    (kurze Loesung, array mit Zufallszahl als Index)
.. author:: Guenter Quast <g.quast@kit.edu>
'''
#aufgabe 4.1 a)
import numpy as np
import matplotlib.pyplot as plt

# 1) "Wuerfeln" der Zufallszahlen:
N = 1000
n=100 #anzahl wuerfel


# 2) Bestimmung der Haeufigkeit:

h =np.zeros(N)
S =np.ones(n)
for i in range(0, N):
    z = np.int32(6*np.random.rand(n) + 1)
    Summ=np.dot(S,z)
    mi=np.float32(Summ/n)
    h[i]=mi

    
mean=np.sum(h)/N
var=np.sum((h-mean)**2)/N


print mean,var

c, bins, patches = plt.hist(h, 16, normed=1, facecolor='g', log=False, alpha=0.5)

# erwartete ideele Verteilung  Gausskurve
mu = mean
sigma = np.sqrt(var)    # 3 fuer n=3 5 fuer n=10
def fgauss(x, mu, sigma):
    return np.exp(-(x-mu)**2/(2*sigma**2))/np.sqrt(2*np.pi*sigma**2)
 


# 3) grafisch Darstellen
a = np.arange(0., 7.01, 0.1)
plt.plot(a, fgauss(a,mu,sigma), 'r-')     

#   und noch ein wenig verschoenern ...
plt.xlabel(r'$Gew\"urfelte Zahl$', size='x-large')
plt.ylabel(r'$H\"aufigkeit$', size='x-large')


plt.grid(True)
plt.show()
