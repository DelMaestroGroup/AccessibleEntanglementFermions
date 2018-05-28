#Plot an inset showing how the peak of Von Neumann
#Operational Entanglement moves closer to V/t=2
#as the particle number in the tV-chain increases

import numpy as np
import matplotlib.pyplot as plt
from math import e
from scipy.stats import chisquare
from scipy import stats
import colors

with plt.style.context('../IOP_large.mplstyle'):

    #Load Adrian's APS Colors
    red = ["#e85c47"]
    blue = ["#4173b3"]
    green = ["#7dcca4"]     #Actually orange
    orange = ["#fdbe6e"]    #Actually green

    beta = [0.8,0.5,0.1]

    for i,c in enumerate(beta):
            red.append(colors.get_alpha_hex(red[0],beta[i]))
            orange.append(colors.get_alpha_hex(orange[0],beta[i]))
            green.append(colors.get_alpha_hex(green[0],beta[i]))
            blue.append(colors.get_alpha_hex(blue[0],beta[i]))

#Load Data
dataN3 = np.loadtxt("EOPP6F3l3a2.dat")
dataN5 = np.loadtxt("EOPP10F5l5a2.dat")
dataN7 = np.loadtxt("EOPP14F7l7a2.dat")
dataN9 = np.loadtxt("EOPP18F9l9a2.dat")
dataN11 = np.loadtxt("EOPP22F11l11a2.dat")
dataN13 = np.loadtxt("EOPP26F13l13a2.dat")
dataN15 = np.loadtxt("EOPP30F15l15a2.dat")

xN3, yN3 = dataN3[:,0], dataN3[:,3]
xN5, yN5 = dataN5[:,0], dataN5[:,3]
xN7, yN7 = dataN7[:,0], dataN7[:,3]
xN9, yN9 = dataN9[:,0], dataN9[:,3]
xN11, yN11 = dataN11[:,0], dataN11[:,3]
xN13, yN13 = dataN13[:,0], dataN13[:,3]
xN15, yN15 = dataN15[:,0], dataN15[:,3]

#Plot
ax1 = plt.plot(xN3,yN3,label='3',color=blue[1])
ax1.plot(2, np.linspace(0,2))
ax2 = plt.plot(xN5,yN5,label='5',color=blue[1])
ax3 = plt.plot(xN7,yN7,label='7',color=blue[1])
ax4 = plt.plot(xN9,yN9,label='9',color=blue[1])
ax5 = plt.plot(xN11,yN11,label='11',color=blue[1])
ax6 = plt.plot(xN13,yN13,label='13',color=blue[1])
ax7 = plt.plot(xN15,yN15,label='15',color=blue[1])

#Mark position of peaks for each N
ax1 = plt.plot(3.1903119454707949,0.2335959173839680,marker='*',mfc=blue[3],color=blue[1])
ax2 = plt.plot(3.0716932401905814,0.3720450303814098,marker='X',mfc=blue[3],color=blue[1])
ax3 = plt.plot(2.9842038317092805,0.4634960193349440,marker='p',mfc=blue[3],color=blue[1])
ax4 = plt.plot(2.9211898989895535,0.5315254430302333,marker='d',mfc=blue[3],color=blue[1])
ax5 = plt.plot(2.8721517043926008,0.5856038496253868,marker='^',mfc=blue[3],color=blue[1])
ax6 = plt.plot(2.8258612507925038,0.6305148711748493,marker='s',mfc=blue[3],color=blue[1])
ax7 = plt.plot(2.7928168485370364,0.6689827690493597,marker='o',mfc=blue[3],color=blue[1])
ax7.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='off', direction = 'in')


plt.ylabel(r'$S_{1}^{\mathrm{op}}$')
plt.xlabel(r'$V/t$')
plt.legend(loc='best',title=r'$N$')
plt.savefig('inset.pdf')
