#calculating earths orbital period using 4th order runge-kutta

import numpy as np 
import matplotlib.pyplot as plt 

class Body():
  def __init__(self, mass, x_vec, v_vec, colour, name=None):
    self.name = name
    self.mass = mass
    self.x_vec = x_vec
    self.v_vec = v_vec
    self.colour = colour

  def return_vec(self):
    return np.concatenate((self.x_vec,self.v_vec))

  def return_mass(self):
    return self.mass

  def return_name(self):
    return self.name

class Simulation():
  def __init__(self,bodies):  
    self.bodies = bodies
    self.Nbodies = len(self.bodies)
    self.full_vec = np.concatenate(np.array([i.return_vec() for i in self.bodies]))
    self.mass_vec = np.array([i.return_mass() for i in self.bodies])
    self.name_vec = [i.return_name() for i in self.bodies]

  def rk4(self,t,dt):
    k1 = dt * self.diff_eqs(t,self.full_vec,self.mass_vec) 
    k2 = dt * self.diff_eqs(t + 0.5*dt,self.full_vec+0.5*k1,self.mass_vec)
    k3 = dt * self.diff_eqs(t + 0.5*dt,self.full_vec+0.5*k2,self.mass_vec)
    k4 = dt * self.diff_eqs(t + dt,self.full_vec + k2,self.mass_vec)

    y_new = self.full_vec + ((k1 + 2*k2 + 2*k3 + k4) / 6.0)

    return y_new

  def run(self,T,dt,t0=0):
    self.history = [self.full_vec]
    nsteps = int((T-t0)/dt)
    for step in range(nsteps):
      y_new = self.rk4(0,dt)
      self.history.append(y_new)
      self.full_vec = y_new
    
    self.history = np.array(self.history)

  def run_orbit(self,T,dt,t0=0):
    self.history = [self.full_vec]
    nsteps = int((T-t0)/dt)
    flag = 0
    t=0
    for step in range(nsteps):
      y_new = self.rk4(0,dt)
      self.history.append(y_new)
      self.full_vec = y_new

      #comment
      if y_new[5] > 0 and flag == 0:
        flag = 1
        t=0
      elif y_new[5] < 0 and flag == 1:
        flag = 2
      elif y_new[5] > 0 and flag == 2:
        print("Orbital Period of Earth =", t/(60*60*24), "days")
        break
      
      #comment
      if y_new[5] < 0 and flag == 0:
        flag = -1
      elif y_new[5] > 0 and flag == -1:
        flag = -2
      elif y_new[5] < 0 and flag == -2:
        print("Orbital Period of Earth =", t/(60*60*24), "days")
        break
      t+=dt

    self.history = np.array(self.history)

  def calc_accel(self,diff_eqs):
      self.diff_eqs = diff_eqs

def nbody_solve(t,y,masses):
    G = 6.67e-11
    Nbodies = int(len(y) / 4)
    solved_vector = np.zeros(y.size)
    for i in range(Nbodies):
        itick = i*4
        for j in range(Nbodies):
            jtick = j*4
            solved_vector[itick:itick+2] = y[itick+2:itick+4]
            if i != j:
                dx = y[itick] - y[jtick]
                dy = y[itick+1] - y[jtick+1]
                r = np.hypot(dx,dy)
                ax = (-G * masses[j] / r**3) * dx
                ay = (-G * masses[j] / r**3) * dy
                solved_vector[itick+2] += ax
                solved_vector[itick+3] += ay          
    return solved_vector 

mass_sun = 1.98892e30

Earth = Body(name="Earth",
  x_vec = np.array([1.496e11,0]),
  v_vec = np.array([0,29.78e3]),
  mass =  5.9742e24,
  colour = "green")

mom_bodies = [Earth]
tot_mom = 0
for index, i in enumerate(range(0,len(mom_bodies)*4,4)):
  tot_mom+= mom_bodies[index].mass*mom_bodies[index].v_vec[1]
v_sun = -1*(tot_mom/mass_sun)

Sun = Body(name="Sun",
    x_vec = np.array([0,0]),
    v_vec = np.array([0,0]),
    mass = mass_sun,
    colour = "gold")

bodies = [Sun,Earth]

simulation = Simulation(bodies)
simulation.calc_accel(nbody_solve)

simulation.run_orbit(365.25*24*60*60, 1*60*60)
history = simulation.history

AU = 1.495978707e11

for index, i in enumerate(range(0, len(bodies) * 4, 4)):
  plt.plot((history[-1,i])/AU, (history[-1,i+1])/AU, 'o', color = bodies[index].colour )

for index, i in enumerate(range(0, len(bodies) * 4, 4)):
  plt.plot((history[:,i])/AU, (history[:,i+1])/AU, label=bodies[index].name, color = bodies[index].colour)

plt.title('Orbit of Earth and Sun with equal masses')
plt.xlabel('x position (AU)')
plt.ylabel('y position (AU)')
plt.legend()
plt.axis('equal')
plt.show()
