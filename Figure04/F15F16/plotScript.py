#Top Plot: One Particle Entanglement entropy dependence on the interaction potential
#Bottom Plot: Entanglement entropies for equal particle number bipartitions at various system sizes

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.

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

alpha = [0.2,0.1,0.0]
beta = [1.0,0.6,0.2]

for i,c in enumerate(alpha):
        blue.append(colors.get_alpha_hex(blue[0],beta[i]))
        orange.append(colors.get_alpha_hex(orange[0],beta[i]))
        green.append(colors.get_alpha_hex(green[0],beta[i]))
        red.append(colors.get_alpha_hex(red[0],beta[i]))

with plt.style.context('../IOP_large.mplstyle2'):

    #Top Plot: Probabilities vs Particle Number in Subsystem Size (For N=15); N=Total Number of Particles
    
    #V/t = -10
    data_n15_VNEG10a2 = np.loadtxt("M30F15VNEG10.0a2Probs.dat")
    data_n16_VNEG10a2 = np.loadtxt("M32F16VNEG10.0a2Probs.dat")
    
    data_n15_VNEG10a5 = np.loadtxt("M30F15VNEG10.0a5Probs.dat")
    data_n16_VNEG10a5 = np.loadtxt("M32F16VNEG10.0a5Probs.dat")
    
    data_n15_VNEG10a10 = np.loadtxt("M30F15VNEG10.0a10Probs.dat")
    data_n16_VNEG10a10 = np.loadtxt("M32F16VNEG10.0a10Probs.dat")
       
    #V/t = -1.5
    data_n15_VNEG1d5a2 = np.loadtxt("M30F15VNEG1.5a2Probs.dat")
    data_n16_VNEG1d5a2 = np.loadtxt("M32F16VNEG1.5a2Probs.dat")
    
    data_n15_VNEG1d5a5 = np.loadtxt("M30F15VNEG1.5a5Probs.dat")
    data_n16_VNEG1d5a5 = np.loadtxt("M32F16VNEG1.5a5Probs.dat")
    
    data_n15_VNEG1d5a10 = np.loadtxt("M30F15VNEG1.5a10Probs.dat")
    data_n16_VNEG1d5a10 = np.loadtxt("M32F16VNEG1.5a10Probs.dat")
    
    #V/t = 10
    data_n15_V10a2 = np.loadtxt("M30F15V10.0a2Probs.dat")
    data_n16_V10a2 = np.loadtxt("M32F16V10.0a2Probs.dat")
    
    data_n15_V10a5 = np.loadtxt("M30F15V10.0a5Probs.dat")
    data_n16_V10a5 = np.loadtxt("M32F16V10.0a5Probs.dat")
    
    data_n15_V10a10 = np.loadtxt("M30F15V10.0a10Probs.dat")
    data_n16_V10a10 = np.loadtxt("M32F16V10.0a10Probs.dat")
    
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
    
    pntoa15_VNEG10a10 = data_n15_VNEG10a10[:,1]
    pntoa15_VNEG10a10 = pn15_VNEG10
    pna15_VNEG10a10 = data_n15_VNEG10a10[:,2]


    #V/t = -1.5
    pntoa15_VNEG1d5a2 = data_n15_VNEG1d5a2[:,1]
    pn15_VNEG1d5 = pntoa15_VNEG1d5a2**(1/2)
    pn15_VNEG1d5 /= np.sum(pn15_VNEG1d5)
    pntoa15_VNEG1d5a2 = pn15_VNEG1d5
    pna15_VNEG1d5a2 = data_n15_VNEG1d5a2[:,2]
    pna15_VNEG1d5a2 = pna15_VNEG1d5a2**(1/2)
    pna15_VNEG1d5a2 /= np.sum(pna15_VNEG1d5a2)

    pntoa15_VNEG1d5a5 = data_n15_VNEG1d5a5[:,1]
    pna15_VNEG1d5a5 = data_n15_VNEG1d5a5[:,2]
    
    pntoa15_VNEG1d5a10 = data_n15_VNEG1d5a10[:,1]
    pna15_VNEG1d5a10 = data_n15_VNEG1d5a10[:,2]

    #V/t = 10
    pntoa15_V10a2 = data_n16_V10a2[:,1]
    pn15_V10 = pntoa15_V10a2**(1/2)
    pn15_V10 /= np.sum(pn15_V10)
    pntoa15_V10a2 = pn15_V10
   # pna15_V10a2 = data_n15_V10a2[:,2]
    pna15_V10a2 = data_n16_V10a10[:,1]
    pna15_V10a2 = pna15_V10a2**(1/10)
    pna15_V10a2 /= np.sum(pna15_V10a2)

    pntoa15_V10a5 = data_n15_V10a5[:,1]
    pna15_V10a5 = data_n15_V10a5[:,2]
    
    pntoa15_V10a10 = data_n15_V10a10[:,1]
    pna15_V10a10 = data_n15_V10a10[:,2]

    #16 particles
    #V/t = -10
    pntoa16_VNEG10a2 = data_n15_VNEG10a2[:,1]
    pna16_VNEG10a2 = data_n15_VNEG10a2[:,2]

    pntoa16_VNEG10a5 = data_n15_VNEG10a5[:,1]
    pna16_VNEG10a5 = data_n15_VNEG10a5[:,2]
    
    pntoa16_VNEG10a10 = data_n15_VNEG10a10[:,1]
    pna16_VNEG10a10 = data_n15_VNEG10a10[:,2]


    #V/t = -1.5
    pntoa16_VNEG1d5a2 = data_n16_VNEG1d5a2[:,1]
    pna16_VNEG1d5a2 = data_n16_VNEG1d5a2[:,2]

    pntoa16_VNEG1d5a5 = data_n16_VNEG1d5a5[:,1]
    pna16_VNEG1d5a5 = data_n16_VNEG1d5a5[:,2]
    
    pntoa16_VNEG1d5a10 = data_n16_VNEG1d5a10[:,1]
    pna16_VNEG1d5a10 = data_n16_VNEG1d5a10[:,2]

    #V/t = 10
    pntoa16_V10a2 = data_n16_V10a2[:,1]
    pna16_V10a2 = data_n16_V10a2[:,2]

    pntoa16_V10a5 = data_n16_V10a5[:,1]
    pna16_V10a5 = data_n16_V10a5[:,2]
    
    pntoa16_V10a10 = data_n16_V10a10[:,1]
    pna16_V10a10 = data_n16_V10a10[:,2]

    #Fit Quadratic to test Gaussian Hypothesis
    ############################################################################################################
    
    #Determine average n_A
    n15Ave = 7.5
    n16Ave = 8.0
    
    #15 particles
    #V/t = -10
    lnpntoa15_VNEG10a2 = np.log(data_n15_VNEG10a2[:,1])
    lnpna15_VNEG10a2 = np.log(data_n15_VNEG10a2[:,2])

    lnpntoa15_VNEG10a5 = np.log(data_n15_VNEG10a5[:,1])
    lnpna15_VNEG10a5 = np.log(data_n15_VNEG10a5[:,2])
    
    lnpntoa15_VNEG10a10 = np.log(data_n15_VNEG10a10[:,1])
    lnpna15_VNEG10a10 = np.log(data_n15_VNEG10a10[:,2])

    #V/t = -1.5
    lnpntoa15_VNEG1d5a2 = np.log(data_n15_VNEG1d5a2[:,1])
    lnpna15_VNEG1d5a2 = np.log(data_n15_VNEG1d5a2[:,2])

    lnpntoa15_VNEG1d5a5 = np.log(data_n15_VNEG1d5a5[:,1])
    lnpna15_VNEG1d5a5 = np.log(data_n15_VNEG1d5a5[:,2])
    
    lnpntoa15_VNEG1d5a10 = np.log(data_n15_VNEG1d5a10[:,1])
    lnpna15_VNEG1d5a10 = np.log(data_n15_VNEG1d5a10[:,2])

    #V/t = 10
    lnpntoa15_V10a2 = np.log(data_n15_V10a2[:,1])
    lnpna15_V10a2 = np.log(data_n15_V10a2[:,2])

    lnpntoa15_V10a5 = np.log(data_n15_V10a5[:,1])
    lnpna15_V10a5 = np.log(data_n15_V10a5[:,2])
    
    lnpntoa15_V10a10 = np.log(data_n15_V10a10[:,1])
    lnpna15_V10a10 = np.log(data_n15_V10a10[:,2])

    #16 particles
    #V/t = -10
    lnpntoa16_VNEG10a2 = np.log(data_n16_VNEG10a2[:,1])
    lnpna16_VNEG10a2 = np.log(data_n16_VNEG10a2[:,2])

    lnpntoa16_VNEG10a5 = np.log(data_n16_VNEG10a5[:,1])
    lnpna16_VNEG10a5 = np.log(data_n16_VNEG10a5[:,2])
    
    lnpntoa16_VNEG10a10 = np.log(data_n16_VNEG10a10[:,1])
    lnpna16_VNEG10a10 = np.log(data_n16_VNEG10a10[:,2])

    #V/t = -1.5
    lnpntoa16_VNEG1d5a2 = np.log(data_n16_VNEG1d5a2[:,1])
    lnpna16_VNEG1d5a2 = np.log(data_n16_VNEG1d5a2[:,2])
    
    lnpntoa16_VNEG1d5a5 = np.log(data_n16_VNEG1d5a5[:,1])
    lnpna16_VNEG1d5a5 = np.log(data_n16_VNEG1d5a5[:,2])
    
    lnpntoa16_VNEG1d5a10 = np.log(data_n16_VNEG1d5a10[:,1])
    lnpna16_VNEG1d5a10 = np.log(data_n16_VNEG1d5a10[:,2])

    #V/t = 10
    lnpntoa16_V10a2 = np.log(data_n16_V10a2[:,1])
    lnpna16_V10a2 = np.log(data_n16_V10a2[:,2])

    lnpntoa16_V10a5 = np.log(data_n16_V10a5[:,1])
    lnpna16_V10a5 = np.log(data_n16_V10a5[:,2])
   
    lnpntoa16_V10a10 = np.log(data_n16_V10a10[:,1])
    lnpna16_V10a10 = np.log(data_n16_V10a10[:,2])

    #coeffs15 = np.polyfit((n15List[2:-2]-n15Ave), lnpntoa15[2:-2], deg=2)
    #coeffs16 = np.polyfit((n16List[2:-2]-n16Ave), lnpntoa16[2:-2], deg=2)
    
    #var15 = np.sum(n15List**2 * pntoa15) - n15Ave**2
    #var16 = np.sum(n16List**2 * pntoa16) - n16Ave**2
    
    #print("Variance N=15: ", var15)
    #print("Variance N=16: ", var16)
 
    #A15 , B15, C15 = coeffs15[0], coeffs15[1], coeffs15[2]
    #A16 , B16, C16 = coeffs16[0], coeffs16[1], coeffs16[2]
    
    #A13 = - 1/(2*var13) 
    #A14 = - 1/(2*var14) 
    
    #C13 = (0.5)*np.log(1/(2*np.pi*var13))
    #C14 = (0.5)*np.log(1/(2*np.pi*var14))
    
    #print("Coeffs of N=15: ", coeffs15)
    #print("Coeffs of N=16: ", coeffs16)
        
    #n15fit = np.linspace(0,15,1000)
    #n16fit = np.linspace(0,16,1000)
    
    #lnpntoa15fit = A15*(n15fit-n15Ave)**2 + B15*(n15fit-n15Ave) + C15
    #lnpntoa16fit = A16*(n16fit-n16Ave)**2 + B16*(n16fit-n16Ave) + C16

    
    ############################################################################################################

    #Create the figure
    fig = plt.figure()

    #Set height ratios for subplots
    gs = gridspec.GridSpec(2,1)

    #Shift V/t=-10,-1.5,10 data sets vertically
    shiftV10 = 1300
    shiftVNEG1d5 = -100
    shiftVNEG10 = -1400

    #V/t=-10 , N=15
    ax1 = plt.subplot(gs[0])

    #Legend (hacky, very ugly way)
    #Define some empty plots with the corresponding labels
    ax1.plot([],[],'o',mfc=blue[3],color=blue[0],markersize=4,mew=0.25,label=r'$\ln P_{n}^{(\alpha=2)}$')
    ax1.plot([],[],'o',mfc=green[3],color=green[0],markersize=4,mew=0.25,label=r'$\ln P_{n}^{(\alpha=5)}$')
    ax1.plot([],[],'o',mfc=red[3],color=red[0],markersize=4,mew=0.25,label=r'$\ln P_{n}^{(\alpha=10)}$')
    ax1.plot([],[],'.',mfc=blue[0],color=blue[0],markersize=4,mew=0.25,label=r'$\ln P_{(n,\alpha=2)}$')
    ax1.plot([],[],'.',mfc=green[0],color=green[0],markersize=4,mew=0.25,label=r'$\ln P_{(n,\alpha=5)}$')
    ax1.plot([],[],'.',mfc=red[0],color=red[0],markersize=4,mew=0.25,label=r'$\ln P_{(n,\alpha=10)}$')
      
    lgnd1 = plt.legend(loc=(0.27,0.14), fontsize=6, handlelength=3,handleheight=2,title=r'',ncol=2,frameon=False)

    #alpha=2
    ax1.plot(n15List, lnpntoa15_VNEG10a2+shiftVNEG10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax1.plot(n15List, lnpna15_VNEG10a2+shiftVNEG10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color=blue[0],zorder=5)
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=5
    ax1.plot(n15List, lnpntoa15_VNEG10a5+shiftVNEG10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 3, markerfacecolor = green[3], markeredgewidth = '0.25',color=green[0],zorder=4)
    ax1.plot(n15List, lnpna15_VNEG10a5+shiftVNEG10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 3, markerfacecolor =green[0], markeredgewidth = '0.25',color=green[0],zorder=5)
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=10
    ax1.plot(n15List, lnpntoa15_VNEG10a10+shiftVNEG10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 2, markerfacecolor = red[3], markeredgewidth = '0.25',color=red[0],zorder=4)
    ax1.plot(n15List, lnpna15_VNEG10a10+shiftVNEG10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 2, markerfacecolor =red[0], markeredgewidth = '0.25',color=red[0],zorder=5)
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')
 
    #V/t=-1.5 , N=15

    #alpha=2
    ax1.plot(n15List, lnpntoa15_VNEG1d5a2+shiftVNEG1d5, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0])
    ax1.plot(n15List, lnpna15_VNEG1d5a2+shiftVNEG1d5, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color=blue[0])
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=5
    ax1.plot(n15List, lnpntoa15_VNEG1d5a5+shiftVNEG1d5, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = green[3], markeredgewidth = '0.25',color=green[0])
    ax1.plot(n15List, lnpna15_VNEG1d5a5+shiftVNEG1d5, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =green[0], markeredgewidth = '0.25',color=green[0])
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=10
    ax1.plot(n15List, lnpntoa15_VNEG1d5a10+shiftVNEG1d5, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = red[3], markeredgewidth = '0.25',color=red[0])
    ax1.plot(n15List, lnpna15_VNEG1d5a10+shiftVNEG1d5, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =red[0], markeredgewidth = '0.25',color=red[0])
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')
     
    #V/t=10 , N=15

    #alpha=2
    ax1.plot(n15List, lnpntoa15_V10a2+shiftV10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0])
    ax1.plot(n15List, lnpna15_V10a2+shiftV10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color=blue[0])
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=5
    ax1.plot(n15List, lnpntoa15_V10a5+shiftV10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = green[3], markeredgewidth = '0.25',color=green[0])
    ax1.plot(n15List, lnpna15_V10a5+shiftV10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor = green[0], markeredgewidth = '0.25',color=green[0])
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=10
    ax1.plot(n15List, lnpntoa15_V10a10+shiftV10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = red[3], markeredgewidth = '0.25',color=red[0])
    ax1.plot(n15List, lnpna15_V10a10+shiftV10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor = red[0], markeredgewidth = '0.25',color=red[0])
    #ax1.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    ax1.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax1.xaxis.set_ticks(np.arange(0, 16, 1))    
 
    #V/t=-10 , N=16
    ax2 = plt.subplot(gs[1])

    #alpha=2
    ax2.plot(n16List, lnpntoa16_VNEG10a2+shiftVNEG10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0],zorder=4)
    ax2.plot(n16List, lnpna16_VNEG10a2+shiftVNEG10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color=blue[0],zorder=5)
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=5
    ax2.plot(n16List, lnpntoa16_VNEG10a5+shiftVNEG10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 3, markerfacecolor = green[3], markeredgewidth = '0.25',color=green[0],zorder=4)
    ax2.plot(n16List, lnpna16_VNEG10a5+shiftVNEG10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 3, markerfacecolor =green[0], markeredgewidth = '0.25',color=green[0],zorder=5)
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=10
    ax2.plot(n16List, lnpntoa16_VNEG10a10+shiftVNEG10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 2, markerfacecolor = red[3], markeredgewidth = '0.25',color=red[0],zorder=4)
    ax2.plot(n16List, lnpna16_VNEG10a10+shiftVNEG10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 2, markerfacecolor =red[0], markeredgewidth = '0.25',color=red[0],zorder=5)
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #V/t=-1.5 , N=16

    #alpha=2
    ax2.plot(n16List, lnpntoa16_VNEG1d5a2+shiftVNEG1d5, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0])
    ax2.plot(n16List, lnpna16_VNEG1d5a2+shiftVNEG1d5, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color=blue[0])
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=5
    ax2.plot(n16List, lnpntoa16_VNEG1d5a5+shiftVNEG1d5, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = green[3], markeredgewidth = '0.25',color=green[0])
    ax2.plot(n16List, lnpna16_VNEG1d5a5+shiftVNEG1d5, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =green[0], markeredgewidth = '0.25',color=green[0])
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=10
    ax2.plot(n16List, lnpntoa16_VNEG1d5a10+shiftVNEG1d5, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = red[3], markeredgewidth = '0.25',color=red[0])
    ax2.plot(n16List, lnpna16_VNEG1d5a10+shiftVNEG1d5, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =red[0], markeredgewidth = '0.25',color=red[0])
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #V/t=10 , N=16

    #alpha=2
    ax2.plot(n16List, lnpntoa16_V10a2+shiftV10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = blue[3], markeredgewidth = '0.25',color=blue[0])
    ax2.plot(n16List, lnpna16_V10a2+shiftV10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =blue[0], markeredgewidth = '0.25',color=blue[0])
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=5
    ax2.plot(n16List, lnpntoa16_V10a5+shiftV10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = green[3], markeredgewidth = '0.25',color=green[0])
    ax2.plot(n16List, lnpna16_V10a5+shiftV10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =green[0], markeredgewidth = '0.25',color=green[0])
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    #alpha=10
    ax2.plot(n16List, lnpntoa16_V10a10+shiftV10, 'o', label=r'$\ln{P_{n}^{(\alpha=2)}}$', markersize = 4, markerfacecolor = red[3], markeredgewidth = '0.25',color=red[0])
    ax2.plot(n16List, lnpna16_V10a10+shiftV10, '.', label=r'$\ln{P_{(n,\alpha=2)}}$', markersize = 4, markerfacecolor =red[0], markeredgewidth = '0.25',color=red[0])
    #ax2.plot(n15fit, lnpntoa15fit, color='k',label=r'$\ln{P_{n}^{(\alpha=2)}} (Fit)$')

    ax2.tick_params(axis='both', which='both', right='off', top='off',labelright='off', direction='in')
    ax2.xaxis.set_ticks(np.arange(0, 17, 1))
    ax2.set_xlabel(r'$n$')
    
    # remove vertical gap between subplots
    #plt.subplots_adjust(hspace=0.023)
    plt.subplots_adjust(hspace=0.15)
    
    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.030)

    #Adjust y-limits
    ax1.set_ylim(-1750,1750)
    ax2.set_ylim(-1750,1750)

    #Include annotations denoting the interaction strength V/t
    text_x = 0
    text_yV10 = 1350
    text_yVNEG1d5 = 0 
    text_yVNEG10 = -1200

    #N=15
    ax1.annotate(r'$\frac{V}{t}=10.0$', xy=(8,0.01), xytext=(text_x,text_yV10),fontsize=9)
    ax1.annotate(r'$\frac{V}{t}=-1.5$', xy=(8,0.01), xytext=(text_x, text_yVNEG1d5),fontsize=9)
    ax1.annotate(r'$\frac{V}{t}=-10.0$', xy=(8,0.01), xytext=(text_x,text_yVNEG10),fontsize=9)

    #N=16
    ax2.annotate(r'$\frac{V}{t}=10.0$', xy=(8,0.01), xytext=(text_x,text_yV10),fontsize=9)
    ax2.annotate(r'$\frac{V}{t}=-1.5$', xy=(8,0.01), xytext=(text_x,text_yVNEG1d5),fontsize=9)
    ax2.annotate(r'$\frac{V}{t}=-10.0$', xy=(8,0.01), xytext=(text_x,text_yVNEG10),fontsize=9)

    #Inlude annotations denoting the total particle number N
    ax1.annotate(r'$N=15$', xy=(8,0.01), xytext=(text_x+13.5,text_yV10+65),fontsize=9)
    ax2.annotate(r'$N=16$', xy=(8,0.01), xytext=(text_x+14.35,text_yV10+65),fontsize=9)
    

    #plt.savefig('probabilities_N13N14_VNEG1.5_log.pdf', transparent=False)
    #plt.savefig('probabilities_N13N14_VNEG1.0_log.pdf', transparent=False)   
    #plt.savefig('probabilities_N13N14_V1.0_log.pdf', transparent=False)
    #plt.savefig('probabilities_N13N14_VMax_log.pdf', transparent=False)
    #plt.savefig('probabilities_N15N16_logn.pdf', transparent=False)


    #plt.show()

    fig = plt.figure()
    ax1 = plt.subplot(111)
    ax1.plot(n16List,np.log(pn15_V10),mfc='None',marker='o')
    ax1.plot(n16List,np.log(pna15_V10a2),'*')
    print(np.sum(pn15_V10))
    print(np.sum(pna15_V10a2))
    plt.savefig('testing.pdf')
