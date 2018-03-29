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
    data = np.loadtxt('peakScalingOddN.dat') 
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

    print('ln(c1) = %.8f'%(lnc1))
    print('c1 = %.8f'%(c1))
    print('c2 = %.8f'%(c2))
    print('c3 = %.8f'%(c3))


    Vmaxfit = c1*(Nfit)**(-c2)+c3  #Exponential form of the fit
    #Create the figure
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    #ax1.plot(N,Vmax-c3,'o',mfc='w',label='Data')
    #ax1.plot(Nfit,Vmaxfit-c3,'-',label=r'$%.4f N^{-%.4f}+%.4f$'%(c1,c2,c3))
    ax1.plot(N**(-c2),Vmax,'o',mfc=blue[3],label='Data',color=blue[1])
    ax1.plot(Nfit**(-c2),Vmaxfit,'-',label=r'$%.4f N^{-%.4f}+%.4f$'%(c1,c2,c3),color=orange[1])
    #ax1.set_ylim(2,5)
    ax1.set_xlim(0,1)
    #ax1.set_xlim(3,15)
    #ax1.set_ylim(0,8)
    ax1.set_xlabel(r'$N^{%.4f}$'%(-c2))
    ax1.set_ylabel(r'$(\frac{V}{t})_{Max}$')
    ax1.legend(fontsize='small')
    plt.savefig('peakFitOddN_wLegend.pdf')
    plt.show()

    #plt.clf()
    #fig = plt.figure()
    #ax2 = fig.add_subplot(111)
    #ax2.plot(c3List,chisquareList,'o')
    #ax2.set_xlabel(r'$C_3$')
    #ax2.set_ylabel(r'$|\chi^{2}|$')
    #ax2.set_xlim(1.0,2.15)
    #ax2.set_ylim(0,0.025)

    #plt.savefig('ChiSquaredVsC3_VNEG1.85.pdf')
    #plt.savefig('ChiSquaredVsC3_V0.pdf')
    #plt.savefig('ChiSquaredVsC3_VPOS1.85.pdf')


    plt.show()




