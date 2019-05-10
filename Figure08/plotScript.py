import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

from scipy.optimize import fsolve
from scipy.interpolate import UnivariateSpline

from collections import defaultdict
try: plt.style.use('notebook')
except: pass
#%matplotlib inline
π = np.pi
from matplotlib import gridspec

colors = ['#5e4ea2','#3d94b8','#7bc9a5']
fcolors = ['#aea7d0','#9ec9db','#bce3d2']
markers = ['o','s','^']


from math import e
from scipy import stats
import colors

def Θ(k1,k2,Δ):
    return 2.0*np.arctan(Δ*np.sin(0.5*(k1-k2))/(Δ*np.cos(0.5*(k1-k2))+np.cos(0.5*(k1+k2))))

def _I(n):
    return np.array([i+1-0.5*(n+1) for i in range(n)])

def equations(k,L,Δ,n,I,Φ):
    eqs = np.zeros(len(k))
    for i in range(n):
        eqs[i] = L*k[i] - 2.0*π*I[i] - Φ - np.sum(Θ(k[i],k,Δ))
    return eqs

def E0(k,L,Δ):
    energy=0
    return 0.5*Δ*L - 2*np.sum(np.cos(k)+Δ)

#%%time

n = 14
L = 28
Δ = 0.0
I = _I(n)

Evals = []
for cn in [n-2,n,n+2]:
    I = _I(cn)
    var_guess = np.linspace(-π,π,cn)

    sol,info,success,mesg = fsolve(equations,var_guess,args=(L,Δ,cn,I,0),full_output=True)
    Evals.append(E0(sol,L,Δ))

invκ = L*(Evals[-1] + Evals[0] - 2*Evals[1])/4

uoK = invκ/(π)
print(uoK)

Φ = np.linspace(-0.1,0.1,10)

EΦvals = []
for cΦ in Φ:
    I = _I(n)
    var_guess = np.linspace(-π,π,n)

    sol,info,success,mesg = fsolve(equations,var_guess,args=(L,Δ,n,I,cΦ),full_output=True)
    EΦvals.append(E0(sol,L,Δ))

fEΦ = UnivariateSpline(Φ,EΦvals,s=0,k=4)
y_spl_2d = fEΦ.derivative(n=2)
uK = L*π*y_spl_2d(0.0)

n = [14]
L = 28
Δ = np.linspace(-0.74,0.75,101)
#Δ = np.linspace(-0.5,0.5,11)

#Kvsn=[range(len(n)),range(len(Δ))]
Kvsn=np.zeros([len(n),len(Δ)])
for i,ni in enumerate(n):
    I = _I(ni)
    Φ = np.linspace(-0.1,0.1,10)
    var_guess = np.linspace(-π,π,ni)
    Kvals = []
    uoKvals = []
    uKvals = []
    E=[]
    Ep=[]
    Em=[]

    #Δ = np.linspace(-0.74,0.75,101)
    #Δ = np.linspace(-0.2,0.2,41)

    for j,cΔ in enumerate(Δ):
        Evals = []
        for cn in [ni-2,ni,ni+2]:
            I = _I(cn)
            var_guess0 = np.linspace(-π,π,cn)

            sol,info,success,mesg = fsolve(equations,var_guess0,args=(L,cΔ,cn,I,0),full_output=True)
            Evals.append(E0(sol,L,cΔ))
            #if (cn==n+2):
                #print(np.sum(np.cos(sol)))
        #if ni==int(L/2):
        #    invκ = abs(L*(Evals[0] - Evals[1])/2)
        #else:
        invκ = abs(L*(Evals[-1] + Evals[0] - 2*Evals[1])/4)

        uoK = invκ/(π)
        E.append(Evals[1])
        Ep.append(Evals[-1])
        Em.append(Evals[0])

        #Φ = np.linspace(-0.1,0.1,10)
        var_guess = np.linspace(-π,π,ni)
        EΦvals = []
        for cΦ in Φ:
            I = _I(ni)
            sol,info,success,mesg = fsolve(equations,var_guess,args=(L,cΔ,ni,I,cΦ),full_output=True)
            EΦvals.append(E0(sol,L,cΔ))
            #var_guess=sol
        fEΦ = UnivariateSpline(Φ,EΦvals,s=0,k=4)
        y_spl_2d = fEΦ.derivative(n=2)
        uK = L*π*y_spl_2d(0.0)
        uoKvals.append(uoK)
        uKvals.append(uK)
        Kvals.append(np.sqrt(uK/uoK))
        #print(Kvals)
    for k in range(len(Kvals)):
        Kvsn[i,k]=Kvals[k]

