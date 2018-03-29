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

    #Top Plot: Probabilities vs Particle Number in Subsystem Size (For N=13); N=Total Number of Particles

    #Load data files
    data_n13 = np.loadtxt("M26F13V2.826Probs.dat")
    data_n14 = np.loadtxt("M28F14V3.638Probs.dat")
 
    #Load particle numbers 
    n13List = data_n13[:,0]
    n14List = data_n14[:,0]

    #Save probabilities

    #13 particles
    pntoa13 = data_n13[:,1]
    pna13 = data_n13[:,2]

    #14 particles
    pntoa14 = data_n14[:,1]
    pna14 = data_n14[:,2]

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 1)

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    ax1.plot(n13List, np.log(pntoa13), 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax1.plot(n13List, np.log(pna13), '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color='#2B5080')
    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax1.set_xlabel('n')
    ax1.annotate(r'$N=13,\frac{V}{t}=2.826$', xy=(8,0.01), xytext=(10.0,-12.5),fontsize=9)
    ax1.xaxis.set_ticks(np.arange(0, 15, 1))
 
    #Legend
    lgnd = plt.legend(loc=(0.28,0.35), fontsize=9, handlelength=3,handleheight=2,title=r'',frameon=False)
    lgnd.get_title().set_fontsize(9)
    lgnd.get_title().set_position((6,0))

    #Bottom Plot: Probabilities vs Subsystem Size for N=14
    
    #Negative energies subplot
    ax2 = plt.subplot(gs[1], sharex=ax1)

    ax2.plot(n14List, np.log(pntoa14), 'o', label='1, 14', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax2.plot(n14List, np.log(pna14), '.', label='1, 14', markersize = 4, markerfacecolor = blue[0], markeredgewidth = '0.25',color='#2B5080')
    ax2.set_xlabel(r'$n$')
    ax2.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax2.annotate(r'$N=14,\frac{V}{t}=3.638$', xy=(8,0.01), xytext=(10.0,-12.5),fontsize=9)
    
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)
    
    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    plt.savefig('probabilities_N13N14_Vmax_log.pdf', transparent=False)
    plt.show()
