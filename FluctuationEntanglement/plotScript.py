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
orange = ["#e51093"] #NOTE:THIS IS ACTUALLY PINK!
purple = ["#760BA5"]
#blue = ["#4173b3"]

beta = [0.9,0.6,0.2,0.05]

for i,c in enumerate(beta):
    orange.append(colors.get_alpha_hex(orange[0],beta[i]))
 #   blue.append(colors.get_alpha_hex(blue[0],beta[i]))
    purple.append(colors.get_alpha_hex(purple[0],beta[i]))

print(len(orange))


with plt.style.context('../IOP_large.mplstyle2'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files
    
    #13 particles

    #alpha=2
    datFileNEG_M26N13 = 'EOPP26F13l13a2NEG.dat'
    dataNEG_M26N13 = np.loadtxt(datFileNEG_M26N13)
    
    datFile_M26N13 = 'EOPP26F13l13a2.dat'
    data_M26N13 = np.loadtxt(datFile_M26N13)
    
    #alpha=4
    datFileNEG_M26N13a4 = 'EOPP26F13l13a4NEG.dat'
    dataNEG_M26N13a4 = np.loadtxt(datFileNEG_M26N13a4)
    
    datFile_M26N13a4 = 'EOPP26F13l13a4.dat'
    data_M26N13a4 = np.loadtxt(datFile_M26N13a4)

    #alpha=10
    datFileNEG_M26N13a10 = 'EOPP26F13l13a10NEG.dat'
    dataNEG_M26N13a10 = np.loadtxt(datFileNEG_M26N13a10)
    
    datFile_M26N13a10 = 'EOPP26F13l13a10.dat'
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
    #ax1 = fig.add_subplot(221)

    ax1.axvline(x=-2,color='#cccccc')   #Grey vertical line at transition point

#    #alpha=1
#    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,2]-dataNEG_M26N13[:,3], 'o',  label=r'1, $S_{1}-S_{1}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25', color='#4173b3')
#    ax1.plot(energiesNEG_M26N13, 0.5*np.log(2*pi*e*dataNEG_M26N13[:,6]), '*', label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2})}$', markersize = 2, markerfacecolor = '#4173b3', markeredgewidth ='0.25',color='#4173b3')
#    ax1.plot(xNEG, 0.5*np.log(2*pi*e*sigma2LLNEG), '-',label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = 'w', markeredgewidth = '0.25',color='#4173b3')

    #alpha=2
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,4]-dataNEG_M26N13[:,5], 's',  label=r'2, $S_{2}-S_{2}^{op}$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color=orange[0])
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,4]-dataNEG_M26N13[:,8], 'o',  label=r'2, $S_{2}-S_{2}^{op(5)}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
#    ax1.plot(energiesNEG_M26N13, 0.5*np.log(4*pi*dataNEG_M26N13[:,6]), 'd',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2})}$', markersize = 2, markerfacecolor = orange[2], markeredgewidth = '0.25',color='#ff8c00')
#    ax1.plot(xNEG, 0.5*np.log(4*pi*sigma2LLNEG), '-',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color='#ff8c00')
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,7], '*',label=r'2, $H(\alpha=2)$', markersize = 2, markerfacecolor = orange[4], markeredgewidth = '0.08',color=orange[0])

    #alpha=4
#    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13a4[:,4]-dataNEG_M26N13a4[:,5], 's',  label=r'4, $S_{4}-S_{4}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25',color='#A5270B')
#    ax1.plot(energiesNEG_M26N13, 0.5*np.log(2*(4)**(1/3)*pi*dataNEG_M26N13a4[:,6]), 'd',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')
#    ax1.plot(xNEG, 0.5*np.log(2*(4)**(1/3)*pi*sigma2LLNEG), '-',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')

