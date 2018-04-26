#Top Plot: One Particle Entanglement entropy dependence on the interaction potential
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

with plt.style.context('../IOP_large.mplstyle'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files

    datFileHalfChainVT2 = 'fillingFractionsHalfChainPartitionVT2.dat'
    dataHalfChainVT2 = np.loadtxt(datFileHalfChainVT2)

    datFileHalfChainVT100 = 'fillingFractionsHalfChainPartitionVT100.dat'
    dataHalfChainVT100 = np.loadtxt(datFileHalfChainVT100)

    datFilePartNumChainVT2 = 'fillingFractionsParticleNumPartitionVT2.dat'
    dataPartNumVT2 = np.loadtxt(datFilePartNumChainVT2)

    datFilePartNumChainVT100 = 'fillingFractionsParticleNumPartitionVT100.dat'
    dataPartNumVT100 = np.loadtxt(datFilePartNumChainVT100)

    #Load filling fractions
    fillingFractions = dataHalfChainVT2[:,0]

    #Save Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables


    s1HalfChainVT2Spatial = dataHalfChainVT2[:,3]
    s2HalfChainVT2Spatial = dataHalfChainVT2[:,5]
    s1HalfChainVT2Operational = dataHalfChainVT2[:,4]
    s2HalfChainVT2Operational = dataHalfChainVT2[:,6]
    
    s1HalfChainVT100Spatial = dataHalfChainVT100[:,3]
    s2HalfChainVT100Spatial = dataHalfChainVT100[:,5]
    s1HalfChainVT100Operational = dataHalfChainVT100[:,4]
    s2HalfChainVT100Operational = dataHalfChainVT100[:,6]
    
    s1PartNumVT2Spatial = dataPartNumVT2[:,3]
    s2PartNumVT2Spatial = dataPartNumVT2[:,5]
    s1PartNumVT2Operational = dataPartNumVT2[:,4]
    s2PartNumVT2Operational = dataPartNumVT2[:,6]
    
    s1PartNumVT100Spatial = dataPartNumVT100[:,3]
    s2PartNumVT100Spatial = dataPartNumVT100[:,5]
    s1PartNumVT100Operational = dataPartNumVT100[:,4]
    s2PartNumVT100Operational = dataPartNumVT100[:,6]


    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 2, height_ratios=[20,20])

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    ax1.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point
    ax1.plot(fillingFractions, s1PartNumVT2Spatial, '.', label=r'$S_{1}$', linewidth = 1, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax1.plot(fillingFractions, s2PartNumVT2Spatial, '.', label=r'$S_{2}$', linewidth = 1, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax1.plot(fillingFractions, s1PartNumVT2Operational, '.', label=r'$S_{1}^{op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax1.plot(fillingFractions, s2PartNumVT2Operational, '.', label=r'$S_{2}^{op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax1.plot(fillingFractions, s1PartNumVT2Spatial, '-', label=r'$S_{1}$', linewidth = 0.5, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax1.plot(fillingFractions, s2PartNumVT2Spatial, '-', label=r'$S_{2}$', linewidth = 0.5, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax1.plot(fillingFractions, s1PartNumVT2Operational, '-', label=r'$S_{1}^{op}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax1.plot(fillingFractions, s2PartNumVT2Operational, '-', label=r'$S_{2}^{op}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax1.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax1.set_ylim(-0.1, 1.65)
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='off', labelleft='on', direction = 'in',labelsize='4')
    ax1.set_ylabel(r'$S$')
    ax1.text(0.34,0.01, r'$V/t=2,\ell = N$', fontsize=4)
    plt.yticks([0.0,0.5,1.0,1.5])

    
    ax2 = plt.subplot(gs[1])
    ax2.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point
    ax2.plot(fillingFractions, s1PartNumVT100Spatial, '.', label=r'$S_{1}$', linewidth = 1, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax2.plot(fillingFractions, s2PartNumVT100Spatial, '.', label=r'$S_{2}$', linewidth = 1, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax2.plot(fillingFractions, s1PartNumVT100Operational, '.', label=r'$S_{1}^{op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax2.plot(fillingFractions, s2PartNumVT100Operational, '.', label=r'$S_{2}^{op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax2.plot(fillingFractions, s1PartNumVT100Spatial, '-', label=r'$S_{1}$', linewidth = 0.5, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax2.plot(fillingFractions, s2PartNumVT100Spatial, '-', label=r'$S_{2}$', linewidth = 0.5, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax2.plot(fillingFractions, s1PartNumVT100Operational, '-', label=r'$S_{1}^{op}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax2.plot(fillingFractions, s2PartNumVT100Operational, '-', label=r'$S_{2}^{op}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax2.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax2.set_ylim(-0.1, 1.65)
    ax2.tick_params(axis='both', which='both', left='off', right='off', top='off', bottom='off', labelleft='off', direction = 'in')
    ax2.text(0.34,0.01, r'$V/t=100,\ell = N$', fontsize=4)


    ax3 = plt.subplot(gs[2])
    ax3.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point
    ax3.plot(fillingFractions, s1HalfChainVT2Spatial, '.', label=r'$S_{1}$', linewidth = 1, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax3.plot(fillingFractions, s2HalfChainVT2Spatial, '.', label=r'$S_{2}$', linewidth = 1, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax3.plot(fillingFractions, s1HalfChainVT2Operational, '.', label=r'$S_{1}^{\rm op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax3.plot(fillingFractions, s2HalfChainVT2Operational, '.', label=r'$S_{2}^{\rm op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax3.plot(fillingFractions, s1HalfChainVT2Spatial, '-', linewidth = 0.5, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax3.plot(fillingFractions, s2HalfChainVT2Spatial, '-', linewidth = 0.5, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax3.plot(fillingFractions, s1HalfChainVT2Operational, '-', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax3.plot(fillingFractions, s2HalfChainVT2Operational, '-', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax3.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax3.set_ylim(-0.1, 1.65)
    ax3.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in',labelsize='4')
    ax3.set_xlabel(r'$f$')
    ax3.set_ylabel(r'$S$')
    ax3.text(0.32,0.13, r'$V/t=2,\ell = L/2$', fontsize=4)
    plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5])
    plt.yticks([0.0,0.5,1.0,1.5])



    #Legend
    lgnd = plt.legend(loc=(0.055,1.75),fontsize=3,frameon=False,handlelength=1,handleheight=1)
    
    ax4 = plt.subplot(gs[3])
    ax4.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point
    ax4.plot(fillingFractions, s1HalfChainVT100Spatial, '.', label=r'$S_{1}$', linewidth = 1, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax4.plot(fillingFractions, s2HalfChainVT100Spatial, '.', label=r'$S_{2}$', linewidth = 1, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax4.plot(fillingFractions, s1HalfChainVT100Operational, '.', label=r'$S_{1}^{op}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5')
    ax4.plot(fillingFractions, s2HalfChainVT100Operational, '.', label=r'$S_{2}^{op}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5')
    ax4.plot(fillingFractions, s1HalfChainVT100Spatial, '-', linewidth = 0.5, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax4.plot(fillingFractions, s2HalfChainVT100Spatial, '-', label=r'$S_{2}$', linewidth = 0.5, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax4.plot(fillingFractions, s1HalfChainVT100Operational, '-', label=r'$S_{1}^{op}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax4.plot(fillingFractions, s2HalfChainVT100Operational, '-', label=r'$S_{2}^{op}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax4.set_xlim(fillingFractions[0]-0.01, fillingFractions[-1]+0.01)
    ax4.set_ylim(-0.1, 1.65)
    ax4.tick_params(axis='both', which='both', left='off', right='off', top='off', bottom='on', labelleft='off', direction = 'in',labelsize='4')
    ax4.set_xlabel(r'$f$')
    ax4.text(0.32,0.13, r'$V/t=100,\ell = L/2$', fontsize=4)
    plt.xticks([0.1, 0.2, 0.3, 0.4, 0.5])

   
   
   
  
    #Legend
    #lgnd = plt.legend(loc=(0.04,0.3),fontsize=7,handlelength=3,handleheight=2, frameon=False)

    #lgnd.get_title().set_fontsize(7)
    #lgnd.get_title().set_position((12,0))
    
    #Remove numbers from real axes of top plots
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=True)
    plt.setp(ax3.get_xticklabels(), visible=True)
    plt.setp(ax4.get_xticklabels(), visible=True)
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.050)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.040)
    
    plt.savefig('fillingFractionDependence.pdf', transparent=False)
    plt.show()
