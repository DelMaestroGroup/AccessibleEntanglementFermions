#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
import colors

orange = ["#4173b3"] #Actually blue  
blue = ["#ff8c00"]   #Actually orange 
green = ["#66cdaa"]
red = ["#e85c47"]

alpha = [1.0,0.70,0.45,0.2,0.05]

for i,c in enumerate(alpha):
        blue.append(colors.get_alpha_hex(blue[0],alpha[i]))
        orange.append(colors.get_alpha_hex(orange[0],alpha[i]))
        green.append(colors.get_alpha_hex(green[0],alpha[i]))
        red.append(colors.get_alpha_hex(red[0],alpha[i]))
        
with plt.style.context('../IOP_large.mplstyle2'):

    #Top Plot: Probabilities vs Particle Number in Subsystem Size (For N=15); N=Total Number of Particles   
       
    #V/t = +-1.5
    data_n15_V1d5a2 = np.loadtxt("M30F15V1.5a2Probs.dat")
    data_n16_V1d5a2 = np.loadtxt("M32F16V1.5a2Probs.dat")
    data_n15_VNEG1d5a2 = np.loadtxt("M30F15VNEG1.5a2Probs.dat")
    data_n16_VNEG1d5a2 = np.loadtxt("M32F16VNEG1.5a2Probs.dat")
    
    #V/t = +- 1.0
    data_n15_V1a2 = np.loadtxt("M30F15V1.0a2Probs.dat")
    data_n16_V1a2 = np.loadtxt("M32F16V1.0a2Probs.dat")
    data_n15_VNEG1a2 = np.loadtxt("M30F15VNEG1.0a2Probs.dat")
    data_n16_VNEG1a2 = np.loadtxt("M32F16VNEG1.0a2Probs.dat")

    #V/t = 0
    data_n15_V0a2 = np.loadtxt("M30F15V0.0a2Probs.dat")
    data_n16_V0a2 = np.loadtxt("M32F16V0.0a2Probs.dat")

    #Load particle numbers 
    n15List = data_n15_VNEG1d5a2[:,0]
    n16List = data_n16_VNEG1d5a2[:,0]

    #Lists of Interaction Strengths and Luttinger Parameters
    VotList = [-1.5,-1.0,0.0,1.0,1.5]       
    k = [np.pi/(2*np.arccos(-Vot/2)) for Vot in VotList] 
    
    #Save probabilities and rescale with Luttinger Parameter
    
    #15 particles
    #V/t = +-1.5
    pna15_V1d5a2 = data_n15_V1d5a2[:,2]
    pna15_V1d5a2 = pna15_V1d5a2**(k[4])
    pna15_V1d5a2 /= np.sum(pna15_V1d5a2)
     
    pna15_VNEG1d5a2 = data_n15_VNEG1d5a2[:,2]
    pna15_VNEG1d5a2 = pna15_VNEG1d5a2**(k[0])
    pna15_VNEG1d5a2 /= np.sum(pna15_VNEG1d5a2)
    
    #V/t = +-1.0
    pna15_V1a2 = data_n15_V1a2[:,2]
    pna15_V1a2 = pna15_V1a2**(k[3])
    pna15_V1a2 /= np.sum(pna15_V1a2)
    
    pna15_VNEG1a2 = data_n15_VNEG1a2[:,2]
    pna15_VNEG1a2 = pna15_VNEG1a2**(k[1])
    pna15_VNEG1a2 /= np.sum(pna15_VNEG1a2)

    #V/t = 0.0
    pna15_V0a2 = data_n15_V0a2[:,2]
    pna15_V0a2 = pna15_V0a2**(k[2])
    pna15_V0a2 /= np.sum(pna15_V0a2)

    
    #16 particles
    #V/t = +-1.5
    pna16_V1d5a2 = data_n16_V1d5a2[:,2]
    pna16_V1d5a2 = pna16_V1d5a2**(k[4])
    pna16_V1d5a2 /= np.sum(pna16_V1d5a2)
    
    pna16_VNEG1d5a2 = data_n16_VNEG1d5a2[:,2]
    pna16_VNEG1d5a2 = pna16_VNEG1d5a2**(k[0])
    pna16_VNEG1d5a2 /= np.sum(pna16_VNEG1d5a2)
    
    #V/t = +-1.0
    pna16_V1a2 = data_n16_V1a2[:,2]
    pna16_V1a2 = pna16_V1a2**(k[3])
    pna16_V1a2 /= np.sum(pna16_V1a2)
    
    pna16_VNEG1a2 = data_n16_VNEG1a2[:,2]
    pna16_VNEG1a2 = pna16_VNEG1a2**(k[1])
    pna16_VNEG1a2 /= np.sum(pna16_VNEG1a2)

    #V/t = 0.0
    pna16_V0a2 = data_n16_V0a2[:,2]
    pna16_V0a2 = pna16_V0a2**(k[2])
    pna16_V0a2 /= np.sum(pna16_V0a2)

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2,1)
    
    #N=15
    ax1 = plt.subplot(gs[0])
    
    #List of Markersizes
    ms = ['Nan',2.50,5.25,8.00,10.75,13.50]

    #alpha=2
    ax1.plot(n15List, pna15_V1d5a2, 'o', label=r'$%.2f, 1.5$'%(k[4]), markersize = ms[5], markerfacecolor = blue[5], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax1.plot(n15List, pna15_V1a2, 'o', label=r'$%.2f, 1.0$'%(k[3]), markersize = ms[4], markerfacecolor = blue[4], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax1.plot(n15List, pna15_V0a2, 'o', label=r'$%.2f, 0.0$'%(k[2]), markersize = ms[3], markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax1.plot(n15List, pna15_VNEG1a2, 'o', label=r'$%.2f, -1.0$'%(k[1]), markersize = ms[2], markerfacecolor = blue[2], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax1.plot(n15List, pna15_VNEG1d5a2, 'o', label=r'$%.2f, -1.5$'%(k[0]), markersize = ms[1], markerfacecolor = blue[1], markeredgewidth = '0.25',color=blue[0],zorder=4)



    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off',labelleft='on', direction='in')
    ax1.xaxis.set_ticks(np.arange(0, 16, 3))
    ax1.set_yscale('log')
    ax1.set_ylabel(r'$(P_{n,2,K})^{K}$')
    #ax1.set_ylim(1E-35,1E+02)
    ax1.text(13,1E-06,r'$N=15$')
    
    lgnd = plt.legend(loc=(0.355,0.125), fontsize=11,ncol=1,frameon=False,handletextpad=0.08,title=r'$K, V/t$')
    lgnd.get_title().set_position((7.0,0))
  
    #N=16
    ax2 = plt.subplot(gs[1])

    #alpha=2
    ax2.plot(n16List, pna16_V1d5a2, 'o', label=r'$a$', markersize = ms[5], markerfacecolor = blue[5], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax2.plot(n16List, pna16_V1a2, 'o', label=r'$a$', markersize = ms[4], markerfacecolor = blue[4], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax2.plot(n16List, pna16_V0a2, 'o', label=r'$a$', markersize = ms[3], markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax2.plot(n16List, pna16_VNEG1a2, 'o', label=r'$a$', markersize = ms[2], markerfacecolor = blue[2], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax2.plot(n16List, pna16_VNEG1d5a2, 'o', label=r'$a$', markersize = ms[1], markerfacecolor = blue[1], markeredgewidth = '0.25',color=blue[0],zorder=4)

    ax2.tick_params(axis='both', which='both', right='off', top='off',labelright='off', labelleft='on',direction='in')
    ax2.xaxis.set_ticks(np.arange(0, 17, 4))
    ax2.set_yscale('log')
    ax2.set_xlabel(r'$n$')
    ax2.set_ylabel(r'$(P_{n,2,K})^{K}$')
    #ax2.set_ylim(1E-35,1E+02)
    ax2.text(13.9,1E-06,r'$N=16$')

          
    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.15)
    
    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)
    
    plt.savefig('kDependencePna.pdf')
