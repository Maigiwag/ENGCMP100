##---CODE FROM LESSONS---##
input = int(input("thing: "))
import numpy as np


if input == 1:
    #---recursive function---#
    def factorial(n):
        return n if n<= 1 else n*factorial(n-1)
    n = factorial(4)
    print(n)
if input == 2: 
    A = [14,1456,1234]
    for i in A:
        print(i)
    


