
import numpy as np
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

#constants

a=1.0 #constant for f(s,e)/growth func
m=8.0 #constant for f(s,e)/growth func (non-linear)
d=0.01 #dilution 
q1=0.24 #amount of nutrient used for producing enzyme
q2=0.25 #amount of nutrient used for producing toxin
kk=0.015 #toxicity rate against cooperators/x1
k=0.3 #toxicity rate against cheaters/x3
s0=1.0 #nutrient concentration


#######2 options for type of growth rate function, f(s,e)######

####f(s,e) linear
def g(b,t):
    #set to initial conditions
    s=b[0]
    e=b[1]
    p=b[2]
    x1=b[3]
    x2=b[4]
    x3=b[5]
    #differential equations
    dsdt=(d*(s0-s))-((x1+x2+x3)*(a*s*e)) #nutrient
    dedt=(q1*x1*(a*s*e))-d*e #enzyme
    dpdt=(q2*x2*(a*s*e))-d*p #toxin
    dx1dt=x1*((1-q1)*(a*s*e)-d-kk*p) #coop/x1
    dx2dt=x2*((1-q2)*(a*s*e)-d) #police/x2
    dx3dt=x3*((a*s*e)-d-k*p) #cheat/x3
    return [dsdt,dedt,dpdt,dx1dt,dx2dt,dx3dt]
'''

###f(s,e) Michaellis-menton
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

xbig=9000 #timesteps
s0_0=0.1
e_0=0.21
t_0=0
x1_0=0.6
x2_0=0.02
x3_0=0.03

t=np.linspace(0,xbig) #timestep
bo=[s0_0,e_0,t_0,x1_0,x2_0,x3_0] #initial conditions
b=odeint(g,bo,t) #odesolver over timestep


######figure, 3d projection######

###patch start to remove margins###
from mpl_toolkits.mplot3d.axis3d import Axis
if not hasattr(Axis, "_get_coord_info_old"):
    def _get_coord_info_new(self, renderer):
        mins, maxs, centers, deltas, tc, highs = self._get_coord_info_old(renderer)
        mins += deltas / 4
        maxs -= deltas / 4
        return mins, maxs, centers, deltas, tc, highs
    Axis._get_coord_info_old = Axis._get_coord_info  
    Axis._get_coord_info = _get_coord_info_new
###patch end###

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
ax.plot(b[:,3],b[:,4],b[:,5]) #x coop, y police, z cheat
ax.plot([x1_0],[x2_0],[x3_0],marker='o',markersize=3,color='r') #initial condition

ax.view_init(azim=45) #angle of cube

init_dot=mlines.Line2D([],[],color='r',marker='o',linestyle='none',label='initial condition')
ax.legend(handles=[init_dot])

#set axis and labels
ax.xaxis.set_rotate_label(False)
ax.set_xlabel(r'$x_1$')
ax.set_xlim(0,1)
ax.yaxis.set_rotate_label(False)
ax.set_ylabel(r'$x_2$')
ax.set_ylim(0,1)
ax.zaxis.set_rotate_label(False)
ax.set_zlabel(r'$x_3$')

'''
ax.set_zticks(np.arange(0,x3_0+0.01,step=0.01))
'''
######end 3d fig######
'''
######2d for pairs######
plt.plot(b[:,3],b[:,5],linewidth=2.0) #
plt.plot(x1_0,x3_0,marker='o',markersize=3,color='r') #initial condition

plt.xlim(0,1)
plt.ylim(0,1)

plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_3$',rotation=0)

#legendkey
init_dot=mlines.Line2D([],[],color='r',marker='o',linestyle='none',label='initial condition')
plt.legend(handles=[init_dot],loc=(0.6,0.85))
######end 2d for pairs######


#######figure, timeseries######

#ploting 
plt.plot(t,b[:,3],'r',linewidth=3.0) #x1/cooperator in red
plt.plot(t,b[:,0],'purple',linewidth=2.0,linestyle='dashdot') #substrate 
plt.plot(t,b[:,1],'green',linewidth=2.0,linestyle='dashed') #enzyme

plt.plot(t,b[:,4],'b',linewidth=2.5) #x2/police in blue
plt.plot(t,b[:,2],'darkorange',linewidth=2.0,linestyle=':') #toxin in orange

plt.plot(t,b[:,5],'deeppink',linewidth=2.0) #x3/cheater in pink

#set axis lengths and ticks
plt.yticks(np.arange(0,1.1,step=0.25))
plt.ylim(bottom=0)
plt.xlim(0,xbig)
plt.xticks(np.arange(0,xbig+1, step=(xbig/5)), visible=True)

#axis labels
plt.xlabel("Time")
plt.ylabel("Concentration")

#legend key
line5=mlines.Line2D([],[],color='purple', label='substrate', linewidth=2.0,linestyle='dashdot')
line4=mlines.Line2D([],[],color='green', label='enzyme',linewidth=2.0,linestyle='dashed')

line1=mlines.Line2D([],[],color='red', label = '$x_1$ cooperator',linewidth=3.0)

line2=mlines.Line2D([],[],color='blue', label='$x_2$ toxin producer',linewidth=2.5)
line6=mlines.Line2D([],[],color='darkorange',label='toxin',linewidth=2.0,linestyle=':')

line3=mlines.Line2D([],[],color='deeppink', label='$x_3$ cheater',linewidth=2.0)

#constants key
kkdef=mpatches.Patch(color='white', label=r'$\tilde{k}$ = %.2f' %kk)
kdef=mpatches.Patch(color='white', label='k = %.2f' %k)
amdef=mpatches.Patch(color='white', label='a= %.2f, m=%.2f' %(a, m))
qsdef=mpatches.Patch(color='white', label=r'$q_1$=%.2f, $q_2$=%.2f' %(q1,q2))
s0def=mpatches.Patch(color='white', label=r'$s^0$=%.2f' %s0)
ddef=mpatches.Patch(color='white', label=r'd=%.2f' %d)
plt.subplots_adjust(right=0.7) #legend location

#legend
plt.legend(handles=[line1,line2,line3,line4,line5,line6],
           loc=(1.05,0.5))
           
######end, fig timeseries######
'''

plt.show()

#print consts for records
print 'a:', a, 'm:', m, 'k1:', k, 'k3:', kk, 's0:', s0, 'd:', d, 'q1:', q1, 'q2:', q2     
print bo
print 'timesteps',xbig
