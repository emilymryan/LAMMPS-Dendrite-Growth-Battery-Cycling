#import matplotlib
#matplotlib.use('Agg')
#from matplotlib import pyplot as plt
import numpy as np

import sys

fname = sys.argv[1]
#job = 'bvCC4_2479634/dump.1112740.dat'
#fname = '/projectnb/ryanlab/tmelsh/chargingProfiles/final/results/bvCC/'+ job
#fname = '/projectnb/ryanlab/tmelsh/chargingProfiles/lammpsUpdate/results/cc/'+ job

def my_range(start, end,step):
    while start <= end:
        yield start
        start += step

##parameters, length in micrometers
Ly = 5.0 #simulation box height
Lx = 2.5 #electrode length
neq = 30 #number of particles in the kernel
h = 1/neq #kernel radius for mass transport
dx = h/4 #particle spacing
Lay = 0.06 #anode thickness/length
totAtoms = 180000 #number of atoms
totMass = 0 #initialize
Lmax = 0.0 #initialize
solid = 0 #initialize
length = np.zeros((totAtoms,1),dtype=float)
Ltemp = 0.0 #initialize

##load data
typ = np.loadtxt(fname, skiprows=9, usecols=1)
y = np.loadtxt(fname, skiprows=9, usecols=3)
mass = np.loadtxt(fname, skiprows=9, usecols=5)

##loop through atoms, sort into solids, compile lengths, calculate max length
for i in range(0,totAtoms):
    if int(typ[i]) == int(2):
        Ltemp = y[i]
        length[i] = y[i]
        solid = 1 + solid
    if (Ltemp > Lmax):
        Lmax = Ltemp

Lmax = round((Lmax - Lay),5)    
print("Max Total Dendrite Length: " + str(Lmax) + " um\n")

#Lavg = round(float(sum(length))/solid - Lay,5)
#print("Average Dendrite Particle Location from Anode: " + str(Lavg) + " um\n")

##calculate dendrite density
density1 = round(sum(mass)/(Lx*Lmax),5)
print("Dendrite density from Lmax: " + str(density1) + " ug/um^2\n")

##dendrite mass deposited
mass = round(sum(mass),5)
print("Total dendrite mass: " + str(mass) + " ug\n")
