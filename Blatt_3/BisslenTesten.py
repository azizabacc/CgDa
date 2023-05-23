import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(2,1,2)

plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
#plt.title("$\(A_s\)$")
plt.subplot(211)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')


b = np.loadtxt('numbers.dat', dtype=int)
N = len(b)
h=np.array([0,0,0,0,0,0,0,0,0,0])
i=0
while i < N:
    h[b[i]]=(h[b[i]]+1)
    i=i+1
#print(h)
sigma=1
mu=0


data = sigma* np.random.randn(100) +mu
# Ueberpruefung der Formel von data fuer beliebiges mu und sigma
def mean(data):
  return np.sum(data)/100


def variance(a):
    v=np.sum((data-mean(data))**2)/100
    return v

def sigma2(data):
    s= np.sqrt(variance(data))
    return s

print mean(data)
print sigma2(data)
hist=np.zeros(1000)
for i in range(1000):
    x =sigma* np.random.normal(9)+mu
    m =np.sum(x)/9
    bc=np.histogram=(m)
    hist=hist+bc
    
print(hist)
