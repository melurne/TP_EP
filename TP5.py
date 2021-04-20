import matplotlib.pyplot as plt
import numpy as np

Ll = [0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
LIout = [1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04, 1.04]
LVout = [40.20, 40.12, 40.18, 40.18, 40.18, 40.18, 40.18, 40.20, 40.15, 40.17]
LVeff = [20.30, 20.3, 20.32, 20.37, 20.37, 20.40, 20.38, 20.38, 20.38, 20.39]
LIeff = [0.10, 0.10, 0.06, 0.04, 0.03, 0.02, 0.02, 0.01, 0.01, 0.01]

Vin_eff = 47.46
Iin_eff = 0.02

LP = [v*i for v,i in zip(LVout, LIout)]
LS = [Vin_eff*Iin_eff for veff,ieff in zip(LVeff, LIeff)]
print(LP)
print(LS)


Lfact = [P/S for P,S in zip(LP, LS)]

a, b = np.polyfit(Ll, Lfact, 1)
Lfit_fact = [a*l + b for l in Ll]


Vin_eff = 46.57


plt.plot(Ll, Lfact, 'r', label = 'facteur de puissance')
plt.plot(Ll, Lfit_fact, 'b--', label = 'fit')
plt.xlabel('L')
plt.ylabel('f')
plt.title('facteur de puissance = f(L)')
plt.show()

#2.7
Vout_1000 = 58.35
Vout_10000 = 60.7
#lim(Vout) = Vin_max ~ 65.86

#2.8
Vin_eff = 47.46
Iin_eff = 0.02
IRch = 1.2
r = 50

fact = (r*IRch**2)/(Vin_eff*Iin_eff)
print(fact)
