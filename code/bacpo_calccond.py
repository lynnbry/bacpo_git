import math



#constants
a=1.0
m=8.0
d=0.01
q1=0.24
q2=0.25
k1=0.015
s0=1.0


#calculate constant c
def calc_constant(q1,q2,d,k1):
    numerator=(q2-q1)*d
    denominator=q2*(1-q2)*k1
    constant=float(numerator/denominator)
    return constant

#define f(s,e), growth func
def f(s,e):
    growthfunc=a*s*e #linear growth func
    return growthfunc

#det s compatibility s^2*q1-q1*(s0-c)+(da/(1-q2))=0
def rad_s(a,q1,q2,c,d,s0):
    bee=float(q1*(c-s0)) #b in quadratic formula as^2+bs+c=0
    cee=float((d*a)/(1-q2)) #c in quadratic formula
    radicand= float(bee*bee - (4*a*cee)) #needs to be pos for real solutions
    return radicand

def solve_s(a,q1,q2,d,k1,s0,c,radicand):
    bee=float(q1*(c-s0))
    sol1= ((-bee)+(math.sqrt(radicand)))/(2*a)
    sol2= ((-bee)-(math.sqrt(radicand)))/(2*a)
    print "sol1: "
    steady_states(q1,q2,d,k1,s0,c,sol1)
    print "sol2: "
    steady_states(q1,q2,d,k1,s0,c,sol2)

#use these params to calculate steady states
def steady_states(q1,q2,d,k1,s0,c,s):
    x2_stst=((q2-q1)*d)/(q2*k1)
    e_stst=(q1*(s0-s-c))
    x1_stst= (e_stst*(1-q2))/q1
    print "s: ", s, "e: ", e_stst, "x1: ", x1_stst, "x2: ",x2_stst
            
    

c=calc_constant(q1,q2,d,k1)
rad=rad_s(a,q1,q2,c,d,s0)

print "c : ", c
print "radicand : ", rad


solve_s(a,q1,q2,d,k1,s0,c,rad)

print "constants: "
print "a: ", a, "m: ", m, "d: ", d, "q1: ", q1, "q2: ", q2, "k1: ", k1, "s0: ", s0

