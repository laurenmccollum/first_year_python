#calculates and plots radioactive decay as a function of time
import math
import matplotlib.pyplot as plt

N0 = 1000
tau = 20
tmax = 100
dt = 10
Neu = 1000

tlist = []
Nexactlist = []
Neulist = []

for t in range(dt,tmax,dt):
  Nexact = N0 * math.exp(-t/tau)
  dNdt = -Neu/tau
  Neu = Neu +dt*dNdt
  tlist.append(t)
  Nexactlist.append(Nexact)
  Neulist.append(Neu)
  
plt.plot(tlist,Nexactlist)
plt.plot(tlist,Neulist)
plt.show()
