L1_1 = {'Vin': 64, 'Iin': 0.12, 'Vout': 32, 'Iout': 0.067, 'f': 51.58}

LfourierVout = [0, 27.5, 1.68, 7.71, 1.97, 5.12, 1.63, 3.48] #harmoniques d'ordres i
LfourierIout = [0, 146, 4.99, 17, 2.3, 5.93, 1.99, 2.3]

THDVout = sum([Vi**2 for Vi in LfourierVout[2:]])**0.5 / LfourierVout[1]
THDIout = sum([Vi**2 for Vi in LfourierIout[2:]])**0.5 / LfourierIout[1]
print(THDIout) #0.1306056988207583