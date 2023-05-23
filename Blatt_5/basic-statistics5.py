#!/usr/bin/env python
#     (the first line allows execution directly from the linux shell) 
#
# --- sinmple python exercise 
# Author:        G. Quast   Oct. 2013
# dependencies:  PYTHON v2.7, numpy
# last modified: 
#--------------------------------------------------------------

'''
Frage Tutor:
array von int zu float 
umlaute erlauben
Funktionen und ihr variablen beispiel mean(a), mean(odds)
'''
import numpy as np

# write here your own implementation of the statistical functions

def mean(a):
  return np.sum(a)/len(a)

def variance(a):
    v=np.sum((a-mean(a))**2)/N
    return v

def sigma(a):
    s= np.sqrt(variance(a))
    return s

def cov(a,b):
    return (1/(len(a)-1)*np.sum((a-mean(a))*(b-mean(b))))
            
def Kore(a,b):
    return (cov(a,b)/(sigma(a)*sigma(b)))

# --- main program
#
# read data from text file
a = np.loadtxt('numbers.dat', dtype=float)
N = len(a)
print N, " numbers read \n", a

#Erste wahrscheinlichkeitsberechnung
z,b,c,d,e,f,g,h,k,j=0.,0.,0.,0.,0.,0.,0.,0.,0.,0.
for i in range(N):
    if (a[i] ==0):
        z=z+1
    elif (a[i]==1):
        b=b+1
    elif (a[i]==2):
        c=c+1
    elif (a[i]==3):
        d=d+1
    elif (a[i]==4):
        e=e+1
    elif (a[i]==5):
        f=f+1
    elif (a[i]==6):
        g=g+1
    elif (a[i]==7):
        h=h+1
    elif (a[i]==8):
        j=j+1
    else:
        k=k+1
odds=np.array([z,b,c,d,e,f,g,h,j,k])/N


# zweiter, kuerzerer Weg        

b = np.loadtxt('numbers.dat', dtype=int)
h=np.array([0,0,0,0,0,0,0,0,0,0])
i=0
while i < N:
    h[b[i]]=(h[b[i]]+1)
    i=i+1
    
#Aufgabenteil  c
#mit h Mittelwert,... bestimmen   
c=np.array([0,1,2,3,4,5,6,7,8,9]) #array fuer mittelwert

def mean2(odds):
    return np.dot(odds,c)

def variance2(odds):
    return np.sum(odds*(c-mean2(odds))**2)

def sigma2(odds):
    return np.sqrt(variance2(odds))


    

#     print same statistical quantities using numpy functions
print "\n*==* result with numpy functions:"
print "mean is", np.mean(a), mean(a), mean2(odds)
print "variance is", np.var(a), variance(a),variance2(odds) 
print "standard deviation sigma=", np.std(a), sigma(a), sigma2(odds)
print "unbiased sigma =", np.std(a)*np.sqrt(N/(N-1.0))
print odds
print h


print odds[1]

# ---> your code starts here ....

# calculate and print some statistical quantities on raw data

# histogram data

# calculate mean and sigma from histogram and print
