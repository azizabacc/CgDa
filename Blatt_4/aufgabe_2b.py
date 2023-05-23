import numpy as np
import matplotlib.pyplot as plt

# generate some data
N=100000 #Anzahl werte fuer z
n = 2 # 2,3,20 ist verlangt 

randat = np.zeros(n, dtype=float)
y = np.zeros(N)
z = np.zeros(N)
for i in range(0, N):
    randat= np.random.rand(n)
    y[i] = np.sum(randat)
    z[i] = (y[i]-n/2.)/np.sqrt(n/12.)


plt.hist(z, 50, normed=1, facecolor='g', log=False, alpha=0.5)


# definiere die Gaussfunction
mu = 0
sigma = 1
def fgauss(f, mu, sigma):
    return (np.exp(-(f-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)

# plot Gauss distribution
f = np.arange(-4*sigma, 4*sigma, 0.01)
plt.plot(f, fgauss(f, mu, sigma), "r-")


plt.show()
