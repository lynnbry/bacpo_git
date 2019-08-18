import numpy as np
from numpy import linalg as LA

#initial condtions
d=0.119
s=0.553
e=0.00574
x1=0.0179
x2=0.317
#constants
a=50.0
q1=0.24
q2=0.25
k1=0.015
f=a*s*e #growth func
ds=a*e #dfds
de=a*s #dfde

#jacobian for x1x2 steady state
J=[[-d-((x1+x2)*ds), -(x1+x2)*de,  -f, -f],
   [q1*x1*ds,(q1*x1*de)-d, q1*f, 0],
   [x1*(1-q1)*ds, x1*(1-q1)*de, 0, -k1*(q2/(1-q2))*x1],
   [x2*(1-q2)*ds, x2*(1-q2)*de, 0,0]]

w,v=LA.eig(J)

print 'd: ',d
print w

   