ccΔ = np.linspace(-0.75,0.75,100)
ccK = π/(2.0*np.arccos(-ccΔ))

#n = [14
L = 28
#Δ = [-0.75,-0.5,-0.2,0.0,0.2,0.5,0.74]
Δ = [-0.75]
n_init=2
KvsV=np.zeros([len(range(n_init,int(L/2)+1)),len(Δ)])
for j,cΔ in enumerate(Δ):
    Φ = np.linspace(-0.1,0.1,1000)
#    Φ = np.linspace(-0.01,0.01,1000) # for n=14

    Kvals = []
    E=[]
    Ep=[]
    Em=[]
    n=range(n_init,int(L/2)+1)
    f=np.zeros(len(n))
    for i in range(len(n)):
        f[i]=n[i]/L
    for ni in range(n_init,int(L/2)):
        #print(ni)
        I = _I(ni)
        Evals = []
        for cn in [ni-2,ni,ni+2]:
            cni=cn
            if (cn>int(L/2)):
                cni=2*int(L/2)-cn

            I = _I(cni)
            var_guess = np.linspace(-π,π,cni)
            sol,info,success,mesg = fsolve(equations,var_guess,args=(L,cΔ,cni,I,0),full_output=True)
            Evals.append(E0(sol,L,cΔ))

        invκ = np.abs(L*(Evals[-1] + Evals[0] - 2*Evals[1])/4)
        E.append(Evals[1])
        Ep.append(Evals[-1])
        Em.append(Evals[0])
        uoK = invκ/(π)

        #Φ = np.linspace(-0.1,0.1,10)
        var_guess = np.linspace(-π,π,ni)
        EΦvals = []
        for cΦ in Φ:
            I = _I(ni)
            sol,info,success,mesg = fsolve(equations,var_guess,args=(L,cΔ,ni,I,cΦ),full_output=True)
            EΦvals.append(E0(sol,L,cΔ))
            var_guess=sol
        fEΦ = UnivariateSpline(Φ,EΦvals,s=0,k=4)
        y_spl_2d = fEΦ.derivative(n=2)
        uK = np.abs(L*π*y_spl_2d(0.0))
        Kvals.append(np.sqrt(uK/uoK))
    #Kvals.append(π/(2.0*np.arccos(-cΔ)))
    Kvals.append(2.17633069)
    for k in range(len(Kvals)):
        KvsV[k,j]=Kvals[k]

fig = plt.figure()
ax1= fig.add_subplot(111)
ax2= fig.add_subplot(111)

Test=KvsV
ax1.plot(f[:],KvsV[:,0],'o',label=r'V/t=-1.5',zorder=1,ms=8.0,markerfacecolor='#ffffff',markeredgewidth = '1.5',color='#5e4ea2')
ax1.plot(f[-1],Test[-1,0],'*',label=r'Th',zorder=1,ms=8.0,markerfacecolor='#7bc9a5',markeredgewidth = '0.95',color='#7bc9a5')

ax1.legend(loc=(0.5,0.5),title=r'$L=28,N=14$',frameon=False,handlelength=.5, numpoints=1,ncol=3)
ax1.set_xlabel(r'$f=N/L$')
ax1.set_ylabel(r'$K$')

