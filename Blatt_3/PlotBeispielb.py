# -*- coding: utf-8 -*-
#      diese Zeile legt die Codierung von Umlauten fest
##################################################################

# script PlotBeispiel.py
''' 
Fragen Tutor:
Generieren vpn verschiedenen Farben fuer die Funktionsschaaren
'''
#--------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

def myFunction(x,p1,p2):
    F = p1/((1-x**2)**2+(2*x*p2)**2)**0.5
    return F               

##### ---- main Program starts here -----

## Ein numpy-array, das die Stuetzstellen enthaelt (np.pi ist pi=3.141..)
emin, emax = 0, 3
npoints = 256
X = np.linspace(emin, emax, npoints, endpoint=True)

# Plot der Funktionen, die werden hier aber noch nicht angezeigt!
A_s=1.0
D=0.
# Darstellung einer Sinus-Funktion
for i in range(0,20):
    D=D+0.05
    Y = myFunction(X, A_s, D)
    plt.plot(X, Y)
    
    
plt.text(1.5,8,r'$A(\eta=\omega/\omega_0), A_s,D)= \frac{A_s}{\sqrt{(1-\eta^2)^2+(2\eta D)^2}}$')


'''
 Darstellung einer Cosinus-Funktion
phase = np.pi/2.
Y = myFunction(X, A_s, D)
plt.plot(X, Y, color="green", label="Cosinus")
'''

# Definition der Grenzen der grafischen Ausgabe ...
plt.xlim(-0.1,3.1)
plt.ylim(-0.5,10.5)
# und Verschönern der Grafik:
# Setze in X- und Y-Richtung ein paar Ticks (Achsenpunkte)
# LaTeX-Ausdruecke koennen verwendet werden, r steht fuer "raw-string"

#plt.xticks([0, np.pi/2, np.pi, np.pi*2],
#           [r'$0$', r'$\pi/2$', r'$\pi$', r'$2\pi$'])


#plt.yticks(np.linspace(-1, 1, 5, endpoint=True))

# Wo soll die Legende hin? (Text dazu ist in den "label" der plot-Anweisungen)
#plt.legend(loc='lower left')

# Zeige ein Gitternetz
plt.grid(True)

# Zeige nun alles auf dem Bildschirm an
plt.show()
