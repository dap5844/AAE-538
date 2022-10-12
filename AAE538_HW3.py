# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np

#Given quantities
P01 = 20 * 10**5 #in Pa
T01 = 1800 #K
P01_P3is = 3 
N = 13000 * 0.104719755 #Convert to rad/s. Had to add 0.5 correction factor to make it work.
gam = 1.3 
cp = 1007 #J/kg*K
R = 289 #J/kg*K
Gam = ((gam-1)/gam)
deg2rad = np.pi/180

#Geometry for Stator
r_sta_h = 0.69/2 #m
r_sta_t = 0.79/2 #m
angle_sta_i = 0
angle_sta_e = 71 * deg2rad
num_blades_sta = 45
sta_chord = 70
sta_loss = 2.7/100
R2 = (r_sta_t + r_sta_h)/2 
B2 = 37.1 * deg2rad #Beta 2 at stator
A2 = np.pi*(r_sta_t**2 - r_sta_h**2)

#Geometry for Rotor
r_rot_h = 0.68/2 #m
r_rot_t = 0.79/2 #m
angle_rot_i = -45 * deg2rad
angle_rot_e = -61 * deg2rad
num_blades_rot = 62 
rot_chord = 50
rot_loss = 5.4/100
R3 = (r_rot_t + r_rot_h)/2
alpha3 = -2.2 * deg2rad
B3 = angle_rot_e
A3 = np.pi*(r_rot_t**2 - r_rot_h**2)

#Stator values:

#First guess of Ps2
P2is = 10 * 10**5

#Initialize Mdot 2 and Mdot_3 for the while loop:
P2 = P2is
P3is = P01 / P01_P3is
P3 = P3is
#Calculate T2is
T02is = T01
T2is = T02is * (P2is/P01)**(Gam)
V2is = (2*cp*(T02is - T2is))**0.5
V2 = ((1-sta_loss)*V2is**2)**0.5
T2 = T02is - (V2**2)/(2*cp)
V2ax = V2 * np.cos(angle_sta_e)
V2tan = V2 * np.sin(angle_sta_e)
P02 = P2 * (T02is/T2)**(1/Gam)
U2 = N * R2
W2 = (V2ax**2 + (V2tan - U2)**2)**0.5
W2ax = W2 * np.cos(B2)
W2tan = W2 * np.sin(B2)

#T02R
T02R = T2 + (W2**2) / (2*cp)
P02R = (P2)*(T02R/T2)**(1/Gam)
##########################################################################

#Rotor Values

U3 = N * R3
#Rothalpy Equation to find T03R
# T3is = T01
T3is = T02R * (P3is/P02R)**Gam
T03R = (T02R + (U3**2 - U2**2)/(2*cp))
W3is = (2*cp*(T03R - T3is))**0.5
W3 = ((1-rot_loss)*W3is**2)**0.5
W3ax = W3 * np.cos(B3)
W3tan = W3 * np.sin(B3)
T3 = T03R - W3**2 / (2*cp)
P03R = P3is * (T03R/T3)**(1/Gam)
V3 = (W3ax**2 + (W3tan + U3)**2)**0.5
V3ax = V3 * np.cos(alpha3)
V3tan = V3 * np.sin(alpha3)
T03 = T3 + (V3**2) / (2*cp)
P03 = P3is * (T03/T3)**(1/Gam)

#Calculate Turbine Efficiency
Eff = (cp*(1- (T03/T01))) / (cp*(1 - (P3is / P01)**Gam))

#Get the mass flow rates at the stator and rotor
mdot_2 = A2 * (P2 / (R*T2)) * V2ax
mdot_3 = A3 * (P3 / (R*T3)) * W3ax



#Print all the stator values
print(f"\nStator Temperature values:\nT2,is is: {T2is:.1f} K")
print(f"T2 is: {T2:.1f} K")
print(f"T,02R is: {T02R:.1f} K")
print(f"\nStator Velocities:\nV2,is is: {V2is:.1f} m/s")
print(f"V2 is: {V2:.1f} m/s")
print(f"V2,ax is: {V2ax:.1f} m/s")
print(f"V2,tan is: {V2tan:.1f} m/s")
print(f"U2 is: {U2:.1f} m/s")
print(f"W2 is: {W2:.1f} m/s")
print(f"W2,ax is: {W2ax:.1f} m/s")
print(f"W2,tan is: {W2tan:.1f} m/s")
print(f"\nStator Pressures:\nP02 is: {P02/10**5:.2f} bar")
print(f"P,02R is: {P02R/10**5:.2f} bar")

#Print all the rotor values
print(f"\nRotor Temperature values:\nT3,is is: {T3is:.1f} K")
print(f"T3 is: {T3:.1f} K")
print(f"T03 is: {T03:.1f} K")
print(f"T03R is: {T03R:.1f} K")
print(f"\nRotor Pressures:\nP3,is is: {P3is/10**5:.2f} bar")
print(f"P03 is: {P03/10**5:.2f} bar")
print(f"P03R is: {P03R/10**5:.2f} bar")
print(f"\nRotor Velocities:V3 is: {V3:.1f} m/s")
print(f"U3 is: {U3:.1f} m/s")
print(f"V3 is: {V3:.1f} m/s")
print(f"W3,is is: {W3is:.1f} m/s")
print(f"W3 is: {W3:.1f} m/s")
print(f"W3ax is: {W3ax:.1f} m/s")
print(f"W3tan is: {W3tan:.1f} m/s")
print(f"V3ax is: {V3ax:.1f} m/s")
print(f"V3tan is: {V3tan:.1f} m/s")

print(f"\nThe turbine efficiency is: {Eff:.2f}")
print(f"\nThe stator MFR is: {mdot_2:.2f} kg/s")
print(f"The rotor MFR is: {mdot_3:.2f} kg/s")

#Misc calculations
a2 = (gam*R*T2)**0.5
a3 = (gam*R*T3)**0.5
M2_V2 = V2 / a2 #Mabs for 2
M2_W2 = W2 / a2 #Mrel for 2
M3_V3 = V3 / a3 #Mabs for 3
M3_W3 = W3 / a3 #Mrel for 2