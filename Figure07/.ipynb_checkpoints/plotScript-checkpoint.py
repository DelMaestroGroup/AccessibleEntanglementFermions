#Top Plot: One Particle Entanglement entropy dependence on the interaction potential
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import numpy as np
import matplotlib.pyplot as plt
import colors
from matplotlib import gridspec

orange = ["#ff8c00"]
blue = ["#4173b3"]

alpha = [0.2,0.1,0.0]
beta = [1.0,0.6,0.2]

for i,c in enumerate(alpha):
        orange.append(colors.get_alpha_hex(orange[0],beta[i]))
        blue.append(colors.get_alpha_hex(blue[0],beta[i]))

with plt.style.context('../IOP_large.mplstyle'):
    
    #Load filling fractions
    fillingFractions = [i/28 for i in range(1,15)]
    
    #Save Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables
    
    s1opVNEG100M28l14 = np.loadtxt("VNEG100M28l14.dat")[:,3]
    s1opVNEG100M28lN = np.loadtxt("VNEG100M28lN.dat")[:,3]
    s1opVNEG1d5M28l14 = np.loadtxt("VNEG1.5M28l14.dat")[:,3]
    s1opVNEG1d5M28lN = np.loadtxt("VNEG1.5M28lN.dat")[:,3]
    s1opV100M28l14 = np.loadtxt("V100M28l14.dat")[:,3]
    s1opV100M28lN = np.loadtxt("V100M28lN.dat")[:,3]
    
    s2opVNEG100M28l14 = np.loadtxt("VNEG100M28l14.dat")[:,8]
    s2opVNEG100M28lN = np.loadtxt("VNEG100M28lN.dat")[:,8]
    s2opVNEG1d5M28l14 = np.loadtxt("VNEG1.5M28l14.dat")[:,8]
    s2opVNEG1d5M28lN = np.loadtxt("VNEG1.5M28lN.dat")[:,8]
    s2opV100M28l14 = np.loadtxt("V100M28l14.dat")[:,8]
    s2opV100M28lN = np.loadtxt("V100M28lN.dat")[:,8]
    
    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    #gs = gridspec.GridSpec(2, 2, height_ratios=[20,20])
    gs = gridspec.GridSpec(2, 3)


    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    ax1.plot(fillingFractions, s1opVNEG100M28lN, '.', label=r'$S_{1}^{\rm{op}}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax1.plot(fillingFractions, s2opVNEG100M28lN, '.', label=r'$S_{2}^{\rm{op}}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax1.plot(fillingFractions, s1opVNEG100M28lN, '-', label=r'$S_{1}^{\rm{op}}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax1.plot(fillingFractions, s2opVNEG100M28lN, '-', label=r'$S_{2}^{\rm{op}}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax1.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax1.set_ylim(-0.1, 1.1)
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='off', labelleft='on', direction = 'in',labelsize='4',labelbottom='off')
    ax1.set_ylabel(r'$S$')
    ax1.text(0.085,0.99, r'$V/t=-100,\ell = N$', fontsize=4)
 
    ax2 = plt.subplot(gs[1])
    ax2.plot(fillingFractions, s1opVNEG1d5M28lN , '.', label=r'$S_{1}^{op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax2.plot(fillingFractions, s2opVNEG1d5M28lN, '.', label=r'$S_{2}^{op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax2.plot(fillingFractions, s1opVNEG1d5M28lN , '-', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax2.plot(fillingFractions, s2opVNEG1d5M28lN, '-', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax2.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax2.set_ylim(-0.1, 1.1)
    ax2.tick_params(axis='both', which='both', left='off', right='off', top='off', bottom='off', labelleft='off', labelbottom='off')
    ax2.text(0.045,0.99, r'$V/t=-1.5,\ell = N$', fontsize=4)
 
    #Legend
    lgnd = plt.legend(loc=(0.3,0.45),fontsize=5,frameon=False,handlelength=1,handleheight=1)
    
    ax3 = plt.subplot(gs[2])
    ax3.plot(fillingFractions, s1opV100M28lN , '.', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax3.plot(fillingFractions, s2opV100M28lN, '.', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax3.plot(fillingFractions, s1opV100M28lN , '-', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax3.plot(fillingFractions, s2opV100M28lN, '-', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax3.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax3.set_ylim(-0.1, 1.1)
    ax3.tick_params(axis='both', which='both', left='off', right='off', top='off', bottom='off', labelleft='off', labelbottom='off')
    ax3.text(0.045,0.99, r'$V/t=100,\ell = N$', fontsize=4)

    ax4 = plt.subplot(gs[3])
    ax4.plot(fillingFractions, s1opVNEG100M28l14, '.', label=r'$S_{1}^{\rm op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax4.plot(fillingFractions, s2opVNEG100M28l14, '.', label=r'$S_{2}^{\rm op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax4.plot(fillingFractions, s1opVNEG100M28l14, '-', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax4.plot(fillingFractions, s2opVNEG100M28l14, '-', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax4.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax4.set_ylim(-0.1, 1.1)
    ax4.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in',labelsize='4')
    ax4.set_xlabel(r'$f$')
    ax4.set_ylabel(r'$S$')
    ax4.text(0.085,0.99, r'$V/t=-100,\ell = L/2$', fontsize=4)

    ax5 = plt.subplot(gs[4])
    ax5.plot(fillingFractions, s1opVNEG1d5M28l14, '.', label=r'$S_{1}^{op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax5.plot(fillingFractions, s2opVNEG1d5M28l14, '.', label=r'$S_{2}^{op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax5.plot(fillingFractions, s1opVNEG1d5M28l14, '-', label=r'$S_{1}^{op}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax5.plot(fillingFractions, s2opVNEG1d5M28l14, '-', label=r'$S_{2}^{op}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax5.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax5.set_ylim(-0.1, 1.1)
    ax5.tick_params(axis='both', which='both', left='off', right='off', top='off', bottom='on', labelleft='off', direction = 'in',labelsize='4')
    ax5.set_xlabel(r'$f$')
    ax5.text(0.045,0.99, r'$V/t=-1.5,\ell = L/2$', fontsize=4)
    
    ax6 = plt.subplot(gs[5])
    ax6.plot(fillingFractions, s1opV100M28l14, '.', label=r'$S_{1}^{op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax6.plot(fillingFractions, s2opV100M28l14, '.', label=r'$S_{2}^{op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax6.plot(fillingFractions, s1opV100M28l14, '-', label=r'$S_{1}^{op}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax6.plot(fillingFractions, s2opV100M28l14, '-', label=r'$S_{2}^{op}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax6.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax6.set_ylim(-0.1, 1.1)
    ax6.tick_params(axis='both', which='both', left='off', right='off', top='off', bottom='on', labelleft='off', direction = 'in',labelsize='4')
    ax6.set_xlabel(r'$f$')
    ax6.text(0.045,0.99, r'$V/t=100,\ell = L/2$', fontsize=4)
    
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.050)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.040)
    
    plt.savefig('fillingFractionDependence.pdf', transparent=False)
    plt.show()
