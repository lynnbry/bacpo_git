import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib.patches as mpatches

#constants
a=1.0
m=8
d=0.01
q1=0.24
q2=0.25
k1=0.015
s0=1.0


#f(s,e) linear
def g(b,t):
    s=b[0]
    e=b[1]
    x1=b[2]
    x2=b[3]
    #differential equations
    dsdt=d*(s0-s)-((x1+x2)*(a*s*e))
    dedt=q1*x1*(a*s*e)-(d*e)
    dx1dt=x1*((1-q1)*(a*s*e)-d-(k1*(q2/(1-q2))*x2))
    dx2dt=x2*((1-q2)*(a*s*e)-d)
    return [dsdt,dedt,dx1dt,dx2dt]
'''

#f(s,e) Michaellis-menton
def g(b,t):
    s=b[0]
    e=b[1]
    p=b[2]
    x1=b[3]
    x2=b[4]
    x3=b[5]
    #differential equations
    dsdt=d*(s0-s)-(x1+x2+x3)*((m*m*s*e)/((a+s)*(a+e)))
    dedt=q1*x1*((m*m*s*e)/((a+s)*(a+e)))-d*e
    dpdt=q2*x2*((m*m*s*e)/((a+s)*(a+e)))-d*p
    dx1dt=x1*((1-q1)*((m*m*s*e)/((a+s)*(a+e)))-d-kk*p)
    dx2dt=x2*((1-q2)*((m*m*s*e)/((a+s)*(a+e)))-d)
    dx3dt=x3*(((m*m*s*e)/((a+s)*(a+e)))-d-k*p)
    return [dsdt,dedt,dpdt,dx1dt,dx2dt,dx3dt]
'''

t=np.linspace(0,500)
bo=[0.1079,0.205563,0.6423848,0.04]
b=odeint(g,bo,t)

plt.plot(t,b[:,2],'orange',linewidth=1.0)
plt.plot(t,b[:,3],'b',linewidth=1.0)

plt.ylim(bottom=0)
plt.xlim(0,500)

plt.xlabel("time")
line1=mlines.Line2D([],[],color='orange', label = '$x_1$ cooperator')
line2=mlines.Line2D([],[],color='blue', label='$x_2$ police')
kdef=mpatches.Patch(color='white', label='k = %.2f' %k1)
amdef=mpatches.Patch(color='white', label='a= %.2f' %(a))
qsdef=mpatches.Patch(color='white', label=r'$q_1$=%.2f, $q_2$=%.2f' %(q1,q2))
s0def=mpatches.Patch(color='white', label=r'$s^0$=%.2f' %s0)
ddef=mpatches.Patch(color='white', label=r'd=%.2f' %d)
plt.subplots_adjust(right=0.7)
plt.legend(handles=[line1,line2,kdef,amdef,qsdef,s0def,ddef],
           loc=(0.9,0.5))
plt.show()

    
