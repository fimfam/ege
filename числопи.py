import random
import matplotlib.pyplot as plt
from math import pi, fabs
dots=0
ln=[]
lp=[]
for i in range(10000):
      x=random.uniform(-1,1)
      y=random.uniform(-1,1)
      if x**2+y**2<=1:
          dots+=1
mypi=4*dots/10000
print(mypi, pi, fabs(mypi-pi))
