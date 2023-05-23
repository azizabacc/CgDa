# -*- coding: utf-8 -*-
#      diese Zeile legt die Codierung von Umlauten fest
##################################################################

# script PlotResonanz.py
'''
       Musterlösung zur Funktionsdarstellung mit matplotlib

   HILFE:
     Ausführen dieses Programms: python PROGRAMMNAME
     Dieses Programm ist in der Sprachversion 2 von python geschrieben.

     numpy-Objekte werden mit prefix "np." aufgerufen
     matplotlib-Objekte werden mit prefix "plt." aufgerufen

.. author:: Günter Quast <g.quast@kit.edu>
     für den Kurs Computergestützte Datenauswertung (CgDA)
'''
# -------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt


def resonanz(eta, D, A=1.):
    return A/np.sqrt((1 - eta*eta)**2 + (2.*eta*D)**2)


# ---- main Program starts here -----
# Ein numpy-array, das die Stuetzstellen enthaelt (np.pi ist pi=3.141..)
etamin, etamax = 0., 3.
npoints = 256
eta = np.linspace(etamin, etamax, npoints, endpoint=True)

# Plots der Funktion generieren
for D in (0.05, 0.1, 0.2, 0.3, 0.5, 1., 2., 3.0):
    plt.plot(eta, resonanz(eta, D), linewidth=2, label="D="+str(D))

# Plot noch etwas polieren
plt.title('Resonanzkurve')
plt.xlabel('$\eta=\omega/\omega_0$', size='x-large')
plt.ylabel('(normierte) Amplidude $A$', size='x-large')
plt.xlim(eta.min()*1.1, eta.max()*1.1)
plt.legend(loc='upper right')
plt.grid(True)

plt.show()
