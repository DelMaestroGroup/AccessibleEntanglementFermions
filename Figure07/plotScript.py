#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import numpy as np
import matplotlib.pyplot as plt
import colors
from matplotlib import gridspec
import matplotlib.ticker as ticker

orange = ["#ff8c00"]
blue = ["#4173b3"]

alpha = [1.0,0.6,0.2]
for i,c in enumerate(alpha):
        orange.append(colors.get_alpha_hex(orange[0],alpha[i]))
        blue.append(colors.get_alpha_hex(blue[0],alpha[i]))

with plt.style.context('../IOP_large.mplstyle2'):
    
    #Load filling fractions
    fillingFractions = [i/28 for i in range(1,15)]
    
    #Save Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables
    
    s1opVNEG100M28l14 = np.loadtxt("Data/VNEG100M28l14.dat")[:,3]
    s1opVNEG100M28lN = np.loadtxt("Data/VNEG100M28lN.dat")[:,3]
    s1opVNEG1d5M28l14 = np.loadtxt("Data/VNEG1.5M28l14.dat")[:,3]
    s1opVNEG1d5M28lN = np.loadtxt("Data/VNEG1.5M28lN.dat")[:,3]
    s1opV100M28l14 = np.loadtxt("Data/V100M28l14.dat")[:,3]
    s1opV100M28lN = np.loadtxt("Data/V100M28lN.dat")[:,3]
    
    s2opVNEG100M28l14 = np.loadtxt("Data/VNEG100M28l14.dat")[:,8]
    s2opVNEG100M28lN = np.loadtxt("Data/VNEG100M28lN.dat")[:,8]
    s2opVNEG1d5M28l14 = np.loadtxt("Data/VNEG1.5M28l14.dat")[:,8]
    s2opVNEG1d5M28lN = np.loadtxt("Data/VNEG1.5M28lN.dat")[:,8]
    s2opV100M28l14 = np.loadtxt("Data/V100M28l14.dat")[:,8]
    s2opV100M28lN = np.loadtxt("Data/V100M28lN.dat")[:,8]
    
    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    #gs = gridspec.GridSpec(2, 2, height_ratios=[20,20])
    gs = gridspec.GridSpec(3, 2)
        
    ax1 = plt.subplot(gs[0])
    ax1.plot(fillingFractions, s1opV100M28l14, '.', label=r'$S_{1}^{\mathrm{acc}}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',mfc= blue[2],zorder=10)
    ax1.plot(fillingFractions, s2opV100M28l14, '.', label=r'$S_{2}^{\mathrm{acc}}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',mfc= orange[2],zorder=10)
    ax1.plot(fillingFractions, s1opV100M28l14, ':', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax1.plot(fillingFractions, s2opV100M28l14, ':', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax1.set_xlim(fillingFractions[0], fillingFractions[-1])
    ax1.set_ylim(0.0, 0.95)
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in',labelbottom='off')
    ax1.xaxis.set_ticks([0.1,0.2,0.3,0.4,0.5])
    ax1.set_ylabel(r'$S_{\alpha}^{\rm{acc}}$')
    
    #Legend
    lgnd = plt.legend(loc=(0.06,0.65),fontsize=9,frameon=False,handlelength=1,handleheight=1)
    
    ax2 = plt.subplot(gs[1])
    ax2.plot(fillingFractions, s1opV100M28lN, '.', label = r'$S_{1}^{acc}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',mfc= blue[2],zorder=10)
    ax2.plot(fillingFractions, s2opV100M28lN, '.', label = r'$S_{2}^{acc}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',mfc= orange[2],zorder=10)
    ax2.plot(fillingFractions, s1opV100M28lN , ':', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax2.plot(fillingFractions, s2opV100M28lN, ':', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax2.set_xlim(fillingFractions[0], fillingFractions[-1])
    ax2.set_ylim(0.0, 0.95)
    ax2.xaxis.set_ticks([0.1,0.2,0.3,0.4,0.5])
    ax2.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='off', direction = 'in',labelbottom='off')
        
    ax3 = plt.subplot(gs[2])
    ax3.plot(fillingFractions, s1opVNEG1d5M28l14, '.', label=r'$S_{1}^{acc}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',mfc= blue[2],zorder=10)
    ax3.plot(fillingFractions, s2opVNEG1d5M28l14, '.', label=r'$S_{2}^{acc}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',mfc= orange[2],zorder=10)
    ax3.plot(fillingFractions, s1opVNEG1d5M28l14, ':', label=r'$S_{1}^{acc}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax3.plot(fillingFractions, s2opVNEG1d5M28l14, ':', label=r'$S_{2}^{acc}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax3.set_xlim(fillingFractions[0], fillingFractions[-1])
    ax3.set_ylim(0.0, 0.23)
    ax3.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in',labelbottom='off')
    ax3.xaxis.set_ticks([0.1,0.2,0.3,0.4,0.5])
    ax3.set_yticks(np.arange(0,0.27,0.1))
    ax3.set_ylabel(r'$S_{\alpha}^{\rm{acc}}$')
    
    ax4 = plt.subplot(gs[3])
    ax4.plot(fillingFractions, s1opVNEG1d5M28lN , '.', label=r'$S_{1}^{acc}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',mfc= blue[2],zorder=10)
    ax4.plot(fillingFractions, s2opVNEG1d5M28lN, '.', label=r'$S_{2}^{acc}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',mfc= orange[2],zorder=10)
    ax4.plot(fillingFractions, s1opVNEG1d5M28lN , ':', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax4.plot(fillingFractions, s2opVNEG1d5M28lN, ':', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax4.set_xlim(fillingFractions[0], fillingFractions[-1])
    ax4.set_ylim(0.0, 0.23)
    ax4.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='off', direction = 'in',labelbottom='off')
    ax4.xaxis.set_ticks([0.1,0.2,0.3,0.4,0.5])
    ax4.set_yticks(np.arange(0,0.27,0.1))

    ax5 = plt.subplot(gs[4])
    ax5.plot(fillingFractions, s1opVNEG100M28l14, '.', label=r'$S_{1}^{\rm acc}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',mfc= blue[2],zorder=10)
    ax5.plot(fillingFractions, s2opVNEG100M28l14, '.', label=r'$S_{2}^{\rm acc}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',mfc= orange[2],zorder=10)
    ax5.plot(fillingFractions, s1opVNEG100M28l14, ':', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax5.plot(fillingFractions, s2opVNEG100M28l14, ':', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax5.set_xlim(fillingFractions[0], fillingFractions[-1])
    ax5.set_ylim(0.0, 0.65)
    ax5.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
    ax5.xaxis.set_ticks([0.1,0.2,0.3,0.4,0.5])
    ax5.set_xlabel(r'$f$')
    ax5.set_ylabel(r'$S_{\alpha}^{\rm{acc}}$')
    
    ax6 = plt.subplot(gs[5])
    ax6.plot(fillingFractions, s1opVNEG100M28lN, '.', label=r'$S_{1}^{\rm{acc}}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',mfc= blue[2],zorder=10)
    ax6.plot(fillingFractions, s2opVNEG100M28lN, '.', label=r'$S_{2}^{\rm{acc}}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',mfc= orange[2],zorder=10)
    ax6.plot(fillingFractions, s1opVNEG100M28lN, ':', label=r'$S_{1}^{\rm{acc}}$', linewidth = 0.5, color='#4173b3',markeredgewidth='0.5')
    ax6.plot(fillingFractions, s2opVNEG100M28lN, ':', label=r'$S_{2}^{\rm{acc}}$', linewidth = 0.5, color='#ff8c00',markeredgewidth='0.5')
    ax6.set_xlim(fillingFractions[0], fillingFractions[-1])
    ax6.set_ylim(0.0, 0.65)
    ax6.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='off', direction = 'in')
    ax6.xaxis.set_ticks([0.1,0.2,0.3,0.4,0.5])
    ax6.set_xlabel(r'$f$')
    
    #Annotations for the interaction strength and type of partition
    x1,y1 = 0.415,0.085
    x2,y2 = 0.5,0.5
    fs = 8
    ax1.annotate(r'$V/t=100,\ell = L/2$',
            xy=(x1-0.1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )
    ax2.annotate(r'$V/t=100,\ell = N$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )
    ax3.annotate(r'$V/t=-1.5,\ell = L/2$',
            xy=(x1-0.1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )
    ax4.annotate(r'$V/t=-1.5,\ell = N$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )
    ax5.annotate(r'$V/t=-100,\ell = L/2$',
            xy=(x1-0.1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )
    ax6.annotate(r'$V/t=-100,\ell = N$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )

    
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.050)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.040)
    
    plt.savefig('fillingFractionDependence.pdf', transparent=False)
