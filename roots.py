#finds whether there are two complex roots, one real root, or two real roots

import math
a = float(input("What is a?"))
b = float(input("What is b?"))
c = float(input("What is c?"))

x = b**2-4*a*c

if x==0:
  print("There is one real root")
  y = -b/(2*a)
  z = math.sqrt(abs(x))/(2*a)
  print(y+z)
elif x>0:
  print("There are two real roots")
  y = -b/(2*a)
  z = math.sqrt(abs(x))/(2*a)
  print(y+z, y-z)
elif x<0:
  y = -b/(2*a)
  z = math.sqrt(abs(x))/(2*a)
  print(y,"+", z, "i")
  print("There are two complex roots")
