import numpy as np
import matplotlib.pyplot as plt

# define a function (straight line)
def fpol1(x, a=1., b=0.):
    return (a*x + b)
def fgauss(x, mu=0, sigma=1):
    return (np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)




def histstat(binc, bine):
    # calculate mean of a histogram with bincontents binc and bin edges bine
    bincent = (bine[1:]+bine[:-1])/2    # determine bincenters
    mean = sum(binc*bincent)/sum(binc)
    rms = np.sqrt(sum(binc*bincent**2)/sum(binc) - mean**2)
    return mean, rms


# generate some data
ndat = 1000
randat = np.random.rand(ndat)

# Implemenzirtung von z
anz = 100000

z=np.zeros(anz)
for n in (2.,3.,20.):
    xi = np.random.rand(n)
    z=np.zeros(anz)
    for i in range(anz):
        z1=(np.sum(xi)-n*0.5)/np.sqrt(n/12)
        z[i]=z1
    binco, bined, patches2 = plt.hist(z, 100, normed=0, log=False, alpha=0.5)
    

# plot data as histogram
nbin = 20
#binc, bine, patches = plt.hist(randat, nbin, normed=0,
#                               facecolor='g', log=False, alpha=0.5)
# make plot nicer:
plt.xlabel('random number')  # axis labels
plt.ylabel('frequency')
plt.title('Histogram of uniform random numbers')  # title



# calculate histogram mean and rms from histogram array
#hmean, hsigma = histstat(binc, bine)    # get mean and RMS
#print "mean, sigma = ", hmean, hsigma


# plot
a = 0
b = np.float(ndat)/np.float(nbin)
x = np.arange(0, 1., 0.005)
#plt.plot(x, fpol1(x, a, b), 'b-')             # plot function
#plt.text(0.5, b*1.1, r'constant function', fontsize=14, color='b')
plt.plot(x, fgauss(x, mu=0, sigma=1))
plt.grid(True)  # show a grid for orientation
plt.show()      # now display everything on the scree