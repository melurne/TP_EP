import matplotlib.pyplot as plt
#import scipy.optimize
#from scipy.optimize import curve_fit
import numpy

R = 50 # <=> P = 1200 W
alpha = 0.3
f = 500 #Hz

L1_1 = {"Vin" : 63.7, "Iin" : 0.1, "VoutEff" : 18.75, "IoutEff" : 0.31, "freal" : 543, "alphareal" : 0.26}

rho = (L1_1["VoutEff"]*L1_1["IoutEff"])/(L1_1["Vin"]*L1_1["Iin"]) # rho = 0.91
#print(rho)

Lalpha = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
LVout = [6.26, 10.19, 19.05, 25.4, 32.3, 38.6, 45, 50.8, 56.8, 59.6]

a, b = numpy.polyfit(Lalpha, LVout, 1)
print(a, b)

Lfit = [a*i+b for i in Lalpha]

plt.plot(Lalpha, LVout, "r")
plt.plot(Lalpha, Lfit, "b--")
plt.xlabel("alpha")
plt.ylabel("Vout")
plt.title("Vout = f(alpha)")
plt.show()

Ll = [0.15, 0.2, 0.3, 0.4, 0.5, 0.7, 0.9, 1.1, 1.2]
LIout = [0.51, 0.51, 0.50, 0.5, 0.48, 0.48, 0.47, 0.46, 0.46] #deception de antoine
LdeltaIout = [0.24, 0.16, 0.18, 0.12, 0.104, 0.072, 0.06, 0.044, 0.04]


#a, b, c = numpy.polyfit(Lalpha, LVout, 2)
#Lfit2 = [a*i**2 + b*i + c for i in Ll]

plt.plot(Ll, LdeltaIout, "r")
#plt.plot(Ll, Lfit2, "b--")
plt.xlabel("L")
plt.ylabel("Delta Iout")
plt.title("Delta Iout = f(L)")
plt.show()

V = 230

LP = [2100, 1800, 1600, 1100, 900, 700, 400, 200, 100]
LIout2 = [0.75, 0.67, 0.57, 0.48, 0.41, 0.33, 0.21, 0.11, 0.08]
LdeltaIout2 = [0.192, 0.2, 0.2, 0.2, 0.208, 0.2, 0.184, 0.176, 0.144]
LdeltaIoutpourcent = [(d)/I for I,d in zip(LIout2[:-2], LdeltaIout2[:-2])]
LR = [(V**2)/p for p in LP]

plt.plot(LR, LIout2, "r")
plt.xlabel("R")
plt.ylabel("Iout")
plt.title("Iout = f(R)")
plt.show()

# Q2.12

LR_ = [1/r for r in LR]
LfL_ = [1/(500*l) for l in Ll]

plt.plot(LR_[:-2], LdeltaIoutpourcent, "r")
plt.xlabel("1/R")
plt.ylabel("Delta Iout")
plt.title("DeltaIout = f(1/R)")
plt.show()

# a, b, c, e, f = numpy.polyfit(LfL_[:-2],LdeltaIoutpourcent, 4)
# Lxfit = [0.002 + n/10000 for n in range(150)]
# LfitIout = [a*d**4 + b*d**3 + c*d**2 + e*d + f for d in Lxfit]

# #plt.plot(LfL_[:-2], LdeltaIoutpourcent, "r")
# plt.plot(Lxfit, LfitIout, 'b--')
# plt.xlabel("1/fL")
# plt.ylabel("Delta Iout")
# plt.title("DeltaIout = f(1/fL)")
# plt.show()


plt.plot(LfL_[:-2], LdeltaIoutpourcent, "r")
#plt.plot(LfL_[:-2], LfitIout, 'b--')
plt.xlabel("1/fL")
plt.ylabel("Delta Iout")
plt.title("DeltaIout = f(1/fL)")
plt.show()

LdeltaIout3 = [0.188, 0.104, 0.07, 0.056, 0.048, 0.024]
Lf = [500, 1000, 2000, 3000, 4000, 5000]

Lf_ = [1/f for f in Lf]

plt.plot(Lf_, LdeltaIout3, "r")
plt.xlabel("1/f")
plt.ylabel("Delta Iout")
plt.title("DeltaIout = f(1/f)")
plt.show()

