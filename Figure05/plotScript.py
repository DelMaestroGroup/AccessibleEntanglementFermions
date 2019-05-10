import numpy as np
import matplotlib.pyplot as plt
import colors
from matplotlib import gridspec
from math import pi,e

orange = ["#ff8c00"]
#purple = ["#7dcca4"] #Actually green
purple = ["#e85c47"] #Actually red
blue = ["#4173b3"]
green = ["#66cdaa"]

beta = [0.9,0.6,0.2,0.05]

for i,c in enumerate(beta):
    orange.append(colors.get_alpha_hex(orange[0],beta[i]))
    purple.append(colors.get_alpha_hex(purple[0],beta[i]))
    green.append(colors.get_alpha_hex(green[0],beta[i]))

print(len(orange))


with plt.style.context('../IOP_large.mplstyle2'):

#Top Plot: One Particle Entanglement entropy dependence on the interaction potential

    #Load data files

    #13 particles

    #alpha=2
    datFileNEG_M26N13 = '../Data/OP_PBC_30_15_15_2.dat'
    dataNEG_M26N13 = np.loadtxt(datFileNEG_M26N13)[0:28,:] # Slicing to plot neg/pos interactions correctly

    datFile_M26N13 = '../Data/OP_PBC_30_15_15_2.dat'
    data_M26N13 = np.loadtxt(datFile_M26N13)[28:,:] # Slicing to plot neg/pos interactions correctly

    #alpha=10
    datFileNEG_M26N13a10 = '../Data/OP_PBC_30_15_15_10.dat'
    dataNEG_M26N13a10 = np.loadtxt(datFileNEG_M26N13a10)

    datFile_M26N13a10 = '../Data/OP_PBC_30_15_15_10.dat'
    data_M26N13a10 = np.loadtxt(datFile_M26N13a10)

    #Load energies
    energiesNEG_M26N13 = dataNEG_M26N13[:,0]
    energies_M26N13 = data_M26N13[:,0]

    energiesNEG_M26N13a10 = dataNEG_M26N13a10[:,0]
    energies_M26N13a10 = data_M26N13a10[:,0]

    #Save Operational Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables

    #13 particles

    #alpha=1,2

    sigma2FF_15= 0.45909421031059594
    #sigma2FF is calculated using the correlation matrix method
    #or doing a run at V/t = 0

    s1NEG_M26N13 = dataNEG_M26N13[:,3]
    s1_M26N13 = data_M26N13[:,3]

    s2NEG_M26N13 = dataNEG_M26N13[:,5]
    s2_M26N13 = data_M26N13[:,5]

    #alpha=10
    s10NEG_M26N13 = dataNEG_M26N13a10[:,5]
    s10_M26N13 = data_M26N13a10[:,5]


    kNEG = pi/(2*np.arccos(-np.linspace(energiesNEG_M26N13[1],energiesNEG_M26N13[-1],1000)/2))
    sigma2NEGLL = kNEG *sigma2FF_15
    alpha=2.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsNEGLL2 = 0.5*np.log(sigma2NEGLL)+B_alpha
    alpha=10.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsNEGLL10 = 0.5*np.log(sigma2NEGLL)+B_alpha

    k = pi/(2*np.arccos(-np.linspace(energies_M26N13[0],energies_M26N13[-1],1000)/2))
    sigma2LL = k * sigma2FF_15
    alpha=2.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsLL2 = 0.5*np.log(sigma2LL)+B_alpha
    alpha=10.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsLL10 = 0.5*np.log(sigma2LL)+B_alpha


    #l=13

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

    #Negative energies subplot
    ax1 = plt.subplot(gs[0])

    ax1.axvline(x=-2,linestyle='--',color='#cccccc')   #Grey vertical line at transition point

    #alpha=2
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,4]-dataNEG_M26N13[:,8], '.',  label=r'$S_{2}-S_{2}^{\rm{acc}}$', markersize = 9, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax1.plot(energiesNEG_M26N13, dataNEG_M26N13[:,7], '.',label=r'$H_2$', markersize = 4, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3],zorder=3)

    #alpha10
    ax1.plot(energiesNEG_M26N13a10, dataNEG_M26N13a10[:,4]-dataNEG_M26N13a10[:,8], '.',  label=r'$S_{10}-S_{10}^{\rm{acc}}$', markersize = 9, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax1.plot(energiesNEG_M26N13a10, dataNEG_M26N13a10[:,7], '.',label=r'$H_{10}$', markersize = 4, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3],zorder=3)

    ax1.text(-.80,2.6,r'$N = 15$')
    ax1.set_xlim(energiesNEG_M26N13[0], energiesNEG_M26N13[-1])
    ax1.set_ylim(0,2.9)
    ax1.set_ylabel(r'$\Delta S_{\alpha}$')
    ax1.set_xscale('symlog', linthreshx = 0.000001)       #symlog necessary to plot negative values with log scale
    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax1.set_xlabel(' ')

    #Positive energies subplot
    ax2 = plt.subplot(gs[1])
    ax2.axvline(x=2, color='#cccccc')
    ax2.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')

    #alpha=2
    ax2.plot(energies_M26N13, data_M26N13[:,4]-data_M26N13[:,8], '.',  label=r'$S_{2}-S_{2}^{\rm{acc}}$', markersize = 9, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax2.plot(energies_M26N13, data_M26N13[:,7], '.',label=r'$H_2$', markersize = 4, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3],zorder=7)
    #alpha10
    ax2.plot(energies_M26N13a10, data_M26N13a10[:,4]-data_M26N13a10[:,8], '.',  label=r'$S_{10}-S_{10}^{\rm{acc}}$', markersize = 9, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax2.plot(energies_M26N13a10, data_M26N13a10[:,7], '.',label=r'$H_{10}$', markersize = 4, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3],zorder=7)

    ax2.set_xlim(energies_M26N13[0], energies_M26N13[-1])
    ax2.set_ylim(0,2.9)
    ax2.set_xscale('symlog', linthreshx = 0.000001)

    #Legend
    #lgnd = plt.legend(loc=(-0.0,0.44),ncol=2,fontsize=9,handlelength=1,handleheight=2, frameon=False)
    lgnd = plt.legend(loc=(0.245,0.440),fontsize=9,handlelength=1,handleheight=1, frameon=True,facecolor='w',framealpha=0.8,edgecolor='w')

    #Inset Plot
    plt.subplots_adjust(wspace = 0.030)