#    #alpha10
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13a10[:,4]-dataNEG_M26N13a10[:,5], 's',  label=r'10, $S_{10}-S_{10}^{op}$', markersize = 3, markerfacecolor = purple[1], markeredgewidth = '0.25',color='#760BA5')
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13a10[:,4]-dataNEG_M26N13a10[:,8], 'o',  label=r'10, $S_{10}-S_{10}^{op(5)}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
   # ax1.plot(energiesNEG_M26N13, 0.5*np.log(2*(10)**(1/9)*pi*dataNEG_M26N13a10[:,6]), 'd',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = purple[2], markeredgewidth = '0.25',color='#760BA5')
   # ax1.plot(xNEG, 0.5*np.log(2*(10)**(1/9)*pi*sigma2LLNEG), '-',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13a10[:,7], '*',label=r'10, $H(\alpha=2)$', markersize = 2, markerfacecolor = purple[4], markeredgewidth = '0.08',color='#760BA5')

    #ax1.set_xlim(-energies_M26N13[-1], -energies_M26N13[0])
    ax1.set_xlim(-2.1,-0.029)
    ax1.set_ylim(0,2.8)
    ax1.set_ylabel(r'$\Delta S_{\alpha}^{\rm{op}}(\ell)$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax1.set_xlabel(' ')

    #Legend
    
    #lgnd = plt.legend(loc=(0.28,0.42),fontsize=6,handlelength=1,handleheight=2, title= r'$\alpha$, $\Delta S$', frameon=False)

    #lgnd.get_title().set_fontsize(7)
    #lgnd.get_title().set_position((-13.02,0))
    
    lgnd = plt.legend(loc=(0.060,0.55),fontsize=4.5,handlelength=1,handleheight=2, title= r'$\alpha$, $\Delta S$', frameon=False) #Uncomment for LL Phase Results only
    #lgnd = plt.legend(loc=(0.060,0.45),fontsize=4.5,handlelength=1,handleheight=2, title= r'$\alpha$, $\Delta S$', frameon=False)

    lgnd.get_title().set_fontsize(5.0)
    lgnd.get_title().set_position((-8.6,0))

    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    #ax2 = fig.add_subplot(222)
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')

#    #alpha=1
#    ax2.plot(energies_M26N13, data_M26N13[:,2]-data_M26N13[:,3], 'o',  label=r'1, $S_{1}-S_{1}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25', color='#4173b3')
#    ax2.plot(energies_M26N13, 0.5*np.log(2*pi*e*data_M26N13[:,6]), '*', label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2})}$', markersize = 2, markerfacecolor = '#4173b3', markeredgewidth ='0.25',color='#4173b3')
#    ax2.plot(x, 0.5*np.log(2*pi*e*sigma2LL), '-',label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = 'w', markeredgewidth = '0.25',color='#4173b3')

    #alpha=2
    ax2.plot(energies_M26N13, data_M26N13[:,4]-data_M26N13[:,5], 's',  label=r'2, $S_{2}-S_{2}^{op}$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color=orange[0])
    ax2.plot(energies_M26N13, data_M26N13[:,4]-data_M26N13[:,8], 'o',  label=r'2, $S_{2}-S_{2}^{op(5)}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
#    ax2.plot(energies_M26N13, 0.5*np.log(4*pi*data_M26N13[:,6]), 'd',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2})}$', markersize = 2, markerfacecolor = orange[2], markeredgewidth = '0.25',color='#ff8c00')
#    ax2.plot(x, 0.5*np.log(4*pi*sigma2LL), '-',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color='#ff8c00')
    ax2.plot(energies_M26N13, data_M26N13[:,7], '*',label=r'2, $H(\alpha=2)$', markersize = 2, markerfacecolor = orange[4], markeredgewidth = '0.08',color=orange[0])

    #alpha=4
#    ax2.plot(energies_M26N13, data_M26N13a4[:,4]-data_M26N13a4[:,5], 's',  label=r'4, $S_{4}-S_{4}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25',color='#A5270B')
#    ax2.plot(energies_M26N13, 0.5*np.log(2*(4)**(1/3)*pi*data_M26N13a4[:,6]), 'd',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')
#    ax2.plot(x, 0.5*np.log(2*(4)**(1/3)*pi*sigma2LL), '-',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')

    #alpha10
    ax2.plot(energies_M26N13, data_M26N13a10[:,4]-data_M26N13a10[:,5], 's',  label=r'10, $S_{10}-S_{10}^{op}$', markersize = 3, markerfacecolor = purple[1], markeredgewidth = '0.25',color='#760BA5')
    ax2.plot(energies_M26N13, data_M26N13a10[:,4]-data_M26N13a10[:,8], 'o',  label=r'10, $S_{10}-S_{10}^{op(5)}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
#    ax2.plot(energies_M26N13, 0.5*np.log(2*(10)**(1/9)*pi*data_M26N13a10[:,6]), 'd',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = purple[2], markeredgewidth = '0.25',color='#760BA5')
#    ax2.plot(x, 0.5*np.log(2*(10)**(1/9)*pi*sigma2LL), '-',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
    ax2.plot(energies_M26N13, data_M26N13a10[:,7], '*',label=r'10, $H(\alpha=2)$', markersize = 2, markerfacecolor = purple[4], markeredgewidth = '0.08',color='#760BA5')

    ax2.text(0.04,2.4,r'$N$ = 13')
    #ax2.set_xlim(energies_M26N13[0], energies_M26N13[-1])
    ax2.set_xlim(0.029,2.1)
    ax2.set_ylim(0,2.8)
    ax2.set_xscale('symlog', linthreshx = 0.000001)
    #plt.xlabel(r'$V/t$',x=0)

    #Inset Plot
    plt.subplots_adjust(wspace = 0.030)

    
#Bottom Plot: Operational entanglement entropies for even number of particles

    #Load data
    
    #14 particles
    
    #alpha=2
    datFileNEG_M28N14 = 'EOPA28F14l14a2NEG.dat'
    dataNEG_M28N14 = np.loadtxt(datFileNEG_M28N14)
    
    datFile_M28N14 = 'EOPA28F14l14a2.dat'
    data_M28N14 = np.loadtxt(datFile_M28N14)
     
    #alpha=4
    datFileNEG_M28N14a4 = 'EOPA28F14l14a4NEG.dat'
    dataNEG_M28N14a4 = np.loadtxt(datFileNEG_M28N14a4)
    
    datFile_M28N14a4 = 'EOPA28F14l14a4.dat'
    data_M28N14a4 = np.loadtxt(datFile_M28N14a4)

    #alpha=10
    datFileNEG_M28N14a10 = 'EOPA28F14l14a10NEG.dat'
    dataNEG_M28N14a10 = np.loadtxt(datFileNEG_M28N14a10)
    
    datFile_M28N14a10 = 'EOPA28F14l14a10.dat'
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

#    #alpha=1
#    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,2]-dataNEG_M28N14[:,3], 'o',  label=r'1, $S_{1}-S_{1}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25', color='#4173b3')
#    ax4.plot(energiesNEG_M28N14, 0.5*np.log(2*pi*e*dataNEG_M28N14[:,6]), '*', label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2})}$', markersize = 2, markerfacecolor = '#4173b3', markeredgewidth ='0.25',color='#4173b3')
#    ax4.plot(xNEG, 0.5*np.log(2*pi*e*sigma2LLNEG_14), '-',label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = 'w', markeredgewidth = '0.25',color='#4173b3')

    #alpha=2
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,4]-dataNEG_M28N14[:,5], 's',  label=r'2, $S_{2}-S_{2}^{op}$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color=orange[0])
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,4]-dataNEG_M28N14[:,8], 'o',  label=r'2, $S_{2}-S_{2}^{op(5)}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    #ax4.plot(energiesNEG_M28N14, 0.5*np.log(4*pi*dataNEG_M28N14[:,6]), 'd',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2})}$', markersize = 2, markerfacecolor = orange[2], markeredgewidth = '0.25',color='#ff8c00')
    #ax4.plot(xNEG, 0.5*np.log(4*pi*sigma2LLNEG_14), '-',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color='#ff8c00')
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,7], '*',label=r'2, $H(\alpha=2)$', markersize = 2, markerfacecolor = orange[4], markeredgewidth = '0.1',color=orange[0])

    #alpha=4
