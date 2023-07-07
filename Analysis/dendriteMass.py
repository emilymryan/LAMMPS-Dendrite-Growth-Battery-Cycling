#import matplotlib
#matplotlib.use('Agg')
#from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
#import sys

#fname = sys.argv[1]

job = 'bvCC2_4286316'
#fname = '/projectnb/ryanlab/tmelsh/chargingProfiles/lammpsUpdate/results/pulse/'+ job
fname = '/projectnb/ryanlab/tmelsh/chargingProfiles/final/results/bvCC/'+ job

Nfreq = 14400
totDump = 144
dumpT = 0.05
time = 0
totAtoms = 180000
length = np.zeros((totAtoms,1),dtype=float)
Lay = 0.06
Lmax = 0.0 #initialize
solid = 0 #initialize
Ltemp = 0.0 #initialize

def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

##Create array to hold mass and time mass[dendrite_mass,time]
##Mass is in index 6 of dump file (double check!)
##Assumes fluid mass is 0. Add one for t=0
#mass = np.zeros((totDump+1,2),dtype=float)
data = np.zeros((totDump,3),dtype=float)

#loop through 6000 dumps that start at 0 (subtract t=0 from loop)
for i in range(0,totDump):
    data[i,1] = time
    time = time + dumpT
    num = i*Nfreq
    fid = fname + "/dump." + str(num) + ".dat"
    d = np.loadtxt(fid, skiprows=9, usecols=5) #Double check!
    data[i,0] = np.sum(d)
    typ = np.loadtxt(fid, skiprows=9, usecols=1)
    y = np.loadtxt(fid, skiprows=9, usecols=3) #Double check!
    for j in range(0,totAtoms):
        if int(typ[j]) == int(2):
            Ltemp = y[j]
            length[j] = y[j]
            solid = 1 + solid
        if (Ltemp > Lmax):
            Lmax = Ltemp
    data[i,2] = round((Lmax - Lay),5)
    print(i)

#Save mass time and length data to csv
Data = pd.DataFrame(data)
Data.to_csv('bvCC2_4286316.csv',index=False)

##Plot mass growth vs. time
# plt.figure(figsize=(11,7),dpi=100);
# plt.plot(mass[:,1],mass[:,0],'r.')
# for i in my_range(0,totDump+1,100):
#     plt.plot(mass[i,1],mass[i,0],'bo',ms=3)
# plt.title('"Pulse Charging Trial 1 Dendrite Growth (mass vs. time)')
# plt.xlabel('Time (s)')
# plt.ylabel('Dendrite Mass Growth()')
# plt.axis([0, (T+1), 0, 0.002])
# plt.minorticks_on()
# plt.xticks(np.arange(0, (T+1),step=1))
# plt.grid(which='both', axis='both', linestyle='--')
#matplotlib.axes.Axes.set_axisbelow(True)


# plt.savefig( 'trial1_5098531.png', bbox_inches='tight')
