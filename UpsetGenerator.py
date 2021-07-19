import numpy as np
from random import seed
from random import gauss

input1 = input("Input LET: ")
input2 = input("Input Standard Deviation: ")
input3 = input("Input Fluence: ")
LET = float(input1)
sd = float(input2)
fluence = float(input3)

a = 1.5*(10**-3) #cm^2, cross section
b = 0.5          #unk unit, onset parameter
w = 20           #unk unit, width parameter (can be altered)
s = 1.1          #unitless exponent (can be altered [1-10])

xs = a*(1 - np.exp(-1*((LET - b)/w)**s))

Randxs = gauss(xs, sd)

upsets = Randxs*fluence

print(str(upsets) + " upsets occured")
