#Top Plot: One Particle Entanglement entropy dependence on the interaction potential
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import numpy as np
import matplotlib.pyplot as plt
import colors
from matplotlib import gridspec
from math import pi,e

orange = ["#ff8c00"]
#purple = ["#7dcca4"] #Actually green
purple = ["#e85c47"] #Actually red
#blue = ["#4173b3"]

beta = [0.9,0.6,0.2,0.05]

for i,c in enumerate(beta):
    orange.append(colors.get_alpha_hex(orange[0],beta[i]))
    purple.append(colors.get_alpha_hex(purple[0],beta[i]))

print(len(orange))


with plt.style.context('../IOP_large.mplstyle2'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files
    
    #13 particles

    #alpha=2
#    datFileNEG_M26N13 = 'Data/EOPP26F13l13a2NEG.dat'
    datFileNEG_M26N13 = 'Data/EOPP30F15l15a2NEG.dat'
    dataNEG_M26N13 = np.loadtxt(datFileNEG_M26N13)
    
#    datFile_M26N13 = 'Data/EOPP26F13l13a2.dat'
    datFile_M26N13 = 'Data/EOPP30F15l15a2.dat'
    data_M26N13 = np.loadtxt(datFile_M26N13)
    
    #alpha=4
    datFileNEG_M26N13a4 = 'Data/EOPP26F13l13a4NEG.dat'
    dataNEG_M26N13a4 = np.loadtxt(datFileNEG_M26N13a4)
    
    datFile_M26N13a4 = 'Data/EOPP26F13l13a4.dat'
    data_M26N13a4 = np.loadtxt(datFile_M26N13a4)

    #alpha=10
#    datFileNEG_M26N13a10 = 'Data/EOPP26F13l13a10NEG.dat'
    datFileNEG_M26N13a10 = 'Data/EOPP30F15l15a10NEG.dat'
    dataNEG_M26N13a10 = np.loadtxt(datFileNEG_M26N13a10)
    
#    datFile_M26N13a10 = 'Data/EOPP26F13l13a10.dat'
    datFile_M26N13a10 = 'Data/EOPP30F15l15a10.dat'
    data_M26N13a10 = np.loadtxt(datFile_M26N13a10)

    #Load energies
    energiesNEG_M26N13 = dataNEG_M26N13[:,0]
    energies_M26N13 = data_M26N13[:,0]

    #Save Operational Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables

    #13 particles

    #alpha=1,2
    s1NEG_M26N13 = dataNEG_M26N13[:,3]
    s1_M26N13 = data_M26N13[:,3]
    
    s2NEG_M26N13 = dataNEG_M26N13[:,5]
    s2_M26N13 = data_M26N13[:,5]

    #alpha=4
    s4NEG_M26N13 = dataNEG_M26N13a4[:,5]
    s4_M26N13 = data_M26N13a4[:,5]

    #alpha=10
    s10NEG_M26N13 = dataNEG_M26N13a10[:,5]
    s10_M26N13 = data_M26N13a10[:,5]

    #Exact Variance (With Luttinger Parameter Dependence)
    xNEG = np.linspace(-2,-0.03,1000)
    x = np.linspace(0.03,2,1000)
    
    K = pi/(2*np.arccos(-x/2))
    KNEG = pi/(2*np.arccos(-xNEG/2))
    
    l=13
    sigma2LLNEG = KNEG*np.log(l)/(2*pi) #\ell = partition size
    sigma2LL = K*np.log(l)/(2*pi)

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])

    ax1.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point

    #alpha=2
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,4]-dataNEG_M26N13[:,8], 'o',  label=r'$S_{2}-S_{2}^{\rm{op}}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,7], 'o',label=r'$H_2$', markersize = 1.5, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3])

    #alpha10
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13a10[:,4]-dataNEG_M26N13a10[:,8], 'o',  label=r'$S_{10}-S_{10}^{\rm{op}}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13a10[:,7], 'o',label=r'$H_{10}$', markersize = 1.5, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3])
    ax1.set_xlim(-energies_M26N13[-1], -energies_M26N13[0])
    ax1.set_ylim(0,2.8)
    ax1.set_ylabel(r'$\Delta S_{\alpha}$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax1.set_xlabel(' ')

    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')

    #alpha=2
    ax2.plot(energies_M26N13, data_M26N13[:,4]-data_M26N13[:,8], 'o',  label=r'$S_{2}-S_{2}^{\rm{op}}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax2.plot(energies_M26N13, data_M26N13[:,7], 'o',label=r'$H_2$', markersize = 1.5, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3])

    #alpha10
    ax2.plot(energies_M26N13, data_M26N13a10[:,4]-data_M26N13a10[:,8], 'o',  label=r'$S_{10}-S_{10}^{\rm{op}}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax2.plot(energies_M26N13, data_M26N13a10[:,7], 'o',label=r'$H_{10}$', markersize = 1.5, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3])

    ax2.text(0.04,2.5,r'$N$ = 15')
    ax2.set_xlim(energies_M26N13[0], energies_M26N13[-1])
    ax2.set_ylim(0,2.8)
    ax2.set_xscale('symlog', linthreshx = 0.000001)

    #Legend 
    lgnd = plt.legend(loc=(0.00,0.34),fontsize=9,handlelength=1,handleheight=2, frameon=False)

    #Inset Plot
    plt.subplots_adjust(wspace = 0.030)

    
#Bottom Plot: Operational entanglement entropies for even number of particles

    #Load data
    
    #14 particles
    
    #alpha=2
    datFileNEG_M28N14 = 'Data/EOPA28F14l14a2NEG.dat'
    dataNEG_M28N14 = np.loadtxt(datFileNEG_M28N14)
    
    datFile_M28N14 = 'Data/EOPA28F14l14a2.dat'
    data_M28N14 = np.loadtxt(datFile_M28N14)
     
    #alpha=4
    datFileNEG_M28N14a4 = 'Data/EOPA28F14l14a4NEG.dat'
    dataNEG_M28N14a4 = np.loadtxt(datFileNEG_M28N14a4)
    
    datFile_M28N14a4 = 'Data/EOPA28F14l14a4.dat'
    data_M28N14a4 = np.loadtxt(datFile_M28N14a4)

    #alpha=10
    datFileNEG_M28N14a10 = 'Data/EOPA28F14l14a10NEG.dat'
    dataNEG_M28N14a10 = np.loadtxt(datFileNEG_M28N14a10)
    
    datFile_M28N14a10 = 'Data/EOPA28F14l14a10.dat'
    data_M28N14a10 = np.loadtxt(datFile_M28N14a10)
    
    #Load energies
    
    energiesNEG_M28N14 = dataNEG_M28N14[:,0]
    energies_M28N14 = data_M28N14[:,0]


    #Load operational entanglement entropies.
    
    #14 particles
    
    #alpha=1,2
    s1NEG_M28N14 = dataNEG_M28N14[:,3]
    s1_M28N14 = data_M28N14[:,3]
    
    s2NEG_M28N14 = dataNEG_M28N14[:,5]
    s2_M28N14 = data_M28N14[:,5]
    
    #alpha=4
    s4NEG_M28N14 = dataNEG_M28N14[:,3]
    s4_M28N14 = data_M28N14[:,3]

    #alpha=10
    s10NEG_M28N14 = dataNEG_M28N14[:,3]
    s10_M28N14 = data_M28N14[:,3]

    #Exact Variance (With Luttinger Parameter Dependence)
    xNEG_14 = np.linspace(-2,-0.03,1000)
    x_14 = np.linspace(0.03,2,1000)
    
    K_14 = pi/(2*np.arccos(-x_14/2))
    KNEG_14 = pi/(2*np.arccos(-xNEG_14/2))
   
    l_even = 14 #partition size.
    sigma2LLNEG_14 = KNEG_14*np.log(l_even)/(2*pi)
    sigma2LL_14 = K_14*np.log(l_even)/(2*pi)
    
    #Negative energies subplot
    ax4 = plt.subplot(gs[2], sharex=ax1)

    #ax4 = fig.add_subplot(223)
    ax4.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point


    #alpha=2
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,4]-dataNEG_M28N14[:,8], 'o',  label=r'2, $S_{2}-S_{2}^{\mathrm{op}}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,7], 'o',label=r'$H_2$', markersize = 1.5, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3])

    #alpha10
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14a10[:,4]-dataNEG_M28N14a10[:,8], 'o',  label=r'10, $S_{10}-S_{10}^{\mathrm{op}}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14a10[:,7], 'o',label=r'10, $H(\alpha=2)$', markersize = 1.5, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3])

    ax4.set_xlim(-energies_M28N14[-1], -energies_M28N14[0])
    #ax4.set_xlim(-2.1,-0.029)
    ax4.set_ylim(0,2.8)
    ax4.set_ylabel(r'$\Delta S_{\alpha}$')
    ax4.set_xscale('symlog', linthreshx = 0.000001)
    ax4.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    
    #Positive energies subplot
    ax5 = plt.subplot(gs[3], sharex=ax2)

    #ax5 = fig.add_subplot(224)
    ax5.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point

    #alpha=2
    ax5.plot(energies_M28N14, data_M28N14[:,4]-data_M28N14[:,8], 'o',  label=r'2, $S_{2}-S_{2}^{op(5)}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax5.plot(energies_M28N14, data_M28N14[:,7], 'o',label=r'$H_2$', markersize = 1.5, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3])

    #alpha10
    ax5.plot(energies_M28N14, data_M28N14a10[:,4]-data_M28N14a10[:,8], 'o',  label=r'10, $S_{10}-S_{10}^{\mathrm{op}}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax5.plot(energies_M28N14, data_M28N14a10[:,7], 'o',label=r'2, $H(\alpha=2)$', markersize = 1.5, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3])
    ax5.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')
    ax5.text(0.04,2.5,r'$N$ = 14')
    ax5.set_xlim(energies_M28N14[0], energies_M28N14[-1])
    ax5.set_ylim(0,2.8)
    ax5.set_xscale('symlog', linthreshx = 0.000001)  #symlog necessary for log scale on negative values
    plt.xlabel(r'$V/t$',x=0)

    #Remove numbers from real axes of top plots
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    plt.savefig('higherAlphaDeltaS_N13N14_fullRange.pdf', transparent=False)
