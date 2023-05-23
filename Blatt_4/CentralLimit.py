# -------- CentralLimit.py ----------------------------------------
# Description: Vorlage CGDA SS16 Blatt04: Zentraler Grenzwertsatz
#
# Author:      G. Quast   Dec. 2013
# dependencies: PYTHON v2.7, numpy, matplotlib.pyplot
# last modified:
# -----------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt


# --- some helper functions ---
# Gauss distribution

def fgauss(x, mu=0, sigma=1):
    return (np.exp(-(x-mu)**2/2/sigma**2)/np.sqrt(2*np.pi)/sigma)


# ==>> your code goes from here on:

# plot reference Gauss distribution and data
def CompareNormal(data, title=' ', xlabel=' '):
    # ==>> your code
    # plot data array as a histogram
    return


# --- execution starts here ------
isize = 100000
# build sum 1 - n  of random numbers
for n in range(2, 21):
    # ==>> your code
    z = ???

    # now Compare with Normal distribution
    title = ' '     # complete title of figure
    xlab = ' '      # complete  axix label (should include "n")
    # CompareNormal(z, title, xlab)

    # save plot to file
    filename = 'xxx' + '.pdf'
    plt.savefig(filename)
    # plt.show() # eventually, show plot (for debug purpose)
    plt.clf()    # clear the figure after we saved it
    #
    # next n
# end loop over n

print 'this is the end'
