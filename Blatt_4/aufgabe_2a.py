import numpy as np
import matplotlib.pyplot as plt

# generate some data
N =100 #fuer ein paar verschiedene y
n = 10000

y=np.zeros(N)
for i in range(0,N):
    randat =np.zeros(n, dtype=float)
    randat= np.random.rand(n)
    y[i] = np.sum(randat)

# Erwartungswert, Standardabweichung und Varianz berechnen
def mean(a):
  return np.sum(a)/len(a)

def variance(a):
    v=np.sum((a-mean(a))**2)/len(a)
    return v

def sigma(a):
    s= np.sqrt(variance(a))
    return s


print sigma(randat), 'Standardabweichung,Vergleich sqrt(1/12) ',np.sqrt(1/12.)
print mean(y) , 'Erwartungswert, Vergleich zu n/2  ',n/2.
print variance(y) , 'Varianz, Vergleich zu n/12',n/12.

#    z[i] = (y[i]-n/2.)/np.sqrt(n/12.)



#plt.hist(z, 50, normed=1, facecolor='g', log=False, alpha=0.5)




plt.show()
