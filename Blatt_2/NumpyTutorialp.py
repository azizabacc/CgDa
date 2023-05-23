import numpy as np
from timeit import Timer
size_of_vec=1000

def pure_python_version():
  X=range(size_of_vec)
  Y=range(size_of_vec)
  Z= []
  for i in range(len(X)):
    Z.append(X[i] +Y[i])
def numpy_version():
  X=np.arange(size_of_vec)
  Y=np.arange(size_of_vec)
  Z= X+Y
timer_obj1 = Timer("pure_python_version()", "from __main__ import pure_python_version")
timer_obj2 = Timer("numpy_version()", "from __main__ import numpy_version")
print(timer_obj1.timeit(10))
print(timer_obj2.timeit(10))



"Numpy mehrdimension vor allem" 
"print(X[::2,::3]) bei 4,7


# Data Befehl bei doppel belegung
>>> A =np.arange(12)
>>> B =A.reshape(3,4)
>>> A[0]=42
>>> print(B)
[[42  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
>>> print(A.data)
*


>>> print(B.data)
*


>>> print(A.data== B.data)
True
>>> np.may_share_memory(A,B)
True

#order="F""

#print(x.flags['C_CONTIGUOUS'])



