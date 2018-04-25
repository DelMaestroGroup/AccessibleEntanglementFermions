#Top Plot: One Particle Entanglement entropy dependence on the interaction potential
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec

with plt.style.context('IOP_large.mplstyle'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files

    #datFileNEG_M28N14 = 'NA28F14n1NEGu.03_100l_ifP.dat'
    #dataNEG_M28N14 = np.loadtxt(datFileNEG_M28N14)

    #datFile_M28N14 = 'NA28F14n1u.03_100l_ifP.dat'
    #data_M28N14 = np.loadtxt(datFile_M28N14)

    datFileNEG_M26N13 = 'EOPA28F14l14NEG.dat'
    dataNEG_M26N13 = np.loadtxt(datFileNEG_M26N13)

    datFile_M26N13 = 'EOPA28F14l14.dat'
    data_M26N13 = np.loadtxt(datFile_M26N13)

    #Load energies
    energiesNEG = dataNEG_M26N13[:,0]
    energies = data_M26N13[:,0]

    #Save Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables
    #M=28, N=14
    #s1NEG_M28N14 = dataNEG_M28N14[:,2]
    #s1_M28N14 = data_M28N14[:,2]

    #s2NEG_M28N14 = dataNEG_M28N14[:,3]
    #s2_M28N14 = data_M28N14[:,3]

    #M=26, N=13
    s1NEG_M26N13_Spatial = dataNEG_M26N13[:,2]
    s1_M26N13_Spatial = data_M26N13[:,2]

    s2NEG_M26N13_Spatial = dataNEG_M26N13[:,4]
    s2_M26N13_Spatial = data_M26N13[:,4]

    s1NEG_M26N13_Operational = dataNEG_M26N13[:,3]
    s1_M26N13_Operational = data_M26N13[:,3]
    
    s2NEG_M26N13_Operational = dataNEG_M26N13[:,5]
    s2_M26N13_Operational = data_M26N13[:,5]

    #Saves entropies for the inset to variables
    #s1_M28N14_3_3 = data_M28N14_3_3[:,2]
    #s2_M28N14_3_3 = data_M28N14_3_3[:,3]

    #s1_M26N13_3_3 = data_M26N13_3_3[:,2]
    #s2_M26N13_3_3 = data_M26N13_3_3[:,3]


    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(1, 2, height_ratios=[1])

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    #ax1 = fig.add_subplot(221)
    ax1.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point
    #ax1.plot(energiesNEG, s1NEG_M28N14, '-',  label='1, 14', linewidth = 1, color='#5e4ea2')
    #ax1.plot(energiesNEG, s2NEG_M28N14, '-',  label='2, 14', linewidth = 1, color='#7dcba4')
    #ax1.plot(energiesNEG, s1NEG_M26N13_Spatial, '.', label=r'$S_{1}^{Sp}$', linewidth = 2,markeredgewidth=1,markeredgecolor='#e95c47', markerfacecolor='None')
    ax1.plot(energiesNEG, s1NEG_M26N13_Spatial, '.', label=r'$S_{1}$', linewidth = 1, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax1.plot(energiesNEG, s2NEG_M26N13_Spatial, '.', label=r'$S_{2}$', linewidth = 1, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax1.plot(energiesNEG, s1NEG_M26N13_Operational, '.', label=r'$S_{1}^{\rm op}$', linewidth = 1, color='#4173b3', markeredgewidth='0.5')
    ax1.plot(energiesNEG, s2NEG_M26N13_Operational, '.', label=r'$S_{2}^{\rm op}$', linewidth = 1, color='#ff8c00', markeredgewidth='0.5')
    ax1.set_xlim(-energies[-1], -energies[0])
    ax1.set_ylabel(r'$S_{\alpha}(\ell)$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', left='on', top='off',labelleft='on', direction = 'in')
    ax1.set_xscale('symlog', linthreshx = 0.000001)
    ax1.set_ylim(0.0,3.7)
    ax1.set_xlim(-100,-0.029)
    #ax1.set_ylim(-0.15,7.8)
    ax1.set_xlabel(r'$V/t$',x=1)
    ax1.set_title(r'$M=28, N=14, \ell=14$',x=1)



    #Legend
    #Legend
    #lgnd = plt.legend(loc=(0.04,0.5),fontsize=7,handlelength=1,handleheight=1, frameon=False)
    lgnd = plt.legend(loc=(0.04,0.5),fontsize=7,handlelength=1,handleheight=1, frameon=False)
    
    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    #ax2 = fig.add_subplot(222)
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction = 'in')
    ax2.plot(energies, s1_M26N13_Spatial, '.', label='1, 13', linewidth = 1, color='#4173b3', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax2.plot(energies, s2_M26N13_Spatial, '.', label='2, 13', linewidth = 1, color='#ff8c00', markerfacecolor = 'w', markeredgewidth = '0.5')
    ax2.plot(energies, s1_M26N13_Operational, '.', label='1, 13', linewidth = 1, color='#4173b3', markeredgewidth='0.5')
    ax2.plot(energies, s2_M26N13_Operational, '.', label='2, 13', linewidth = 1, color='#ff8c00', markeredgewidth='0.5')
    ax2.set_xlim(energies[0], energies[-1])
    ax2.set_xscale('symlog', linthreshx = 0.000001)
    ax2.set_ylim(0.0,3.7)
    ax2.set_xlim(0.029,100)
    #ax2.set_ylim(-0.15,7.8)
    #ax2.set_xlabel(r'$V/t$')
    
    #Remove numbers from real axes of top plots
    plt.setp(ax1.get_xticklabels(), visible=True)
    plt.setp(ax2.get_xticklabels(), visible=True)
    
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)
    
    #plt.savefig('EOPFigureNEGPOS28F14l14.pdf', transparent=False)
    #plt.savefig('EOPFigureNEGPOS28F14l14_noOP.pdf', transparent=False)

    plt.show()
