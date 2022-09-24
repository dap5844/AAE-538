# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 15:52:15 2022

@author: User
"""

#AAE538 HW2 Problem 3

import numpy as np

atl = 10 #km
Ta = 223.3 #K
Pa = 0.265e5 #Pa
f = 0.02
Ae_ma = 0.006 #m^2*s/kg
Ve = 570 #m/s
Pe = 0.6e5
M = 0.8
gamma = 1.4
R = 287

#Calculate speed of air
a = np.sqrt(gamma*R*Ta)
V0 = M*a
rho = Pa / (R*Ta)
mdot_0 = rho*V0*ai

T_ma = (1+f)*Ve - V0
print(f"The specific thrust is {T_ma} m/s.")

