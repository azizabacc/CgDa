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

# ---- main Program starts here -----

npoints = 10000

insidex = []
insidey = []
outsidex = []
outsidey = []

for i in range(npoints):
    rvec = np.random.rand(2)
    if np.sum(rvec**2) <= 1.:
        insidex.append(rvec[0])
        insidey.append(rvec[1])
    else:
        outsidex.append(rvec[0])
        outsidey.append(rvec[1])


fig = plt.figure(figsize=(7.5, 7.5))
ax = fig.add_subplot(1, 1, 1)
ax.scatter(insidex, insidey, s=1, color='green')
ax.scatter(outsidex, outsidey, s=1, color='red')

pi = 4.*float(len(insidex))/float((len(insidex)+len(outsidex)))
print insidex,insidey
print outsidex,outsidey
print('\n*==* script ' + sys.argv[0]+' executing')
print('   Total number of random points %i' % (len(insidex)+len(outsidex)))
print('   Points inside circle %i' % len(insidex))
print('   ==> pi= %.3f' % pi)

plt.show()

