import matplotlib.pyplot as plt
import numpy as np

Ll_1 = [0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3]
LVout = [29.46, 30.84, 33.85, 36.14, 37.84, 39.46, 40.47, 41.3, 41.95, 42.5, 42.9, 43.4, 43.8]
LIout = [0.303, 0.281, 0.235, 0.201, 0.174, 0.151, 0.135, 0.122, 0.111, 0.102, 0.094, 0.087, 0.082]

plt.plot(Ll_1, LVout, "r", label = "Vout")
plt.legend(loc = "best")
plt.xlabel("L")
plt.ylabel("Vout")
plt.title("Vout = f(L)")
plt.show()


Lvout_iout1 = [v/i for v,i in zip(LVout, LIout)]

plt.plot(Ll_1, Lvout_iout1, "r", label = "Vout/Iout")
plt.legend(loc = "best")
plt.xlabel("L")
plt.ylabel("Vout/Iout")
plt.title("Vout/Iout = f(L)")
plt.show()


Ll_1 = [0.15, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3]
LVout = [25.60, 25.63, 25.72, 25.75, 25.79, 25.80, 25.80, 25.78, 25.74, 25.8]
LIout = [0.276, 0.255, 0.194, 0.153, 0.127, 0.102, 0.088, 0.078, 0.068, 0.061]

Lvout_iout2 = [v/i for v,i in zip(LVout, LIout)]

plt.plot(Ll_1[:10], Lvout_iout1[:10], "r", label = "1 diode")
plt.plot(Ll_1[:10], Lvout_iout2, "b", label = "2 diodes")
plt.legend(loc = "best")
plt.xlabel("L")
plt.ylabel("Vout/Iout")
plt.title("Vout/Iout = f(L)")
plt.show()
