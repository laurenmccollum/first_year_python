#determining the maximum stepsize permissible for the Euler, Euler-Cromer and Runge-Kutta methods in the simulation of a simple harmonic oscillator

import math
import numpy as np

#student number 40260823

#assigning values
k = 9 #spring constant
m = 123 #mass
A = 0.1 #displacement
v = 0 #velocity
tmax = (10*2*math.pi)/math.sqrt(k/m) #time taken for 10 oscillations

dthigh = 10
dtlow = 1e-9

for i in range(30):
  dt = 0.5*(dthigh+dtlow) #calculate new dt each iteration using bisection
  flag = 0

  #assigning starting values for each method
  xeu = xec = xrk = A 
  veu = vec = vrk = v

  for t in np.arange(dt,tmax,dt): #calculating each method at each time step until max time
    #analytical
    xan = A*math.cos(math.sqrt(k/m)*t)
    van = -A*math.sqrt(k/m)*math.sin(math.sqrt(k/m)*t)

    #euler
    xeuold = xeu
    xeu = xeu + dt*veu
    veu = veu + dt*(-k/m)*xeuold
      
    #euler_cromer
    xec = xec + dt*vec
    vec = vec + dt*(-(k/m)*xec)

   #runge_kutta
    xa = vrk
    va = -(k/m)*xrk
    xb = vrk + ((dt/2) * va)
    vb = -(k/m) * (xrk+((dt/2)*xa))
    xc = vrk + ((dt/2) * vb)
    vc = -(k/m) * (xrk + ((dt/2)*xb))
    xd = vrk + (dt*vc)
    vd = -(k/m) * (xrk + (dt*xc))
    xrk = xrk + ((dt/6)*(xa+(2*xb)+(2*xc)+xd))
    vrk = vrk + ((dt/6)*(va+(2*vb)+(2*vc)+vd))

    #dt test for runge-kutta method
    if abs(xan-xrk)/A>0.01 or abs(van-vrk)/(A*math.sqrt(k/m))>0.01:
      flag = 1
      break

  if flag == 1: #if >0.01 then dt becomes higher limit
    dthigh = dt 
  else: #if <0.01 then dt becomes lower limit
    dtlow = dt 

  print("High:", dthigh, "Low:", dtlow, "Test:", dt)

#eu = 0.00117090630681822
#ec =  0.0741285933794289
#rk = 1.3853913833619904
