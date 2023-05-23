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
x=np.zeros(1+n*5)  
for i in range(1+n*5):
    x[i]+=i+n
x=np.int32(x)
  


nn=np.array([10,50,100])  #Array fuer anzahl Wuerfel
for k in range(3):
    n=nn[k]
    S=np.ones(n)
    x=np.zeros(1+n*5)
    for i in range(1+n*5):
        x[i]+=i+n
    x=np.int32(x)
    h = np.zeros(1+n*5)
    for i in range(0, N):
        z = np.int32(6*np.random.rand(n) + 1)
        Summ=np.dot(S,z)  
        Summ=np.int32(Summ)
        h[Summ-n] += 1  
        h=h/N 
    plt.bar(x, h, width=0.3, align='center', color='g', alpha=0.7)
h=h/N  
# erwartete ideele Verteilung  Gausskurve
mu = 3.5*n
sigma = 3    # 3 fuer n=3 5 fuer n=10
def fgauss(a, mu, sigma):
    return (np.exp(-(a-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)
 




# 3) grafisch Darstellen


#rects2=ax.bar(x+0.1, , width=0.1, align='center', color='g', alpha=0.7)
#   und noch ein wenig verschoenern ...
a = np.arange(n-3, n*6+3, 0.1)
plt.plot(a, fgauss(a,mu,sigma), 'r-')    
plt.xlabel(r'$Gew\"urfelte Zahl$', size='x-large')
plt.ylabel(r'$H\"aufigkeit$', size='x-large')


plt.grid(True)
plt.show()