plt.savefig('Kvsf_V_-1.5.pdf', transparent=False)

# K=2.17633069 for V=-1.5, L=28 and N=14
# Th K= 2.1734079041462837

#NOTE: IOP_large.mplstyle2 being used instead of IOP_large.mplstyle.
#This script technically generates two figures and combines them vertically into a single figure.


orange = ["#ff8c00"]
blue = ["#4173b3"]

alpha = [1.0,0.6,0.2]
for i,c in enumerate(alpha):
        orange.append(colors.get_alpha_hex(orange[0],alpha[i]))
        blue.append(colors.get_alpha_hex(blue[0],alpha[i]))

with plt.style.context('../IOP_large.mplstyle'):

    #Load filling fractions
    fillingFractions = np.linspace(1,14,14)/28#[i/28 for i in range(1,15)]

    #Save Entanglement Entropies (s1=VonNeumann, s2=Renyi) to variables

    sigma2VNEG1d5M28l14= np.loadtxt("../Data/Frac_28_14_-1.5.dat")[:,6]
    sigma2VNEG1d5M28lN= np.loadtxt("../Data/Frac_28_N_-1.5.dat")[:,6]

    s1VNEG1d5M28l14 = np.loadtxt("../Data/Frac_28_14_-1.5.dat")[:,2]
    s1opVNEG1d5M28l14 = np.loadtxt("../Data/Frac_28_14_-1.5.dat")[:,3]
    s1VNEG1d5M28lN = np.loadtxt("../Data/Frac_28_N_-1.5.dat")[:,2]
    s1opVNEG1d5M28lN = np.loadtxt("../Data/Frac_28_N_-1.5.dat")[:,3]

    s2VNEG1d5M28l14 = np.loadtxt("../Data/Frac_28_14_-1.5.dat")[:,4]
    s2opVNEG1d5M28l14 = np.loadtxt("../Data/Frac_28_14_-1.5.dat")[:,5]
    s2VNEG1d5M28lN = np.loadtxt("../Data/Frac_28_N_-1.5.dat")[:,4]
    s2opVNEG1d5M28lN = np.loadtxt("../Data/Frac_28_N_-1.5.dat")[:,5]

    fillingFractions = np.linspace(1,14,14)/28#[i/28 for i in range(1,15)]
    f=fillingFractions
    L=28
    N=L*f
    X=L/np.pi*np.sin(f*np.pi)
    #Create the figure

    #Set height ratios for subplots
    #fig, axes = plt.subplots(1,2,sharex=True, sharey=True, squeeze=True, figsize=(12,3.71))
    #fig.subplots_adjust(wspace=0.025)

    #Create the figure
    #fig = plt.figure(figsize=(3.403,2.104))
    fig = plt.figure()
    #Set height ratios for subplots
    gs = gridspec.GridSpec(1, 2, width_ratios=[3.403,3.403],height_ratios=[2.104])

    #Negative energies subplot
    ax3 = plt.subplot(gs[0])

    yy=np.pi*1.0
    y=(X[1:]*X[-1]/L*yy)**2+1

    ax3.plot(KvsV[:,0]/np.pi**2/2*np.log(y), np.exp((s1VNEG1d5M28l14[1:]-s1opVNEG1d5M28l14[1:]-1/2-np.log(2*np.pi)/2.0)*2.0), '.', label=r'$\alpha=1$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',markersize=9,markerfacecolor = blue[3],zorder=10)
    ax3.plot(KvsV[:,0]/np.pi**2/2*np.log(y), np.exp((s2VNEG1d5M28l14[1:]-s2opVNEG1d5M28l14[1:]-np.log(4*np.pi)/2.0)*2.0), '.', label=r'$\alpha=2$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',markersize=6,mfc= orange[3],zorder=10)
    ax3.plot(KvsV[:,0]/np.pi**2/2*np.log(y), sigma2VNEG1d5M28l14[1:], '.', label=r'$ \sigma^2$', linewidth = 1, color='#000000',markeredgewidth='0.5',markersize='4',mfc= '#000000',zorder=10)
    ax3.tick_params(axis='both', which='both', left='on', right='off', top='off', bottom='on', labelleft='on', direction = 'in',labelbottom='on')
    ax3.xaxis.set_ticks([0.1,0.2,0.3,0.4])
    ax3.yaxis.set_ticks([0.4,0.5,0.6,0.7])

    ax3.set_xlabel(r'$\mathcal{F}[X(N),X(\ell=L/2)]$')
    y=(X[1:]*X[1:]/L*yy)**2+1
    #y=(X[1:]*X[1:]/L)**2+1

    ax4 = plt.subplot(gs[1])

    ax4.plot(KvsV[:,0]/np.pi**2/2*np.log(y), np.exp((s1VNEG1d5M28lN[1:]-s1opVNEG1d5M28lN[1:] -0.5-np.log(2*np.pi)/2.0)*2.0) , '.', label=r'$\mathcal{B}_{1}{\rm{e}}^{2\Delta S_{1}}$', linewidth = 1, color='#4173b3',markeredgewidth='0.5',markersize=9,mfc= blue[3],zorder=10)
    ax4.plot(KvsV[:,0]/np.pi**2/2*np.log(y), np.exp((s2VNEG1d5M28lN[1:]-s2opVNEG1d5M28lN[1:]-np.log(4*np.pi)/2)*2), '.', label=r'$\mathcal{B}_{2}{\rm{e}}^{2\Delta S_{2}}$', linewidth = 1, color='#ff8c00',markeredgewidth='0.5',markersize=6,mfc= orange[3],zorder=10)
    ax4.plot(KvsV[:,0]/np.pi**2/2*np.log(y), sigma2VNEG1d5M28lN[1:], '.', label=r'$ \sigma^2$', linewidth = 1, color='#000000',markeredgewidth='0.5',markersize=4,mfc= '#000000',zorder=10)
    ax4.tick_params(axis='both', which='both', left='off', right='on', top='off', bottom='on', labelleft='off', labelright='on', direction = 'in',labelbottom='on')
    ax4.xaxis.set_ticks([ 0.0,0.1,0.2,0.3,0.4])
    ax4.yaxis.set_ticks([ 0.1,0.2,0.3,0.4,0.5,0.6,0.7])
    ax4.set_xlabel(r'$\mathcal{F}[X(N),X(\ell=N)]$')
    #Annotations for the interaction strength and type of partition
    x1,y1 = 0.215,0.875
    x2,y2 = 0.5,0.5
    #fs = 9
    ax3.annotate(r'$V/t=-1.5$',
            xy=(x1-0.1, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points'#, fontsize = fs
            )
    ax3.annotate(r'$\ell = L/2$',
            xy=(x1-0.1, y1-0.1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points'#, fontsize = fs
            )

    ax4.annotate(r'$V/t=-1.5$',
            xy=(x1-.08, y1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points'#, fontsize = fs
            )
    ax4.annotate(r'$\ell = N$',
            xy=(x1-.08, y1-0.1), xycoords='axes fraction',
            xytext=(x2, y2), textcoords='offset points'#, fontsize = fs
            )

    lgnd = plt.legend(loc=(0.40,.08),frameon=False,handlelength=1,ncol=1)

    # remove vertical gap between subplots
    plt.subplots_adjust(hspace=0.050)
    plt.subplots_adjust(left=0.08)
    plt.subplots_adjust(right=0.92)

    plt.subplots_adjust(top=0.99)
    plt.subplots_adjust(bottom=0.18)
    #Adjust space between subplots
    plt.subplots_adjust(wspace = 0.040)


plt.savefig('fillingFractionDependence.pdf', transparent=False)