#Bottom Plot: Operational entanglement entropies for even number of particles

    #Load data

    #14 particles

    #alpha=2
    datFileNEG_M28N14 = '../Data/OP_ABC_32_16_16_2.dat'
    dataNEG_M28N14 = np.loadtxt(datFileNEG_M28N14)[0:28,:]  # Slicing to plot neg/pos interactions correctly

    datFile_M28N14 = '../Data/OP_ABC_32_16_16_2.dat'
    data_M28N14 = np.loadtxt(datFile_M28N14)[28:,:]  # Slicing to plot neg/pos interactions correctly

    #alpha=10
    datFileNEG_M28N14a10 = '../Data/OP_ABC_32_16_16_10.dat'
    dataNEG_M28N14a10 = np.loadtxt(datFileNEG_M28N14a10)

    datFile_M28N14a10 = '../Data/OP_ABC_32_16_16_10.dat'
    data_M28N14a10 = np.loadtxt(datFile_M28N14a10)

    #Load energies

    energiesNEG_M28N14 = dataNEG_M28N14[:,0]
    energies_M28N14 = data_M28N14[:,0]

    energiesNEG_M28N14a10 = dataNEG_M28N14a10[:,0]
    energies_M28N14a10 = data_M28N14a10[:,0]


    #Load operational entanglement entropies.

    #14 particles

    #alpha=1,2

    sigma2FF_16=0.4650954313305221
    #sigma2FF is calculated using the correlation matrix method

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


    sigma2NEGLL = kNEG *sigma2FF_16
    alpha=2.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsNEGLL2 = 0.5*np.log(sigma2NEGLL)+B_alpha
    alpha=10.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsNEGLL10 = 0.5*np.log(sigma2NEGLL)+B_alpha

    sigma2LL = k * sigma2FF_16
    alpha=2.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsLL2 = 0.5*np.log(sigma2LL)+B_alpha
    alpha=10.0
    B_alpha=0.5*np.log(2*np.pi*alpha**(1/(alpha-1)))
    dsLL10 = 0.5*np.log(sigma2LL)+B_alpha

    #Negative energies subplot
    ax4 = plt.subplot(gs[2], sharex=ax1)

    ax4.axvline(x=-2,linestyle='--',color='#cccccc')   #Grey vertical line at transition point


    #alpha=2
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,4]-dataNEG_M28N14[:,8], '.',  label=r'2, $S_{2}-S_{2}^{\mathrm{acc}}$', markersize = 9, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax4.plot(energiesNEG_M28N14, dataNEG_M28N14[:,7], '.',label=r'$H_2$', markersize = 4, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3],zorder=11)
    #alpha10
    ax4.plot(energiesNEG_M28N14a10, dataNEG_M28N14a10[:,4]-dataNEG_M28N14a10[:,8], '.',  label=r'10, $S_{10}-S_{10}^{\mathrm{acc}}$', markersize = 9, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax4.plot(energiesNEG_M28N14a10, dataNEG_M28N14a10[:,7], '.',label=r'10, $H(\alpha=2)$', markersize = 4, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3],zorder=11)

    ax4.text(-0.80,2.6,r'$N = 16$')
    ax4.set_xlim(energiesNEG_M28N14[0], energiesNEG_M28N14[-1])
    ax4.set_ylim(0,2.9)
    ax4.set_ylabel(r'$\Delta S_{\alpha}$')
    ax4.set_xscale('symlog', linthreshx = 0.000001)
    ax4.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')

    #Positive energies subplot
    ax5 = plt.subplot(gs[3], sharex=ax2)

    ax5.axvline(x=2,color='#cccccc')   #Grey vertical line at transition point

    #alpha=2
    ax5.plot(energies_M28N14, data_M28N14[:,4]-data_M28N14[:,8], '.', markersize = 9, markerfacecolor = orange[3], markeredgewidth = '0.25',color=orange[0])
    ax5.plot(energies_M28N14, data_M28N14[:,7], '.', markersize = 4, markerfacecolor = orange[1], markeredgewidth = '0.08',color=orange[3],zorder=15)
    ax5.plot(energies_M28N14a10, data_M28N14a10[:,4]-data_M28N14a10[:,8], '.', markersize = 9, markerfacecolor = purple[3], markeredgewidth = '0.25',color=purple[0])
    ax5.plot(energies_M28N14a10, data_M28N14a10[:,7], '.', markersize = 4, markerfacecolor = purple[1], markeredgewidth = '0.08',color=purple[3],zorder=15)


    ax5.tick_params(axis='both', which='both', left='off', top='off',labelleft='off', direction='in')
    ax5.set_xlim(energies_M28N14[0], energies_M28N14[-1])
    ax5.set_ylim(0,2.9)
    ax5.set_xscale('symlog', linthreshx = 0.000001)  #symlog necessary for log scale on negative values
    plt.xlabel(r'$V/t$',x=0)

