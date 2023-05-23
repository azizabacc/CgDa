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
n=3 #anzahl werfel
z1 = np.int32(6*np.random.rand(N) + 1)
z2 = np.int32(6*np.random.rand(N) + 1)
z3 = np.int32(6*np.random.rand(N) + 1)
z  = np.float64(z1+z2+z3)

# int32(): Ganzzahl-Anteil
# 6*random.rand(N)+1: N gleichverteilte Zufallszahlen im Intervall 1<z<7
#                     z nimmt also die Werte 1-6 an

# 2) Bestimmung der Haeufigkeit:
c, bins, patches = plt.hist(z, n*5+1, normed=1, facecolor='g', log=False, alpha=0.5)
  # Zufallszahl als Index, entsprechenden Wert um 1 erhoehen
#   -> Haeufigkeit der gewuerfelten Zahl i in h[i-1] , i=1, ..., 6
x=np.linspace(3,18,1,endpoint=True)
# 3) grafische Darstellung als Balkendiagramm mit bar():
#plt.bar(x, h, width=0.1, align='center', color='g', alpha=0.7)
#   und noch ein wenig verschoenern ...
plt.xlabel(r'$Gew\"urfelte Zahl$', size='x-large')
plt.ylabel(r'$H\"aufigkeit$', size='x-large')
#   und anzeigen
plt.show()
