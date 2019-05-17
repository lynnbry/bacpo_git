import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

#constants

a=1.0 #constant for f(s,e)/growth func
m=8 #constant for f(s,e)/growth func
<<<<<<< HEAD
d=0.01 #dilution 
q1=0.24 #amount of nutrient used for producing enzyme
q2=0.25 #amount of nutrient used for producing toxin
kk=0.0 #toxicity rate against cooperators/x1
k=0.015 #toxicity rate against cheaters/x3
=======
d=0.5 #dilution 
q1=0.01 #amount of nutrient used for producing enzyme
q2=0.2 #amount of nutrient used for producing toxin
kk=0.1 #toxicity rate against cooperators/x1
k=1.0 #toxicity rate against cheaters/x3
>>>>>>> ec90ec1b27adb4d1cd0b3b74aa55063f0c89b6e9
s0=1.0 #nutrient concentration


#2 options for type of growth rate function, f(s,e)
<<<<<<< HEAD

=======
'''
>>>>>>> ec90ec1b27adb4d1cd0b3b74aa55063f0c89b6e9
#f(s,e) linear
def g(b,t):
    #set to initial conditions
    s=b[0]
    e=b[1]
    p=b[2]
    x1=b[3]
    x2=b[4]
    x3=b[5]
    #differential equations
    dsdt=d*(s0-s)-(x1+x2+x3)*((a*s*e)) #nutrient
    dedt=q1*x1*(a*s*e)-d*e #enzyme
    dpdt=q2*x2*(a*s*e)-d*p #toxin
    dx1dt=x1*((a*s*e)-d-kk*p) #coop/x1
    dx2dt=x2*((a*s*e)-d) #police/x2
    dx3dt=x3*((a*s*e)-d-k*p) #cheat/x3
    return [dsdt,dedt,dpdt,dx1dt,dx2dt,dx3dt]
'''

#f(s,e) Michaellis-menton
def g(b,t):
    #set to initial conditions
    s=b[0]
    e=b[1]
    p=b[2]
    x1=b[3]
    x2=b[4]
    x3=b[5]
    #differential equations
    dsdt=d*(s0-s)-(x1+x2+x3)*((m*m*s*e)/((a+s)*(a+e))) #nutrient
    dedt=q1*x1*((m*m*s*e)/((a+s)*(a+e)))-d*e #enzyme
    dpdt=q2*x2*((m*m*s*e)/((a+s)*(a+e)))-d*p #toxin
    dx1dt=x1*((1-q1)*((m*m*s*e)/((a+s)*(a+e)))-d-kk*p) #coop/x1
    dx2dt=x2*((1-q2)*((m*m*s*e)/((a+s)*(a+e)))-d) #police/x2
    dx3dt=x3*(((m*m*s*e)/((a+s)*(a+e)))-d-k*p) #cheat/x3
    return [dsdt,dedt,dpdt,dx1dt,dx2dt,dx3dt]
'''

<<<<<<< HEAD
xbig=1000 #timesteps

t=np.linspace(0,xbig) #timestep
bo=[0.5,0.2,0,0.0,0.0,0.3] #initial conditions
=======
t=np.linspace(0,50) #timestep
bo=[0.5,0.5,0,0.5,0,0] #initial conditions
>>>>>>> ec90ec1b27adb4d1cd0b3b74aa55063f0c89b6e9
b=odeint(g,bo,t) #odesolver over timestep

#figure
#ploting 
plt.plot(t,b[:,3],'r',linewidth=1.0) #x1/cooperator in red
plt.plot(t,b[:,0],'purple',linewidth=1.0) #substrate 
plt.plot(t,b[:,1],'green',linewidth=1.0) #enzyme
plt.plot(t,b[:,4],'b',linewidth=1.0) #x2/police in blue
plt.plot(t,b[:,5],'deeppink',linewidth=1.0) #x3/cheater in pink

#set axis lengths and ticks
plt.yticks(np.arange(0,1.1,step=0.25))
plt.ylim(bottom=0)
plt.xlim(0,xbig)
plt.xticks([0,xbig], visible=True)

#axis labels
plt.xlabel("Time")
plt.ylabel("Concentration")

#legend key
line5=mlines.Line2D([],[],color='purple', label='substrate')
line4=mlines.Line2D([],[],color='green', label='enzyme')
'''
line1=mlines.Line2D([],[],color='red', label = '$x_1$ cooperator')
line2=mlines.Line2D([],[],color='blue', label='$x_2$ police')
'''
line3=mlines.Line2D([],[],color='deeppink', label='$x_3$ cheater')

#constants key
kkdef=mpatches.Patch(color='white', label=r'$\tilde{k}$ = %.2f' %kk)
kdef=mpatches.Patch(color='white', label='k = %.2f' %k)
amdef=mpatches.Patch(color='white', label='a= %.2f, m=%.2f' %(a, m))
qsdef=mpatches.Patch(color='white', label=r'$q_1$=%.2f, $q_2$=%.2f' %(q1,q2))
s0def=mpatches.Patch(color='white', label=r'$s^0$=%.2f' %s0)
ddef=mpatches.Patch(color='white', label=r'd=%.2f' %d)
plt.subplots_adjust(right=0.7) #legend location

#legend compact
plt.legend(handles=[line3,line4,line5],
           loc=(1.05,0.5))

#leg w constants
'''
plt.legend(handles=[line1,line2,line3,kkdef,kdef,amdef,qsdef,s0def,ddef],
           loc=(1.05,0.5))
'''

plt.show()

#print consts for records
print 'a:', a, 'm:', m, 'k1:', k, 'k3:', kk, 's0:', s0, 'd:', d, 'q1:', q1, 'q2:', q2     
