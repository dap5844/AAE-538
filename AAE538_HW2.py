# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 13:43:58 2022

@author: User
"""

import numpy as np
import matplotlib.pyplot as plt

#Inlet conditions
ai = 0.235 #m^2
ae = 0.25 #m^2
f= 0.02
Pe = 200e3 #Pa
Ve = 600 #m/s

#Amb conditions
Pa = 30.8e3 #Pa
Ta = 229.74 #K
alt = 9 #km
num = 20
V = np.linspace(500, 6000, num)*0.277778 # m/s, the 0.278 is for converting from km/h to m/s
R = 287 # J/kg*K
rho = Pa / (R*Ta)

#Case a) constant mdot
print("Plots for part a) of Problem 1")
mdot = 40 #kg/s
#Momentum drag
V0 = V
D = mdot * V0

#Pressure Thrust
F_p = (Pe - Pa) * ae

#Gross Thrust
F_g = mdot * ((1 + f)*Ve) + F_p

#Net Thrust
F_n = F_g - D

#Plotting for part a)
plt.title('Velocity vs Drag')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Drag (kN)')
plt.grid(True)
plt.plot(V,D/1000)
plt.show()

plt.title('Velocity vs Net Thrust')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Net Thrust (kN)')
plt.grid(True)
plt.plot(V,F_n/1000)
plt.show()

#Case b) varying mdot
print("Plots for part b) of Problem 1")

for i in range(num):
#Momentum drag
    mdot = rho * V * ai
    V0 = V
    D = mdot * V0

#Pressure Thrust
    F_p = (Pe - Pa) * ae

#Gross Thrust
    F_g = mdot * ((1 + f)*Ve) + F_p

#Net Thrust
    F_n = F_g - D
#    print(f"Mdot is {mdot}")
#    print(f"Vo is: {V0}")
#    print(f"Drag is: {D}")
#    print(F_n)

plt.title('Velocity vs Drag')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Drag (kN)')
plt.grid(True)
plt.plot(V0,D/1000)
plt.show()

#plt.title('Velocity vs Mass Flow Rate')
#plt.xlabel('Velocity (m/s)')
#plt.ylabel('Mdot (kg/s)')
#plt.plot(V, mdot)
#plt.show()

plt.title('Velocity vs Gross Thrust')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Gross Thrust (kN)')
plt.grid(True)
plt.plot(V0,F_g/1000)
plt.show()
#
plt.title('Velocity vs Net Thrust')
plt.xlabel('Velocity (m/s)')
plt.ylabel('Net Thrust (kN)')
plt.grid(True)
plt.plot(V,F_n/1000)
plt.show()
