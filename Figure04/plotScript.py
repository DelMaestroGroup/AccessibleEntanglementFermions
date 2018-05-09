#Plot probability distributions as a function of
#subsystem particle number in the tV-Model at
#different V/t and alphas.

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

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
    #data_n13 = np.loadtxt("M26F13VNEG1.5Probs.dat")
    #data_n14 = np.loadtxt("M28F14VNEG1.5Probs.dat")
    
    #data_n13 = np.loadtxt("M26F13VNEG1.0Probs.dat")
    #data_n14 = np.loadtxt("M28F14VNEG1.0Probs.dat")
    
    #data_n13 = np.loadtxt("M26F13V1.0Probs.dat")
    #data_n14 = np.loadtxt("M28F14V1.0Probs.dat")
    
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
    
    #Fit Quadratic to test Gaussian Hypothesis
    ############################################################################################################
    
    #Determine average n_A
    n13Ave = 6.5
    n14Ave = 7.0
    
    lnpntoa13 = np.log(pntoa13)
    lnpna13 = np.log(pna13)
    
    lnpntoa14 = np.log(pntoa14)
    lnpna14 = np.log(pna14)

    coeffs13 = np.polyfit((n13List[2:-2]-n13Ave), lnpntoa13[2:-2], deg=2)
    coeffs14 = np.polyfit((n14List[2:-2]-n14Ave), lnpntoa14[2:-2], deg=2)
    
    var13 = np.sum(n13List**2 * pntoa13) - n13Ave**2
    var14 = np.sum(n14List**2 * pntoa14) - n14Ave**2
    
    print("Variance N=13: ", var13)
    print("Variance N=14: ", var14)
 
    A13 , B13, C13 = coeffs13[0], coeffs13[1], coeffs13[2]
    A14 , B14, C14 = coeffs14[0], coeffs14[1], coeffs14[2]
    
    #A13 = - 1/(2*var13) 
    #A14 = - 1/(2*var14) 
    
    #C13 = (0.5)*np.log(1/(2*np.pi*var13))
    #C14 = (0.5)*np.log(1/(2*np.pi*var14))
    
    print("Coeffs of N=13: ", coeffs13)
    print("Coeffs of N=14: ", coeffs14)
        
    n13fit = np.linspace(0,13,1000)
    n14fit = np.linspace(0,14,1000)
    
    lnpntoa13fit = A13*(n13fit-n13Ave)**2 + B13*(n13fit-n13Ave) + C13
    lnpntoa14fit = A14*(n14fit-n14Ave)**2 + B14*(n14fit-n14Ave) + C14

    
    ############################################################################################################

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 1)

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    ax1.plot(n13List, lnpntoa13, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax1.plot(n13List, lnpna13, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color='#2B5080')
    ax1.plot(n13fit, lnpntoa13fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')
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

    ax2.plot(n14List, lnpntoa14, 'o', label='1, 14', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color='#2B5080')
    ax2.plot(n14List, lnpna14, '.', label='1, 14', markersize = 4, markerfacecolor = blue[0], markeredgewidth = '0.25',color='#2B5080')
    ax2.plot(n14fit, lnpntoa14fit, color='k', label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')
    ax2.set_xlabel(r'$n$')
    ax2.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax2.annotate(r'$N=14,\frac{V}{t}=3.638$', xy=(8,0.01), xytext=(10.0,-12.5),fontsize=9)
    
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)
    
    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    #plt.savefig('probabilities_N13N14_VNEG1.5_log.pdf', transparent=False)
    #plt.savefig('probabilities_N13N14_VNEG1.0_log.pdf', transparent=False)   
    #plt.savefig('probabilities_N13N14_V1.0_log.pdf', transparent=False)
    plt.savefig('probabilities_N13N14_VMax_log.pdf', transparent=False)

    plt.show()
