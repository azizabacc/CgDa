import math



def expfkt(a):
  resultat = math.exp(a)
  return resultat

print "Exponentialfunktion berechnen"
print "-----------------------------"
print

a = raw_input("Eine Zahl bitte: ")
wert = float(a)

print "Der Wert von %g lautet %f" %(wert,expfkt(wert))

    
    