import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
import colors

orange = ["#4173b3"]  #Actually blue
blue = ["#ff8c00"]    #Actually orange
green = ["#66cdaa"]
red = ["#e85c47"]

alpha = [1.0,0.6,0.2]

for i,c in enumerate(alpha):
        blue.append(colors.get_alpha_hex(blue[0],alpha[i]))
        orange.append(colors.get_alpha_hex(orange[0],alpha[i]))
        green.append(colors.get_alpha_hex(green[0],alpha[i]))
        red.append(colors.get_alpha_hex(red[0],alpha[i]))

#orange[0] = 'k'
#orange[2] = 'None'

with plt.style.context('../IOP_large.mplstyle2'):

    #Top Plot: Probabilities vs Particle Number in Subsystem Size (For N=15); N=Total Number of Particles

    #V/t = -10
    data_n15_VNEG10a2 = np.loadtxt("../Data/Pn_PBC_30_15_15_2_-10.0.dat")
    data_n16_VNEG10a2 = np.loadtxt("../Data/Pn_ABC_32_16_16_2_-10.0.dat")

    data_n15_VNEG10a5 = np.loadtxt("../Data/Pn_PBC_30_15_15_5_-10.0.dat")
    data_n16_VNEG10a5 = np.loadtxt("../Data/Pn_ABC_32_16_16_5_-10.0.dat")

    data_n15_VNEG10a10 = np.loadtxt("../Data/Pn_PBC_30_15_15_10_-10.0.dat")
    data_n16_VNEG10a10 = np.loadtxt("../Data/Pn_ABC_32_16_16_10_-10.0.dat")

    #V/t = -1.5
    data_n15_VNEG1d5a2 = np.loadtxt("../Data/Pn_PBC_30_15_15_2_-1.5.dat")
    #data_n15_VNEG1d5a2_alpha = np.loadtxt("../Data/M30F15VNEG1.5a2Probs.dat")
    data_n16_VNEG1d5a2 = np.loadtxt("../Data/Pn_ABC_32_16_16_2_-1.5.dat")

    data_n15_VNEG1d5a5 = np.loadtxt("../Data/Pn_PBC_30_15_15_5_-1.5.dat")
    data_n16_VNEG1d5a5 = np.loadtxt("../Data/Pn_ABC_32_16_16_5_-1.5.dat")

    data_n15_VNEG1d5a10 = np.loadtxt("../Data/Pn_PBC_30_15_15_10_-1.5.dat")
    data_n16_VNEG1d5a10 = np.loadtxt("../Data/Pn_ABC_32_16_16_10_-1.5.dat")

    #V/t = 10
    data_n15_V10a2 = np.loadtxt("../Data/Pn_PBC_30_15_15_2_10.0.dat")
    data_n16_V10a2 = np.loadtxt("../Data/Pn_ABC_32_16_16_2_10.0.dat")

    data_n15_V10a5 = np.loadtxt("../Data/Pn_PBC_30_15_15_5_10.0.dat")
    data_n16_V10a5 = np.loadtxt("../Data/Pn_ABC_32_16_16_5_10.0.dat")

    data_n15_V10a10 = np.loadtxt("../Data/Pn_PBC_30_15_15_10_10.0.dat")
    data_n16_V10a10 = np.loadtxt("../Data/Pn_ABC_32_16_16_10_10.0.dat")

    #Load particle numbers
    n15List = data_n15_VNEG1d5a2[:,0]
    n16List = data_n16_VNEG1d5a2[:,0]

    #Save probabilities

    #15 particles
    #V/t = -10
    pntoa15_VNEG10a2 = data_n15_VNEG10a2[:,1]
    pn15_VNEG10 = pntoa15_VNEG10a2**(1/2)
    pn15_VNEG10 /= np.sum(pn15_VNEG10)
    pntoa15_VNEG10a2 = pn15_VNEG10
    pna15_VNEG10a2 = data_n15_VNEG10a2[:,2]
    pna15_VNEG10a2 = pna15_VNEG10a2**(1/2)
    pna15_VNEG10a2 /= np.sum(pna15_VNEG10a2)

    pntoa15_VNEG10a5 = data_n15_VNEG10a5[:,1]
    pntoa15_VNEG10a5 = pn15_VNEG10
    pna15_VNEG10a5 = data_n15_VNEG10a5[:,2]
    pna15_VNEG10a5 = pna15_VNEG10a5**(1/5)
    pna15_VNEG10a5 /= np.sum(pna15_VNEG10a5)

    pntoa15_VNEG10a10 = data_n15_VNEG10a10[:,1]
    pntoa15_VNEG10a10 = pn15_VNEG10
    pna15_VNEG10a10 = data_n15_VNEG10a10[:,2]
    pna15_VNEG10a10 = pna15_VNEG10a10**(1/10)
    pna15_VNEG10a10 /= np.sum(pna15_VNEG10a10)


    #V/t = -1.5
    pntoa15_VNEG1d5a2 = data_n15_VNEG1d5a2[:,1]
    pn15_VNEG1d5 = pntoa15_VNEG1d5a2**(1/2)
    pn15_VNEG1d5 /= np.sum(pn15_VNEG1d5)
    pntoa15_VNEG1d5a2 = pn15_VNEG1d5
    pna15_VNEG1d5a2 = data_n15_VNEG1d5a2[:,2]
    pna15_VNEG1d5a2 = pna15_VNEG1d5a2**(1/2)
    pna15_VNEG1d5a2 /= np.sum(pna15_VNEG1d5a2)

    pntoa15_VNEG1d5a5 = data_n15_VNEG1d5a5[:,1]
    pntoa15_VNEG1d5a5 = pn15_VNEG1d5
    pna15_VNEG1d5a5 = data_n15_VNEG1d5a5[:,2]
    pna15_VNEG1d5a5 = pna15_VNEG1d5a5**(1/5)
    pna15_VNEG1d5a5 /= np.sum(pna15_VNEG1d5a5)

    pntoa15_VNEG1d5a10 = data_n15_VNEG1d5a10[:,1]
    pntoa15_VNEG1d5a10 = pn15_VNEG1d5
    pna15_VNEG1d5a10 = data_n15_VNEG1d5a10[:,2]
    pna15_VNEG1d5a10 = pna15_VNEG1d5a10**(1/10)
    pna15_VNEG1d5a10 /= np.sum(pna15_VNEG1d5a10)

    #V/t = 10
    pntoa15_V10a2 = data_n15_V10a2[:,1]
    pn15_V10 = pntoa15_V10a2**(1/2)
    pn15_V10 /= np.sum(pn15_V10)
    pntoa15_V10a2 = pn15_V10
    pna15_V10a2 = data_n15_V10a2[:,2]
    pna15_V10a2 = pna15_V10a2**(1/2)
    pna15_V10a2 /= np.sum(pna15_V10a2)

    pntoa15_V10a5 = data_n15_V10a5[:,1]
    pntoa15_V10a5 = pn15_V10
    pna15_V10a5 = data_n15_V10a5[:,2]
    pna15_V10a5 = pna15_V10a5**(1/5)
    pna15_V10a5 /= np.sum(pna15_V10a5)

    pntoa15_V10a10 = data_n15_V10a10[:,1]
    pntoa15_V10a10 = pn15_V10
    pna15_V10a10 = data_n15_V10a10[:,2]
    pna15_V10a10 = pna15_V10a10**(1/10)
    pna15_V10a10 /= np.sum(pna15_V10a10)

    #16 particles
    #V/t = -10
    pntoa16_VNEG10a2 = data_n16_VNEG10a2[:,1]
    pn16_VNEG10 = pntoa16_VNEG10a2**(1/2)
    pn16_VNEG10 /= np.sum(pn16_VNEG10)
    pntoa16_VNEG10a2 = pn16_VNEG10
    pna16_VNEG10a2 = data_n16_VNEG10a2[:,2]
    pna16_VNEG10a2 = pna16_VNEG10a2**(1/2)
    pna16_VNEG10a2 /= np.sum(pna16_VNEG10a2)

    pntoa16_VNEG10a5 = data_n16_VNEG10a5[:,1]
    pntoa16_VNEG10a5 = pn16_VNEG10
    pna16_VNEG10a5 = data_n16_VNEG10a5[:,2]
    pna16_VNEG10a5 = pna16_VNEG10a5**(1/5)
    pna16_VNEG10a5 /= np.sum(pna16_VNEG10a5)

    pntoa16_VNEG10a10 = data_n16_VNEG10a10[:,1]
    pntoa16_VNEG10a10 = pn16_VNEG10
    pna16_VNEG10a10 = data_n16_VNEG10a10[:,2]
    pna16_VNEG10a10 = pna16_VNEG10a10**(1/10)
    pna16_VNEG10a10 /= np.sum(pna16_VNEG10a10)

    #V/t = -1.5
    pntoa16_VNEG1d5a2 = data_n16_VNEG1d5a2[:,1]
    pn16_VNEG1d5 = pntoa16_VNEG1d5a2**(1/2)
    pn16_VNEG1d5 /= np.sum(pn16_VNEG1d5)
    pntoa16_VNEG1d5a2 = pn16_VNEG1d5
    pna16_VNEG1d5a2 = data_n16_VNEG1d5a2[:,2]
    pna16_VNEG1d5a2 = pna16_VNEG1d5a2**(1/2)
    pna16_VNEG1d5a2 /= np.sum(pna16_VNEG1d5a2)

    pntoa16_VNEG1d5a5 = data_n16_VNEG1d5a5[:,1]
    pntoa16_VNEG1d5a5 = pn16_VNEG1d5
    pna16_VNEG1d5a5 = data_n16_VNEG1d5a5[:,2]
    pna16_VNEG1d5a5 = pna16_VNEG1d5a5**(1/5)
    pna16_VNEG1d5a5 /= np.sum(pna16_VNEG1d5a5)

    pntoa16_VNEG1d5a10 = data_n16_VNEG1d5a10[:,1]
    pntoa16_VNEG1d5a10 = pn16_VNEG1d5
    pna16_VNEG1d5a10 = data_n16_VNEG1d5a10[:,2]
    pna16_VNEG1d5a10 = pna16_VNEG1d5a10**(1/10)
    pna16_VNEG1d5a10 /= np.sum(pna16_VNEG1d5a10)

    #V/t = 10
    pntoa16_V10a2 = data_n16_V10a2[:,1]
    pn16_V10 = pntoa16_V10a2**(1/2)
    pn16_V10 /= np.sum(pn16_V10)
    pntoa16_V10a2 = pn16_V10
    pna16_V10a2 = data_n16_V10a2[:,2]
    pna16_V10a2 = pna16_V10a2**(1/2)
    pna16_V10a2 /= np.sum(pna16_V10a2)

    pntoa16_V10a5 = data_n16_V10a5[:,1]
    pntoa16_V10a5 = pn16_V10
    pna16_V10a5 = data_n16_V10a5[:,2]
    pna16_V10a5 = pna16_V10a5**(1/5)
    pna16_V10a5 /= np.sum(pna16_V10a5)

    pntoa16_V10a10 = data_n16_V10a10[:,1]
    pntoa16_V10a10 = pn16_V10
    pna16_V10a10 = data_n16_V10a10[:,2]
    pna16_V10a10 = pna16_V10a10**(1/10)
    pna16_V10a10 /= np.sum(pna16_V10a10)

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(3,2)

    #Shift V/t=-10,-1.5,10 data sets vertically
    shiftV10 = 0
    shiftVNEG1d5 = 0
    shiftVNEG10 = 0

    #V/t=10 , N=15
    ax1 = plt.subplot(gs[0])

    #alpha=2
    ax1.plot(n15List, pn15_V10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 7.5, markerfacecolor = orange[2], markeredgewidth = '0.25',color=orange[0],zorder=4)
    ax1.plot(n15List, pna15_V10a2, 'o', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 5.5, markerfacecolor =blue[2], markeredgewidth = '0.25',color=blue[0],zorder=5)

    #alpha=5
    ax1.plot(n15List, pna15_V10a5, 'o', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 3.75, markerfacecolor = green[2], markeredgewidth = '0.25',color=green[0],zorder=5)

    #alpha=10
    ax1.plot(n15List, pna15_V10a10, 'o', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 1.50, markerfacecolor = red[2], markeredgewidth = '0.25',color=red[0],zorder=5)

    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off',labelleft='on', direction='in')
    ax1.set_yscale('log')
    ax1.set_ylim(1E-35,1E+02)

    #V/t=10 , N=16
    ax2 = plt.subplot(gs[1])

    #alpha=2
    ax2.plot(n16List, pn16_V10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 7.5, markerfacecolor = orange[2], markeredgewidth = '0.25',color=orange[0],zorder=4)
    ax2.plot(n16List, pna16_V10a2, 'o', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 5.5, markerfacecolor =blue[2], markeredgewidth = '0.25',color=blue[0],zorder=5)

    #alpha=5
    ax2.plot(n16List, pna16_V10a5, 'o', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 3.75, markerfacecolor =green[2], markeredgewidth = '0.25',color=green[0],zorder=5)

    #alpha=10
    ax2.plot(n16List, pna16_V10a10, 'o', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 1.50, markerfacecolor =red[2], markeredgewidth = '0.25',color=red[0],zorder=5)

    ax2.tick_params(axis='both', which='both', right='off', top='off',labelright='off', labelleft='off',direction='in')
    ax2.xaxis.set_ticks(np.arange(0, 17, 4))
    ax2.set_yscale('log')
    ax2.set_ylim(1E-35,1E+02)

    #V/t=-1.5 , N=15
    ax3 = plt.subplot(gs[2])

    #alpha=2
    ax3.plot(n15List, pn15_VNEG1d5, 'o', label=r'$P_n$', markersize = 7.5, markerfacecolor = orange[2], markeredgewidth = '0.25',color=orange[0],zorder=4)

    ax3.plot(n15List, pna15_VNEG1d5a2, 'o', label=r'$(P_{n,2})^{1/2}$', markersize = 5.5, markerfacecolor =blue[2], markeredgewidth = '0.25',color=blue[0],zorder=5)

    #alpha=5
    ax3.plot(n15List, pna15_VNEG1d5a5, 'o', label=r'$(P_{n,5})^{1/5}$', markersize = 3.75, markerfacecolor =green[2], markeredgewidth = '0.25',color=green[0],zorder=5)

    #alpha=10
    ax3.plot(n15List, pna15_VNEG1d5a10, 'o', label=r'$(P_{n,10})^{1/10}$', markersize = 1.50, markerfacecolor =red[2], markeredgewidth = '0.25',color=red[0],zorder=5)

    ax3.tick_params(axis='both', which='both', right='off', top='off',labelright='off', labelleft='on', direction='in')
    ax3.set_yscale('log')
    ax3.set_ylim(1E-27,1E+01)
    #plt.legend(loc=(0.236,0.058), fontsize=11,ncol=1,frameon=False,handletextpad=0.08)

    #V/t=-1.5 , N=16
    ax4 = plt.subplot(gs[3])

    #alpha=2
    ax4.plot(n16List, pn16_VNEG1d5, 'o', label=r'$P_n$', markersize = 7.5, markerfacecolor = orange[2], markeredgewidth = '0.25',color=orange[0],zorder=4)
    ax4.plot(n16List, pna16_VNEG1d5a2, 'o', label=r'$(P_{n,2})^{1/2}$', markersize = 5.5, markerfacecolor =blue[2], markeredgewidth = '0.25',color=blue[0],zorder=5)

    #alpha=5
    ax4.plot(n16List, pna16_VNEG1d5a5, 'o', label=r'$(P_{n,5})^{1/5}$', markersize = 3.75, markerfacecolor =green[2], markeredgewidth = '0.25',color=green[0],zorder=5)

    #alpha=10
    ax4.plot(n16List, pna16_VNEG1d5a10, 'o', label=r'$(P_{n,10})^{1/10}$', markersize = 1.50, markerfacecolor =red[2], markeredgewidth = '0.25',color=red[0],zorder=5)

    ax4.tick_params(axis='both', which='both', right='off', top='off',labelright='off', labelleft='off', direction='in')
    ax4.xaxis.set_ticks(np.arange(0, 17, 4))
    ax4.set_yscale('log')
    ax4.set_ylim(1E-27,1E+01)
    #plt.legend(loc=(0.236,0.058), fontsize=11,ncol=1,frameon=False,handletextpad=0.08)

    #V/t=-10 , N=15
    ax5 = plt.subplot(gs[4])

    #alpha=2
    ax5.plot(n15List, pn15_VNEG10, 'o', label=r'$P_n$', markersize = 7.5, markerfacecolor = orange[2], markeredgewidth = '0.25',color=orange[0],zorder=4)
    ax5.plot(n15List, pna15_VNEG10a2, 'o', label=r'$\mathcal{A}_2(P_{n,2})^{\frac{1}{2}}$', markersize = 5.5, markerfacecolor =blue[2], markeredgewidth = '0.25',color=blue[0],zorder=5)

    #alpha=5
    ax5.plot(n15List, pna15_VNEG10a5, 'o', label=r'$\mathcal{A}_5(P_{n,5})^{\frac{1}{5}}$', markersize = 3.75, markerfacecolor =green[2], markeredgewidth = '0.25',color=green[0],zorder=5)

    #alpha=10
    ax5.plot(n15List, pna15_VNEG10a10, 'o', label=r'$\mathcal{A}_{10}(P_{n,10})^{\frac{1}{10}}$', markersize = 1.50, markerfacecolor =red[2], markeredgewidth = '0.25',color=red[0],zorder=5)

    ax5.tick_params(axis='both', which='both', right='off', top='off',labelright='off', labelleft='on', direction='in')
    ax5.set_yscale('log')
    ax5.set_ylim(3E-02 - 0.0008,7E-02 + 0.003)
    ax5.set_xlabel(r'$n$')
    plt.legend(loc=(0.120,0.020), fontsize=11,ncol=1,frameon=False,handletextpad=0.08)

    #V/t=-10 , N=16
    ax6 = plt.subplot(gs[5])

    #alpha=2
    ax6.plot(n16List, pn16_VNEG10, 'o', label=r'$P_n$', markersize = 7.5, markerfacecolor = orange[2], markeredgewidth = '0.25',color=orange[0],zorder=4)
    ax6.plot(n16List, pna16_VNEG10a2, 'o', label=r'$(P_{n,2})^{\frac{1}{2}}$', markersize = 5.5, markerfacecolor =blue[2], markeredgewidth = '0.25',color=blue[0],zorder=5)

    #alpha=5
    ax6.plot(n16List, pna16_VNEG10a5, 'o', label=r'$(P_{n,5})^{\frac{1}{5}}$', markersize =3.75, markerfacecolor =green[2], markeredgewidth = '0.25',color=green[0],zorder=5)

    #alpha=10
    ax6.plot(n16List, pna16_VNEG10a10, 'o', label=r'$(P_{n,10})^{\frac{1}{10}}$', markersize = 1.50, markerfacecolor =red[2], markeredgewidth = '0.25',color=red[0],zorder=5)

    ax6.tick_params(axis='both', which='both', right='off', top='off',labelright='off', labelleft='off', direction='in')
    ax6.xaxis.set_ticks(np.arange(0, 17, 4))
    ax6.set_yscale('log')
    ax6.set_ylim(3E-02 - 0.0008,7E-02 + 0.003)
    ax6.set_xlabel(r'$n$')

    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.15)

    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    #Inlude annotations denoting the interaction strength V/t
    x1,y1 = 0.355,0.085
    x2,y2 = 0.5,0.5
    fs = 13
    #ax1.annotate(r'$\frac{V}{t}=10$',
    #        xy=(x1, y1), xycoords='axes fraction',
    #        xytext=(x2, y2), textcoords='offset points',
    #        )
    ax2.annotate(r'$\frac{V}{t}=10$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )
    #ax3.annotate(r'$\frac{V}{t}=-1.5$',
    #        xy=(x1, y1), xycoords='axes fraction',
    #        xytext=(x2, y2), textcoords='offset points',
    #        )
    ax4.annotate(r'$\frac{V}{t}=-1.5$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )
    #ax5.annotate(r'$\frac{V}{t}=-10$',
    #        xy=(x1, y1), xycoords='axes fraction',
    #        xytext=(x2, y2), textcoords='offset points',
    #        )
    ax6.annotate(r'$\frac{V}{t}=-10$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points', fontsize = fs
            )

    #Inlude annotations denoting the interaction strength V/t
    x1,y1 = 0.02,0.86
    x2,y2 = 0.5,0.5
    ax1.annotate(r'$N=15$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points',
            )
    ax2.annotate(r'$N=16$',
            xy=(x1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points',
            )
    plt.savefig('alphaCollapse.pdf')
