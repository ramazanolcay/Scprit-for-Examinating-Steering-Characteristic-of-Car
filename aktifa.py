# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 17:45:30 2021

@author: ramazanolcay
"""
import numpy as np
import matplotlib.pyplot as plt
import math

W= 1205+75+75 #Total weight, and 75+75 kg is for standart human body (2 people)
g=9.81
W *= g
La=1.805 #Distance of center of gravity to front axle
L= 2.605 #Wheelbase
Lö=0.800 #Distance of center of gravity to rear axle

sö=1.540 #Vehicle front track width
sa=1.540 #Vehicle rear track width

Wö = W  * (La/L) #front axle load
Wa = W  * (Lö/L) #rear axle load

h=850 #Height of center of gravity above ground
rst = ((215*(0.6))+((17/2)*25.4)) #Tyre rst
hl = h - rst
hl /= 1000 

pö=0 #Front axle yaw center height
pa=0.49 #Rear axle yaw center height

ha= 0.49 #Rear axle center of gravity height
hö= 0.36 #Front axle center of gravity height

q=75 #A bend with a radius of 75 m


Caö= (2500*180) / math.pi #crossover coefficient of motion for front
Caa = (1400*180) / math.pi #crossover coefficient of motion for rear

Ca=29000 # rear roll stiffness value for 1
Cö=50000 # front roll stiffness value for 1

V = np.arange(0,51) #Velocity values
c1=0.01 #adding a constant coefficient

a = (V*V)/(g*q) #acceleration coefficient

#calculation of freight transfers
Fzö = W * (((La/L)*(pö/sö)) + ((Wö/W)*(hö/sö)) + ((Cö*hl)/((Cö + Ca - (W*hl))*sö))) * a
Fza = W * (((Lö/L)*(pa/sa)) + ((Wa/W)*(ha/sa)) + ((Ca*hl)/((Cö + Ca - (W*hl))*sa))) * a

#angle
sapma_aci = (L/q) + (((Wö/Caö) - (Wa/Caa) + ((2*Wö*c1*(Fzö*Fzö))/(Caö*Caö)) - ((2*Wa*c1*(Fza*Fza))/(Caa*Caa)))*a)


#Same calculations for 2 with different Cö
Ca=29000
Cö=55000
Fzö = W * (((La/L)*(pö/sö)) + ((Wö/W)*(hö/sö)) + ((Cö*hl)/((Cö + Ca - (W*hl))*sö))) * a
Fza = W * (((Lö/L)*(pa/sa)) + ((Wa/W)*(ha/sa)) + ((Ca*hl)/((Cö + Ca - (W*hl))*sa))) * a
sapma_aci1 = (L/q) + (((Wö/Caö) - (Wa/Caa) + ((2*Wö*c1*(Fzö*Fzö))/(Caö*Caö)) - ((2*Wa*c1*(Fza*Fza))/(Caa*Caa)))*a)

#Same calculations for 3 with different Ca
Ca=32000
Cö=50000
Fzö = W * (((La/L)*(pö/sö)) + ((Wö/W)*(hö/sö)) + ((Cö*hl)/((Cö + Ca - (W*hl))*sö))) * a
Fza = W * (((Lö/L)*(pa/sa)) + ((Wa/W)*(ha/sa)) + ((Ca*hl)/((Cö + Ca - (W*hl))*sa))) * a
sapma_aci2 = (L/q) + (((Wö/Caö) - (Wa/Caa) + ((2*Wö*c1*(Fzö*Fzö))/(Caö*Caö)) - ((2*Wa*c1*(Fza*Fza))/(Caa*Caa)))*a)


#GRAPH
plt.ylim(-0.01,0.08,0.01)

plt.plot(V, sapma_aci1, color="blue", linewidth=3.0, linestyle="-", label="1", marker=(8), markersize=2)
plt.plot(V, sapma_aci,  color="red", linewidth=3.0, linestyle="-", label="2", marker=(8), markersize=2)
plt.plot(V, sapma_aci2, color="green", linewidth=3.0, linestyle="-", label="3", marker=(8), markersize=2)
plt.tick_params(axis='both', which='both')
plt.xticks(np.arange(0,51,2), fontsize=9, rotation=90)
plt.legend(loc='lower left', prop={'size':10})
plt.title('Speed – Wheel Angle Diagram')
plt.ylabel("Wheel Angle [rad]")
plt.xlabel("Speed [m/s]")
plt.grid(True)
plt.savefig("Diyagram.png")
plt.show()
plt.close()

