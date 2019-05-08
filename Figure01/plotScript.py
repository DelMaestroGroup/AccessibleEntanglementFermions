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

with plt.style.context('../IOP_large.mplstyle2'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files

    #11 particles
    datFileNEG_M22N11 = '../Data/OP_PBC_22_11_11_2.dat'
    dataNEG_M22N11 = np.loadtxt(datFileNEG_M22N11)

    datFile_M22N11 = '../Data/OP_PBC_22_11_11_2.dat'
    data_M22N11 = np.loadtxt(datFile_M22N11)[80:160,:]  # Slicing to only plot the positive/neg interaction strengths, accordingly

    #13 particles

    datFileNEG_M26N13 = '../Data/OP_PBC_26_13_13_2.dat'
    dataNEG_M26N13 = np.loadtxt(datFileNEG_M26N13)
    #dataNEG_M26N13 = dataNEG_M26N13[0:81,:]

    datFile_M26N13 = '../Data/OP_PBC_26_13_13_2.dat'
    data_M26N13 = np.loadtxt(datFile_M26N13)


    #15 particles

    datFileNEG_M30N15 = '../Data/OP_PBC_30_15_15_2.dat'
    dataNEG_M30N15 = np.loadtxt(datFileNEG_M30N15)

    datFile_M30N15 = '../Data/OP_PBC_30_15_15_2.dat'
    data_M30N15 = np.loadtxt(datFile_M30N15)

    #Load energies (can choose them arbitrarily from any of the .dat files)
    energiesNEG_M22N11 = dataNEG_M22N11[:,0]
    energies_M22N11 = data_M22N11[:,0]

    energiesNEG_M26N13 = dataNEG_M26N13[:,0]
    energies_M26N13 = data_M26N13[:,0]

    energiesNEG_M30N15 = dataNEG_M30N15[:,0]
    energies_M30N15 = data_M30N15[:,0]

    #Save Operational Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables
    #11 particles
    s1NEG_M22N11 = dataNEG_M22N11[:,3]
    s1_M22N11 = data_M22N11[:,3]

    s2NEG_M22N11 = dataNEG_M22N11[:,8]
    s2_M22N11 = data_M22N11[:,8]

    #13 particles
    s1NEG_M26N13 = dataNEG_M26N13[:,3]
    s1_M26N13 = data_M26N13[:,3]

    s2NEG_M26N13 = dataNEG_M26N13[:,8]
    s2_M26N13 = data_M26N13[:,8]

    #15 particles
    s1NEG_M30N15 = dataNEG_M30N15[:,3]
    s1_M30N15 = data_M30N15[:,3]

    s2NEG_M30N15 = dataNEG_M30N15[:,8]
    s2_M30N15 = data_M30N15[:,8]

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

    #Make a line indicating the value at which operational
    #entanglement converges at +- infinity interaction strength.
    xNEG = np.linspace(-10,-100,1000)
    xPOS = np.linspace(10,100,1000)
    N = 15
    exactNEG = xNEG - xNEG + (N-1)/N * np.log(2)
    exactPOS = 0

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    ax1.axvline(x=-2,color='#cccccc', linestyle='--')   #Grey vertical line at transition point
    ax1.plot(energiesNEG_M30N15, s1NEG_M30N15, 'o',  label='1, 15', markersize = 3, markerfacecolor = blue[1], markeredgewidth = '0.25', color='#2B5080',zorder=4)
    ax1.plot(energiesNEG_M26N13, s1NEG_M26N13, 's', label='1, 13', markersize = 3, markerfacecolor = blue[2], markeredgewidth = '0.25',color='#2B5080')
    ax1.plot(energiesNEG_M22N11, s1NEG_M22N11, '^',  label='1, 11', markersize = 3, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax1.plot(energiesNEG_M30N15, s2NEG_M30N15, 'o',  label='2, 15', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color='#CC7000',zorder=4)
    ax1.plot(energiesNEG_M26N13, s2NEG_M26N13, 's', label='2, 13', markersize = 3, markerfacecolor = orange[2], markeredgewidth = '0.25',color='#CC7000')
    ax1.plot(energiesNEG_M22N11, s2NEG_M22N11, '^',  label='2, 11', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color='#CC7000')
    ax1.plot(xNEG, exactNEG, '-', markersize = 3, markerfacecolor = 'k', markeredgewidth = '0.25',color='k',linewidth=0.6,zorder=5)
    ax1.set_xlim(-energies_M22N11[-1], -energies_M22N11[0])
    ax1.set_ylim(0,0.85)
    ax1.set_ylabel(r'$S_{\alpha}^{\rm{acc}}(\ell)$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax1.set_xlabel(' ')
    ax1.annotate(r'$\frac{14}{15}\ln{2}$', xy=(-30, 0.7 ), xytext=(-80, 0.67))


    #Legend
    lgnd = plt.legend(loc=(0.08,0.031), fontsize=9, handlelength=0,handleheight=1.5,title=r'$\alpha$, $N$',frameon=False)
    lgnd.get_title().set_fontsize(9)
    lgnd.get_title().set_position((2.13,-1))

    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    #ax2 = fig.add_subplot(222)
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')
    ax2.plot(energies_M30N15, s1_M30N15, 'o',  label=r'$1, 15$', markersize = 3, markerfacecolor = blue[1], markeredgewidth = '0.25', color='#2B5080',zorder=4)
    ax2.plot(energies_M26N13, s1_M26N13, 's', label=r'$1, 13$', markersize = 3, markerfacecolor =  blue[2], markeredgewidth = '0.25',color='#2B5080')
    ax2.plot(energies_M22N11, s1_M22N11, '^', label=r'$1, 11$', markersize = 3, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax2.plot(energies_M30N15, s2_M30N15, 'o',  label=r'$2, 15$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color='#CC7000',zorder=4)
    ax2.plot(energies_M26N13, s2_M26N13, 's', label=r'$2, 13$', markersize = 3, markerfacecolor =  orange[2], markeredgewidth = '0.25',color='#CC7000')
    ax2.plot(energies_M22N11, s2_M22N11, '^', label=r'$2, 11$', markersize = 3, markerfacecolor =  orange[3], markeredgewidth = '0.25',color='#CC7000')
    ax2.text(0.04,0.78,r'$N$ Odd')
    ax2.set_xlim(energies_M22N11[0], energies_M22N11[-1])
    ax2.set_ylim(0,0.85)
    ax2.set_xscale('symlog', linthreshx = 0.000001)

    #plt.xlabel(r'$V/t$',x=0)

    #Inset Plot
    plt.subplots_adjust(wspace = 0.030)


#Bottom Plot: Operational entanglement entropies for even number of particles

    #Make a line indicating the value at which operational
    #entanglement converges at +- infinity interaction strength.
    xNEG = np.linspace(-10,-100,1000)
    xPOS = np.linspace(10,100,1000)
    a = 2
    N = 16
    exactNEG = xNEG - xNEG + (a/(1-a))*np.log((N-1)/N * 2**((1-a)/a) + 1/N)
    exactPOS = xPOS - xPOS + np.log(2)

    #Load data

    #12 particles

    datFileNEG_M24N12 = '../Data/OP_ABC_24_12_12_2.dat'
    dataNEG_M24N12 = np.loadtxt(datFileNEG_M24N12)

    datFile_M24N12 = '../Data/OP_ABC_24_12_12_2.dat'
    data_M24N12 = np.loadtxt(datFile_M24N12)


    #14 particles

    datFileNEG_M28N14 = '../Data/OP_ABC_28_14_14_2.dat'
    dataNEG_M28N14 = np.loadtxt(datFileNEG_M28N14)

    datFile_M28N14 = '../Data/OP_ABC_28_14_14_2.dat'
    data_M28N14 = np.loadtxt(datFile_M28N14)


    #16 particles
    datFileNEG_M32N16 = '../Data/OP_ABC_32_16_16_2.dat'
    dataNEG_M32N16 = np.loadtxt(datFileNEG_M32N16)

    datFile_M32N16 = '../Data/OP_ABC_32_16_16_2.dat'
    data_M32N16 = np.loadtxt(datFile_M32N16)

    #Load energies
    energiesNEG_M24N12 = dataNEG_M24N12[:,0]
    energies_M24N12 = data_M24N12[:,0]

    energiesNEG_M28N14 = dataNEG_M28N14[:,0]
    energies_M28N14 = data_M28N14[:,0]

    energiesNEG_M32N16 = dataNEG_M32N16[:,0]
    energies_M32N16 = data_M32N16[:,0]

    #Load operational entanglement entropies.
    #12 particles
    s1NEG_M24N12 = dataNEG_M24N12[:,3]
    s1_M24N12 = data_M24N12[:,3]

    s2NEG_M24N12 = dataNEG_M24N12[:,8]
    s2_M24N12 = data_M24N12[:,8]

    #14 particles
    s1NEG_M28N14 = dataNEG_M28N14[:,3]
    s1_M28N14 = data_M28N14[:,3]

    s2NEG_M28N14 = dataNEG_M28N14[:,8]
    s2_M28N14 = data_M28N14[:,8]

    #16 particles
    s1NEG_M32N16 = dataNEG_M32N16[:,3]
    s1_M32N16 = data_M32N16[:,3]

    s2NEG_M32N16 = dataNEG_M32N16[:,8]
    s2_M32N16 = data_M32N16[:,8]

    #Make a line indicating the value at which operational
    #entanglement converges at +- infinity interaction strength.
    xNEG = np.linspace(-10,-100,1000)
    xPOS = np.linspace(10,100,1000)
    N = 16
    exactNEG = xNEG - xNEG + (N-1)/N * np.log(2)
    exactPOS = np.ones(np.size(xPOS))*np.log(2)

    #Negative energies subplot
    ax4 = plt.subplot(gs[2], sharex=ax1)

    #ax4 = fig.add_subplot(223)
    ax4.axvline(x=-2,color='#cccccc', linestyle='--')   #Grey vertical line at transition point
    ax4.plot(energiesNEG_M32N16, s1NEG_M32N16, 'o',  label='1, 16', markersize = 3, markerfacecolor = blue[1], markeredgewidth = '0.25',color='#2B5080',zorder=4)
    ax4.plot(energiesNEG_M28N14, s1NEG_M28N14, 's', label='1, 14', markersize = 3, markerfacecolor = blue[2], markeredgewidth = '0.25',color='#2B5080')
    ax4.plot(energiesNEG_M24N12, s1NEG_M24N12, '^',  label='1, 12', markersize = 3, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax4.plot(energiesNEG_M32N16, s2NEG_M32N16, 'o',  label='2, 16', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color='#CC7000',zorder=4)
    ax4.plot(energiesNEG_M28N14, s2NEG_M28N14, 's', label='2, 14', markersize = 3, markerfacecolor = orange[2], markeredgewidth = '0.25',color='#CC7000')
    ax4.plot(energiesNEG_M24N12, s2NEG_M24N12, '^',  label='2, 12', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color='#CC7000')
    ax4.plot(xNEG, exactNEG, '-', markersize = 3, markerfacecolor = 'k', markeredgewidth = '0.25',color='k',linewidth=0.6,zorder=5)
    ax4.set_xlim(-energies_M22N11[-1], -energies_M22N11[0])
    ax4.set_ylim(0,0.85)
    ax4.set_ylabel(r'$S_{\alpha}^{\rm{acc}}(\ell)$')
    ax4.set_xscale('symlog', linthreshx = 0.000001)
    ax4.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax4.annotate(r'$\frac{15}{16}\ln{2}$', xy=(-30, 0.7 ), xytext=(-80, 0.67))


    #Legend
    lgnd = plt.legend(loc=(0.08,0.035), fontsize=9, handlelength=0,handleheight=1.5,title=r'$\alpha$, $N$',frameon=False)
    lgnd.get_title().set_fontsize(9)
    lgnd.get_title().set_position((2.13,-1))


    #Positive energies subplot
    ax5 = plt.subplot(gs[3], sharex=ax2)

    #ax5 = fig.add_subplot(224)
    ax5.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point
    ax5.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')
    ax5.plot(energies_M32N16, s1_M32N16, 'o',  label=r'$1, 16$', markersize = 3, markerfacecolor = blue[1], markeredgewidth = '0.25',color='#2B5080',zorder=4)
    ax5.plot(energies_M28N14, s1_M28N14, 's', label=r'$1, 14$', markersize = 3, markerfacecolor = blue[2], markeredgewidth = '0.25',color='#2B5080')
    ax5.plot(energies_M24N12, s1_M24N12, '^', label=r'$1, 12$', markersize = 3, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax5.plot(energies_M32N16, s2_M32N16, 'o',  label=r'$2, 16$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color='#CC7000',zorder=4)
    ax5.plot(energies_M28N14, s2_M28N14, 's', label=r'$2, 14$', markersize = 3, markerfacecolor =  orange[2], markeredgewidth = '0.25',color='#CC7000')
    ax5.plot(energies_M24N12, s2_M24N12, '^', label=r'$2, 12$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color='#CC7000')
    ax5.plot(xPOS, exactPOS, '-', markersize = 3, markerfacecolor = 'k', markeredgewidth = '0.25',color='k',linewidth=0.6,zorder=5)
    ax5.text(0.04,0.78,r'$N$ Even')
    ax5.set_xlim(energies_M22N11[0], energies_M22N11[-1])
    ax5.set_ylim(0,0.85)
    ax5.set_xscale('symlog', linthreshx = 0.000001)  #symlog necessary for log scale on negative values
    ax5.annotate(r'$\ln{2}$', xy=(30, 0.7 ), xytext=(18, 0.73), size=12)
    plt.xlabel(r'$V/t$',x=0)

    #Remove numbers from real axes of top plots
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    plt.savefig('operationalEntanglementEntropies_SOP5.pdf', transparent=False)
