#!/usr/bin/env python
# script Vkugel.py
''' calculate volume of an n-dimensional sphere
with MC method and compare to exact formula
.. author:: Guenter Quast <g.quast@kit.edu>
'''

# dependencies:  PYTHON v2.7, numpy, matplotlib
# last modified:
# --------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import scipy.special as sp


def VofSphere(d, r=1.):
    """
      calculate volume of a d-dimensional sphere with radius r

      Args:
        d: dimension
        r: radius

      Returns:
        (array of) float: d-dimensional Volume
    """
    V = r**d * np.pi**(d/2.) / sp.gamma(d/2. + 1.)
    return V


# #### ---- main program starts here -----

# set dimensions
dmax = 10  # maximum
dim = np.linspace(1., dmax, dmax)

# volume from mathematical formula
Vtheo = VofSphere(dim)

# ---> put your code here
# implement MC method


#  ...