#    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14a4[:,4]-dataNEG_M28N14a4[:,5], 's',  label=r'4, $S_{4}-S_{4}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25',color='#A5270B')
#    ax4.plot(energiesNEG_M28N14, 0.5*np.log(2*(4)**(1/3)*pi*dataNEG_M28N14a4[:,6]), 'd',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')
#    ax4.plot(xNEG, 0.5*np.log(2*(4)**(1/3)*pi*sigma2LLNEG_14), '-',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')

    #alpha10
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14a10[:,4]-dataNEG_M28N14a10[:,5], 's',  label=r'10, $S_{10}-S_{10}^{op}$', markersize = 3, markerfacecolor = purple[1], markeredgewidth = '0.25',color='#760BA5')
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14a10[:,4]-dataNEG_M28N14a10[:,8], 'o',  label=r'10, $S_{10}-S_{10}^{op(5)}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
   # ax4.plot(energiesNEG_M28N14, 0.5*np.log(2*(10)**(1/9)*pi*dataNEG_M28N14a10[:,6]), 'd',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = purple[2], markeredgewidth = '0.25',color='#760BA5')
   # ax4.plot(xNEG, 0.5*np.log(2*(10)**(1/9)*pi*sigma2LLNEG_14), '-',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14a10[:,7], '*',label=r'10, $H(\alpha=2)$', markersize = 2, markerfacecolor = purple[4], markeredgewidth = '0.08',color='#760BA5')

    #ax4.set_xlim(-energies_M28N14[-1], -energies_M28N14[0])
    ax4.set_xlim(-2.1,-0.029)
    ax4.set_ylim(0,2.8)
    ax4.set_ylabel(r'$\Delta S_{\alpha}^{\rm{op}}(\ell)$')
    ax4.set_xscale('symlog', linthreshx = 0.000001)
    ax4.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    
    #Legend
    #lgnd = plt.legend(loc=(0.28,0.42),fontsize=6,handlelength=1,handleheight=2, title= r'$\alpha$, $\Delta S$', frameon=False)

    #lgnd.get_title().set_fontsize(6)
    #lgnd.get_title().set_position((-13.02,0))


    #Positive energies subplot
    ax5 = plt.subplot(gs[3], sharex=ax2)

    #ax5 = fig.add_subplot(224)
    ax5.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point

