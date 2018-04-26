#Calculates the difference between the Von Neumann and Von Neumann Opearational
#Entanglement Entropies

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import gridspec
from math import pi
import colors

orange = ["#ff8c00"]
blue = ["#4173b3"]

alpha = [0.2,0.1,0.0]
beta = [1.0,0.6,0.2]

for i,c in enumerate(alpha):
        orange.append(colors.get_alpha_hex(orange[0],beta[i]))
        blue.append(colors.get_alpha_hex(blue[0],beta[i]))

with plt.style.context('../IOP_large.mplstyle2'):
    
#Load the files

    sigma2FF= 0.4447369456644643  
    #sigma2FF is calculated using the correlation matrix method

    #Negative Side
    datFileNEG = np.loadtxt("EOPP26F13l13NEG.dat")
    energiesNEG = datFileNEG[:,0]
    s1NEG = datFileNEG[:,2]
    s1opNEG = datFileNEG[:,3]
    #sigma2NEG = np.log(datFileNEG[:,6])
    sigma2NEG = 0.5*np.log(2*np.pi*np.exp(1)*datFileNEG[:,6])
    l = 13 #Subsystem Size
    kNEG = pi/(2*np.arccos(-energiesNEG/2))
    sigma2NEGLL = kNEG * sigma2FF

    dsNEGLL = 0.5*np.log(2*np.pi*np.exp(1)*sigma2NEGLL)

    #Positive Side
    datFile = np.loadtxt("EOPP26F13l13.dat")
    energies = datFile[:,0]
    s1 = datFile[:,2]
    s1op = datFile[:,3]
    sigma2 = 0.5*np.log(2*np.pi*np.exp(1)*datFile[:,6])
    k = pi/(2*np.arccos(-energies/2))
    sigma2LL = k * sigma2FF

    dsLL = 0.5*np.log(2*np.pi*np.exp(1)*sigma2LL)


    #Calculate the difference
    dsNEG = s1NEG - s1opNEG
    ds = s1 - s1op

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 2, height_ratios=[1,1])

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])
    ax1.axvline(x=-2,color='#cccccc',zorder=-1)   #Grey vertical line at transition point
    ax1.plot(energiesNEG[0::2], dsNEG[0::2], '.', label=r'$S_{1}-S_{1}^{\rm{op}}$', linewidth = 1, color=blue[0], markerfacecolor = blue[3], markeredgewidth = '0.5',markersize=9,zorder=0)
    ax1.plot(energiesNEG[0::2], sigma2NEG[0::2], '.', label=r'$\frac{1}{2}\ln{(2 \pi e \sigma^{2})}$',linewidth = 1, color=blue[0], markerfacecolor = 'None', markeredgewidth = '0.5',markersize=4,zorder=2)
    ax1.plot(energiesNEG, dsNEGLL, '-', label=r'$\frac{1}{2}\ln{(2 \pi e K\sigma^2_{FF})}$',linewidth = 1, color=blue[0], markerfacecolor = blue[0], markeredgewidth = '0.5',zorder=1)
    ax1.set_xlim(-energies[-1], -energies[0])
    ax1.set_ylabel(r'$\Delta S_{1}$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction = 'in')
    ax1.set_xscale('symlog', linthreshx = 0.000001)
    ax1.set_ylim(-0.51,3.0)
    ax1.set_xlim(-100,-0.029)
    #ax1.set_ylim(-0.15,7.8)

    #Legend
    lgnd = plt.legend(loc=(0.20,0.0998),fontsize=7,handlelength=1,handleheight=1, frameon=True)
    frame = lgnd.get_frame()
    frame.set_edgecolor('#cccccc')
    frame.set_alpha(1.0)
    
    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    ax2.axvline(x=2, color='#cccccc',zorder=-1)
    ax2.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction = 'in')
    ax2.plot(energies[0::2], ds[0::2], '.', label='1, 13', linewidth = 1, color=blue[0], markerfacecolor = blue[3], markeredgewidth = '0.5',markersize=9,zorder=0)
    ax2.plot(energies[0::2], sigma2[0::2], '.', linewidth = 1, color=blue[0], markerfacecolor = 'None', markeredgewidth = '0.5',markersize=4,zorder=2)
    ax2.plot(energies, dsLL, '-', linewidth = 1, color=blue[0],markerfacecolor = blue[0], markeredgewidth = '0.5',zorder=1)
    ax2.set_xlim(energies[0], energies[-1])
    ax2.set_xscale('symlog', linthreshx = 0.000001)
    ax2.set_ylim(-0.51,3.0)
    ax2.set_xlim(0.029,100)
    ax2.text(0.04,2.65,r'$N=13$')

    ################################
    
    sigma2FF=0.4515333623486861
    #sigma2FF is calculated using the correlation matrix method

    #Negative Side
    datFileNEG = np.loadtxt("EOPA28F14l14NEG.dat")
    energiesNEG = datFileNEG[:,0]
    s1NEG = datFileNEG[:,2]
    s1opNEG = datFileNEG[:,3]
    #sigma2NEG = np.log(datFileNEG[:,6])
    sigma2NEG = 0.5*np.log(2*np.pi*np.exp(1)*datFileNEG[:,6])
    l = 14 #Subsystem Size
    kNEG = pi/(2*np.arccos(-energiesNEG/2))
    sigma2NEGLL = kNEG *sigma2FF

    dsNEGLL = 0.5*np.log(2*np.pi*np.exp(1)*sigma2NEGLL)

    
    #Positive Side
    datFile = np.loadtxt("EOPA28F14l14.dat")
    energies = datFile[:,0]
    s1 = datFile[:,2]
    s1op = datFile[:,3]
    sigma2 = 0.5*np.log(2*np.pi*np.exp(1)*datFile[:,6])  #ACTUALLY Delta S
    k = pi/(2*np.arccos(-energies/2))
    sigma2LL = k * sigma2FF

    dsLL = 0.5*np.log(2*np.pi*np.exp(1)*sigma2LL)


    #Calculate the difference
    dsNEG = s1NEG - s1opNEG
    ds = s1 - s1op

    #Negative energies subplot
    ax4 = plt.subplot(gs[2])
    ax4.axvline(x=-2,color='#cccccc',zorder=-1)   #Grey vertical line at transition point
    ax4.plot(energiesNEG[0::2], dsNEG[0::2], '.', label=r'$\Delta s = s_{1}-s_{1}^{op}$', linewidth = 1, color=blue[0], markerfacecolor = blue[3], markeredgewidth = '0.5',markersize=9,zorder=0)
    ax4.plot(energiesNEG[0::2], sigma2NEG[0::2], '.', label=r'$\frac{1}{2}\ln{(2 \pi e \sigma^{2})}$',linewidth = 1, color=blue[0], markerfacecolor = 'None', markeredgewidth = '0.5',markersize=4,zorder=2)
    ax4.plot(energiesNEG, dsNEGLL, '-', label=r'$\frac{1}{2}\ln{(2 \pi e \sigma^{2})}$',linewidth = 1, color=blue[0], markerfacecolor = 'w', markeredgewidth = '0.5',zorder=1)
    ax4.set_xlim(-energies[-1], -energies[0])
    ax4.set_ylabel(r'$\Delta S_{1}$')
    ax4.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax4.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction = 'in')
    ax4.set_xscale('symlog', linthreshx = 0.000001)
    ax4.set_ylim(-0.51,3.0)
    ax4.set_xlim(-100,-0.029)

    #Positive energies subplot
    ax5 = plt.subplot(gs[3])
    ax5.axvline(x=2, color='#cccccc',zorder=-1)
    ax5.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction = 'in')
    ax5.plot(energies[0::2], ds[0::2], '.', label='1, 13', linewidth = 1, color=blue[0], markerfacecolor = blue[3], markeredgewidth = '0.5',markersize=9,zorder=0)
    ax5.plot(energies[0::2], sigma2[0::2], '.', linewidth = 1, color=blue[0], markerfacecolor = 'None', markeredgewidth = '0.5',markersize=4,zorder=2)
    ax5.plot(energies, dsLL, '-', linewidth = 1, color=blue[0], markerfacecolor = 'w', markeredgewidth = '0.5',zorder=1)
    ax5.set_xlim(energies[0], energies[-1])
    ax5.set_xscale('symlog', linthreshx = 0.000001)
    ax5.set_ylim(-0.51,3.0)
    ax5.set_xlim(0.029,100)
    ax5.text(0.04,2.65,r'$N=14$')


    #Remove numbers from real axes of top plots
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)
    plt.xlabel(r'$V/t$',x=0)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    plt.savefig('deltaS_N13N14.pdf', transparent=False)
    plt.show()