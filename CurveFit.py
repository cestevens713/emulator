import numpy as np
from random import gauss
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def weibull(x, A, B, W, S):
    return (A*(1 - np.exp(-1*((x - B)/W)**S)))

Name = 'Weibull\LM6172.csv'
doc = pd.DataFrame(pd.read_csv(Name, index_col=[0]), 
            columns=['Eff. LET', 'XS', 'Fluence', 'Onset LET', 'Limiting XS', 'Shape', 'Width'])
doc = doc.sort_values(by = ['Eff. LET'], ascending = True)
lin = stats.linregress(doc['Eff. LET'], doc['XS'])
LET = doc['Eff. LET'].to_list()
fluence = doc['Fluence'].to_list()

minLET = int(LET[0])
maxLET = int(LET[len(LET) - 1])

m = lin.slope
b = lin.intercept

a = 1.5*(10**-3) #cm^2, cross section
x0 = 0.5         #unk unit, onset parameter
w = 31           #unk unit, width parameter (can be altered)
s = 1            #unitless exponent (can be altered [1-10])

a1 = 10.**(np.arange(-1, 2))
a2 = np.arange(1, 10, 1)
xp = np.outer(a1, a2)
X = np.concatenate(xp, axis=0)
GoldStandardLET = X[minLET:maxLET]
GoldStandardXS = weibull(GoldStandardLET, a, x0, w, s)

mean = []
for h in range(0, len(LET)):
    NewMean = weibull(LET[h], a, x0, w, s)
    mean.append(NewMean)
    h = h + 1

sd = []
for i in range(0, len(LET)):
    NewSD = b + m*LET[i]
    sd.append(NewSD)
    i = i + 1

XS = []
for j in range(0, len(LET)):
    NewXS = gauss(mean[j], sd[j])
    XS.append(NewXS)
    j = j + 1
"""
upsets = []
for k in range(0, len(LET)):
    NewUpset = XS[k]*fluence[k]
    upsets.append(NewUpset)
    #print("For run number " + str(k) + ", " 
    #            + str(upsets[k]) + " upsets occured")
    k = k + 1
"""
#popt, pcov = curve_fit(weibull, LET, XS)
#plt.plot(LET, weibull(LET, *popt), 'r-', label = 'fit')
plt.yscale("log")
plt.plot(LET, XS, 'o', label = 'data')
plt.plot(GoldStandardLET, GoldStandardXS, 'orange', label = 'Gold Standard')
plt.legend()
plt.show()
