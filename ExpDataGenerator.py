import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

def weibull(x, A, B, W, S):
    return (A*(1 - np.exp(-1*((np.log(x) - B)/W)**S)))

vecWeibull = np.vectorize(weibull)

a = 5*(10**-7)
b = 0.5
w = 30
s = 0.17

X = np.arange(0.1,30,.1)

YExac = vecWeibull(X,a,b,w,s)

Offset = 0.01

A = stats.norm.rvs(loc=a,scale=a*Offset, size = len(X))
B = stats.norm.rvs(loc=b,scale=b*Offset, size = len(X))
W = stats.norm.rvs(loc=w,scale=w*Offset, size = len(X))
S = stats.norm.rvs(loc=s,scale=s*Offset, size = len(X))

plt.figure('A')
plt.hist(A)
plt.figure('B')
plt.hist(B)
plt.figure('W')
plt.hist(W)
plt.figure('S')
plt.hist(S)


YExp = vecWeibull(X,A,B,W,S)

plt.figure('Weibull')
plt.yscale("log")
plt.scatter(X, YExp, color = 'black', label = 'Experiment')
plt.plot(X, YExac, color = 'red', label = 'Exact')
plt.legend()
plt.xlabel("LET (in MeV-cm^2/mg)")
plt.ylabel("Cross Section (in square-microns/bit)")
plt.show()