#############################################
#Inset Plot
    data_n16_VNEG1d5a2 = np.loadtxt("../Data/Pn_ABC_32_16_16_2_-1.5.dat")
    pntoa16_VNEG1d5a2 = data_n16_VNEG1d5a2[:,1]
    pn16_VNEG1d5 = pntoa16_VNEG1d5a2**(1/2)
    pn16_VNEG1d5 /= np.sum(pn16_VNEG1d5)
    nav=0.0
    sigma216=0.0
    for i,c in enumerate(pn16_VNEG1d5):
        nav=nav+i*c
    for i,c in enumerate(pn16_VNEG1d5):
        sigma216=sigma216+(i-nav)**2*c

    Halpha= np.linspace(1,10,10)
    HalphaG= np.linspace(1,10,10)
    alpha= np.linspace(1,10,10)
    Halpha[0] = np.sum(-pn16_VNEG1d5*np.log(pn16_VNEG1d5))
    HalphaG[0]=0.5*np.log(sigma216*2*np.pi*np.e)
    for alphai in range(2, 11):
        Halpha[alphai-1] = np.log(np.sum(pn16_VNEG1d5**alphai))/(1-alphai)
        HalphaG[alphai-1]=0.5*np.log(sigma216*2*np.pi*(alphai)**(1/(alphai-1)))
    left,bottom,width,height = [0.615,0.320,0.27,0.148]
    ax6=plt.subplot
    ax6 = fig.add_axes([left,bottom,width,height])
    ax6.plot(alpha, Halpha, 'o', markersize = 5.5, markerfacecolor = 'None', markeredgewidth = '1.0',color=green[0],zorder=4,label=r'$P_n$')
    ax6.plot(alpha, HalphaG, 'o', markersize = 2.5, markerfacecolor = "#000000", markeredgewidth = '0.25',color="#000000",zorder=4,label=r'$\mathcal{N}(\langle n\rangle,\sigma^2)$')
    ax6.tick_params(axis='both', which='both', right='off', top='off',labelright='off', labelleft='on', direction='in')
    ax6.set_xlabel(r'$\alpha$')
    ax6.set_ylabel(r'$H_\alpha$')
    ax6.xaxis.labelpad = -2
    ax6.yaxis.labelpad = -2
    plt.legend(loc=(0.200,0.420),fontsize=9,ncol=1,frameon=False,handletextpad=0.08)

###################################

    #Remove numbers from real axes of top plots
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.023)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    plt.savefig('higherAlphaDeltaS_N15N16.pdf', transparent=False)
