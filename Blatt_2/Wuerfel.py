import numpy as np
import matplotlib.pyplot as plt

#Zufallszahlen von 1 bis 6
x=-6*np.random.rand(1,120)+7
y=np.array(x,dtype=int)


#Wahrscheinlichkeiten
n=0
a=0.
b=0.
c=0.
d=0.
e=0.
f=0.
while n < 120:
    if (y[0][n] ==1):
        a=a+1
        n=n+1
    else:
        if (y[0][n] ==2):
            b=b+1
            n=n+1
        else:
            if (y[0][n] ==3):
                c=c+1
                n=n+1
            else:
                if (y[0][n] ==4):
                    d=d+1
                    n=n+1
                else:
                    if (y[0][n] ==5):
                        e=e+1
                        n=n+1
                    else:
                        if (y[0][n] ==6):
                            f=f+1
                            n=n+1
                        else:
                            print("Fehler im System bitte Neustarten")
                            


h=np.array([a,b,c,d,e,f])
plt.bar([1,2,3,4,5,6],h)
plt.show()
print(y)
print "Wahrscheinlichkeiten"
print"1:%f "%(a/120)
print"2:%f "%(b/120)
print"3:%f "%(c/120)
print"4:%f "%(d/120)
print"5:%f "%(e/120)
print"6:%f "%(f/120)