#    #alpha=1
#    ax5.plot(energies_M28N14, data_M28N14[:,2]-data_M28N14[:,3], 'o',  label=r'1, $S_{1}-S_{1}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25', color='#4173b3')
#    ax5.plot(energies_M28N14, 0.5*np.log(2*pi*e*data_M28N14[:,6]), '*', label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2})}$', markersize = 2, markerfacecolor = '#4173b3', markeredgewidth ='0.25',color='#4173b3')
#    ax5.plot(x, 0.5*np.log(2*pi*e*sigma2LL_14), '-',label=r'1, $\frac{1}{2}\ln{(2 \pi e \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = 'w', markeredgewidth = '0.25',color='#4173b3')

#    #alpha=2
    ax5.plot(energies_M28N14, data_M28N14[:,4]-data_M28N14[:,5], 's',  label=r'2, $S_{2}-S_{2}^{op}$', markersize = 3, markerfacecolor = orange[1], markeredgewidth = '0.25',color=orange[0])
    ax5.plot(energies_M28N14, data_M28N14[:,4]-data_M28N14[:,8], 'o',  label=r'2, $S_{2}-S_{2}^{op(5)}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
#    ax5.plot(energies_M28N14, 0.5*np.log(4*pi*data_M28N14[:,6]), 'd',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2})}$', markersize = 2, markerfacecolor = orange[2], markeredgewidth = '0.25',color='#ff8c00')
#    ax5.plot(x, 0.5*np.log(4*pi*sigma2LL_14), '-',label=r'2, $\frac{1}{2}\ln{(4 \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = orange[3], markeredgewidth = '0.25',color='#ff8c00')
    ax5.plot(energies_M28N14, data_M28N14[:,7], '*',label=r'10, $H(\alpha=2)$', markersize = 2, markerfacecolor = orange[4], markeredgewidth = '0.08',color=orange[0])

    #alpha=4
#    ax5.plot(energies_M28N14, data_M28N14a4[:,4]-data_M26N13a4[:,5], 's',  label=r'4, $S_{4}-S_{4}^{op}$', markersize = 3, markerfacecolor = 'None', markeredgewidth = '0.25',color='#A5270B')
#    ax5.plot(energies_M28N14, 0.5*np.log(2*(4)**(1/3)*pi*data_M28N14a4[:,6]), 'd',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')
#    ax5.plot(x, 0.5*np.log(2*(4)**(1/3)*pi*sigma2LL_14), '-',label=r'4, $\frac{1}{2}\ln{(2 (4)^{\frac{1}{3}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = '#A5270B', markeredgewidth = '0.25',color='#A5270B')

#    #alpha10
    ax5.plot(energies_M28N14, data_M28N14a10[:,4]-data_M28N14a10[:,5], 's',  label=r'10, $S_{10}-S_{10}^{op}$', markersize = 3, markerfacecolor = purple[1], markeredgewidth = '0.25',color='#760BA5')
    ax5.plot(energies_M28N14, data_M28N14a10[:,4]-data_M28N14a10[:,8], 'o',  label=r'10, $S_{10}-S_{10}^{op(5)}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
    #ax5.plot(energies_M28N14, 0.5*np.log(2*(10)**(1/9)*pi*data_M28N14a10[:,6]), 'd',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2})}$', markersize = 2, markerfacecolor = purple[2], markeredgewidth = '0.25',color='#760BA5')
    #ax5.plot(x, 0.5*np.log(2*(10)**(1/9)*pi*sigma2LL_14), '-',label=r'10, $\frac{1}{2}\ln{(2 (10)^{\frac{1}{9}} \pi \sigma^{2}_{LL})}$', markersize = 3, markerfacecolor = purple[3], markeredgewidth = '0.25',color='#760BA5')
    ax5.plot(energies_M28N14, data_M28N14a10[:,7], '*',label=r'2, $H(\alpha=2)$', markersize = 2, markerfacecolor = purple[4], markeredgewidth = '0.08',color='#760BA5')

    ax5.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')
    ax5.text(0.04,2.4,r'$N$ = 14')
    #ax5.set_xlim(energies_M28N14[0], energies_M28N14[-1])
    ax5.set_xlim(0.029,2.1)

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

    #plt.savefig('higherAlphaFluctuations_N13N14_fullRange.pdf', transparent=False)
    plt.savefig('higherAlphaFluctuations_N13N14_LLPhase.pdf', transparent=False)

    plt.show()
