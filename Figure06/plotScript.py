#Find scaling of interaction strength (V/t) where operational
#entanglement peak occurs for tV Model Chains with odd N

import numpy as np
import matplotlib.pyplot as plt
from math import e
from scipy.stats import chisquare
from scipy import stats
import colors

with plt.style.context('../IOP_large.mplstyle'):

    #Load Adrian's APS Colors
    red = ["#e85c47"]
    blue = ["#4173b3"]
    green = ["#7dcca4"]     #Actually orange
    orange = ["#fdbe6e"]    #Actually green

    beta = [0.8,0.5,0.1]

    for i,c in enumerate(beta):
            red.append(colors.get_alpha_hex(red[0],beta[i]))
            orange.append(colors.get_alpha_hex(orange[0],beta[i]))
            green.append(colors.get_alpha_hex(green[0],beta[i]))
            blue.append(colors.get_alpha_hex(blue[0],beta[i]))

    #Load data
    data = np.loadtxt('Data/peakScalingOddN.dat') 
    N = data[:,0]
    Vmax = data[:,1]

    c3List = np.linspace(1.85,2.2,100000) #Equally spaced values around the peak we want to determine
    c2List = np.zeros(np.size(c3List))
    c1List = np.zeros(np.size(c3List))
    chisquareList = np.zeros(np.size(c3List))

    #Nfit = np.linspace(1,15,1000)
    Nfit = np.linspace(1,100000000000000000,1000)

    ###########
    '''
    for i,c in enumerate(c3List):

        #Fit data to linearized N power law and extract coefficients
        #Vmax = c1N^(-c2) + c #Canonical Scaling Form

        coeffs = np.polyfit(np.log(N),np.log(Vmax-c),deg=1)

        c2 = -coeffs[0]        #c2, linear coefficient
        c1 = e**(coeffs[1])    #c1, constant coefficient
        lnc1 = coeffs[1]

        #Save the fitting parameters obtained for each c.
        c2List[i] = c2
        c1List[i] = c1

    #Test goodness of fit using chi-square value
        #Y = np.log(Vmax-c)         #Data
        #y = lnc1 - c2*np.log(N)    #Fit
        #chisq = np.sum((Y-y)**2)

    #Test goodness of (linear form of) the fit using Pearson's Chi-Square Test
        chisq = chisquare(np.log(Vmax-c),lnc1 - c2*np.log(N))[0]


    chisq = chisquare(np.log(Vmax-c),f_exp=lnc1-c2*np.log(N))[1]

        chisquareList[i]=(chisq)


    minIndex = np.argmin((chisquareList))
    c3 = c3List[minIndex]
    c2 = c2List[minIndex]
    c1 = c1List[minIndex]

    print('chi square = %.8e'%(chisquareList[minIndex]))
    print('ln(c1) = %.8f'%(lnc1))
    print('c1 = %.8f'%(c1))
    print('c2 = %.8f'%(c2))
    print('c3 = %.8f'%(c3))
    '''
    ######

    #Do fit for forced value of c3=2 of canonical scaling form
    c3 = 2

    coeffs = np.polyfit(np.log(N),np.log(Vmax-c3),deg=1)

    c2 = -coeffs[0]
    lnc1 = coeffs[1]
    c1  = e**lnc1

    Vmaxfit = c1*(Nfit)**(-c2)+c3  #Exponential form of the fit
    #Create the figure
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(N[0]**(-c2),Vmax[0],'>',mfc=blue[3],label='3',color=blue[1],zorder=1)
    ax1.plot(N[1]**(-c2),Vmax[1],'<',mfc=blue[3],label='5',color=blue[1],zorder=1)
    ax1.plot(N[2]**(-c2),Vmax[2],'p',mfc=blue[3],label='7',color=blue[1],zorder=1)
    ax1.plot(N[3]**(-c2),Vmax[3],'d',mfc=blue[3],label='9',color=blue[1],zorder=1)
    ax1.plot(N[4]**(-c2),Vmax[4],'^',mfc=blue[3],label='11',color=blue[1],zorder=1)
    ax1.plot(N[5]**(-c2),Vmax[5],'s',mfc=blue[3],label='13',color=blue[1],zorder=1)
    ax1.plot(N[6]**(-c2),Vmax[6],'o',mfc=blue[3],label='15',color=blue[1],zorder=1) 
    
    #Set legend
    ax1.legend(loc=(0.67,0.05),fontsize=10,frameon=False,handlelength=1,handleheight=1,title=r'$N$',ncol=2)
    
    ax1.plot(Nfit**(-c2),Vmaxfit,'-',label=r'$%.4f N^{-%.4f}+%.4f$'%(c1,c2,c3),color=blue[1],zorder=0,linewidth=0.75)
    ax1.set_xlim(0,0.80)
    ax1.set_xlabel(r'$N^{%.4f}$'%(-c2))
    ax1.set_ylabel(r'$V/t \vert_{\mathrm{Max}}$')
    ax1.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
   
    #Inset Plot
    dataN3 = np.loadtxt("Data/InsetData/EOPP6F3l3a2.dat")
    dataN5 = np.loadtxt("Data/InsetData/EOPP10F5l5a2.dat")
    dataN7 = np.loadtxt("Data/InsetData/EOPP14F7l7a2.dat")
    dataN9 = np.loadtxt("Data/InsetData/EOPP18F9l9a2.dat")
    dataN11 = np.loadtxt("Data/InsetData/EOPP22F11l11a2.dat")
    dataN13 = np.loadtxt("Data/InsetData/EOPP26F13l13a2.dat")
    dataN15 = np.loadtxt("Data/InsetData/EOPP30F15l15a2.dat")
    
    xN3, yN3 = dataN3[:,0], dataN3[:,3]
    xN5, yN5 = dataN5[:,0], dataN5[:,3]
    xN7, yN7 = dataN7[:,0], dataN7[:,3]
    xN9, yN9 = dataN9[:,0], dataN9[:,3]
    xN11, yN11 = dataN11[:,0], dataN11[:,3]
    xN13, yN13 = dataN13[:,0], dataN13[:,3]
    xN15, yN15 = dataN15[:,0], dataN15[:,3]
    
    left,bottom,width,height = [0.217,0.507,0.36,0.36]
    ax2 = fig.add_axes([left,bottom,width,height])
    ax2.plot(xN3,yN3,label='5',color=blue[1],linewidth=0.75)
    ax2.plot(xN5,yN5,label='5',color=blue[1],linewidth=0.75)
    ax2.plot(xN7,yN7,label='7',color=blue[1],linewidth=0.75)
    ax2.plot(xN9,yN9,label='9',color=blue[1],linewidth=0.75)
    ax2.plot(xN11,yN11,label='11',color=blue[1],linewidth=0.75)
    ax2.plot(xN13,yN13,label='13',color=blue[1],linewidth=0.75)
    ax2.plot(xN15,yN15,label='15',color=blue[1],linewidth=0.75)
    
    #Add marker at the peaks
    ax2.plot(2.7928168485370364,0.6689827690493597,marker='o',mfc=blue[3],color=blue[1],label='15')
    ax2.plot(2.8258612507925038,0.6305148711748493,marker='s',mfc=blue[3],color=blue[1],label='13')
    ax2.plot(2.8721517043926008,0.5856038496253868,marker='^',mfc=blue[3],color=blue[1],label='11')
    ax2.plot(2.9211898989895535,0.5315254430302333,marker='d',mfc=blue[3],color=blue[1],label='9')
    ax2.plot(2.9842038317092805,0.4634960193349440,marker='p',mfc=blue[3],color=blue[1],label='7')
    ax2.plot(3.0716932401905814,0.3720450303814098,marker='<',mfc=blue[3],color=blue[1],label='5')
    ax2.plot(3.1903119454707949,0.2335959173839680,marker='>',mfc=blue[3],color=blue[1],label='3')
    ax2.axvline(x=2,color='#cccccc',zorder=-1)
    ax2.set_xlabel(r'$V/t$')
    ax2.set_ylabel(r'$S_{1}^{\mathrm{op}}$')
    ax2.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in')
    ax2.set_aspect(1.618033*4)
    ax2.set_xlim(0.64281684853,5.34031194547)
    ax2.xaxis.labelpad = -2
    ax2.yaxis.labelpad = 2


    plt.savefig('peakFitOddN.pdf')
