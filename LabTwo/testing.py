# root thingie mabob

import numpy as np

a = float(input('coeff a: '))
b = float(input('coeff b: '))
c = float(input('coeff c: '))
D = b**2-4*a*c #discriminant
if D<0:
    print("no real roots")
else:
    r = float(input('guess: '))
    if np.abs(a*r**2+b*r+c)<1e-16:
        print("Your guess was indeed a root!")
    else:
        if a == 0:
            x = -c/b
            print(f"there is one root it is : {x}")
        else:
            r1 = (-b+np.sqrt(D)/(2*a))
            r2 = (-b-np.sqrt(D)/(2*a))
            print(f"the roots are {r1} and {r2}")

