# bacpo_git
Cyanide production as a policing mechanism to sanction social cheaters in bacterium Pseudomonas aeruginosa

code:
bacpo_calccond.py - given a set of parameters will return whether or not there is a real solution, 
and if so, what the steady state solution is. Use this to find numerical solutions quickly.

bacpo_na.py - full system. will graph timesteps of solution for given initial conditions and paremeters

bacpo_numanal_v2-limitingsysyem.py - uses a reduced system where toxin and enzyme equations are removed
from the system due to linearity. Use for cooperator only model

figures:
plots and the parameter values used to reproduce them. cooresponding figures and 
files share the same filename up to the last underscore. Xtypes_number_sol# and Xtypes_number_params 

products:
AW_fin.ppt - analytical workflows final presentation
bacpoanalysis_allcases_reduction.tex - written mathematical analsis of system