import numpy as np

nmax = 40 
oddInt = np.arange(1,nmax,2)
print(oddInt)
n = len(oddInt)
alt = (-1)**np.arange(0,n)
print(alt)
lebinizVector = 1/oddInt*alt
print(lebinizVector)
sum = 0
for el in lebinizVector:
    sum = sum + el

print(sum)