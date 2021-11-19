#simulating the solar system using 4th order runge-kutta
#also plotting kinetic energy as a function of time to investigate an asteroid in a kirkwood gap
#also plotting distance from the origin as a function of time to investigate the movement of the sun

import numpy as np 
import matplotlib.pyplot as plt 
import math

#create body class to store all planets with their attributes
class Body():
  def __init__(self, mass, x_vec, v_vec, colour, KE, radius, name=None):
    self.name = name
    self.mass = mass
    self.x_vec = x_vec
    self.v_vec = v_vec
    self.colour = colour
    self.KE = KE
    self.radius = radius

  #puts the position and velocity vectors together
  def return_vec(self):
    return np.concatenate((self.x_vec,self.v_vec))

  def return_mass(self):
    return self.mass

  def return_name(self):
    return self.name

#create simulation class where key calculations are done
class Simulation():
  def __init__(self,bodies):  
    self.bodies = bodies
    self.Nbodies = len(self.bodies)
    self.full_vec = np.concatenate(np.array([i.return_vec() for i in self.bodies]))
    self.mass_vec = np.array([i.return_mass() for i in self.bodies])
    self.name_vec = [i.return_name() for i in self.bodies]

  #function which calculates 4 approximations and outputs a new y vector
  def rk4(self,t,dt):
    k1 = dt * self.diff_eqs(t,self.full_vec,self.mass_vec) 
    k2 = dt * self.diff_eqs(t + 0.5*dt,self.full_vec+0.5*k1,self.mass_vec)
    k3 = dt * self.diff_eqs(t + 0.5*dt,self.full_vec+0.5*k2,self.mass_vec)
    k4 = dt * self.diff_eqs(t + dt,self.full_vec + k2,self.mass_vec)

    y_new = self.full_vec + ((k1 + 2*k2 + 2*k3 + k4) / 6.0)
    
    return y_new
  
  #appends x, y, vx, vy to history
  def run(self,T,dt,t0=0):
    self.history = [self.full_vec]
    nsteps = int((T-t0)/dt)
    for step in range(nsteps):
      y_new = self.rk4(0,dt)
      self.history.append(y_new)
      self.full_vec = y_new
      
    self.history = np.array(self.history)
    return nsteps

  def calc_accel(self, diff_eqs):
    self.diff_eqs = diff_eqs

#functions which calculates acceleration acting on body
def nbody_solve(t,y,masses):
    G = 6.67e-11
    Nbodies = int(len(y) / 4)
    vector_end = np.zeros(y.size)
    for i in range(Nbodies):
        itick = i*4
        for j in range(Nbodies):
            jtick = j*4
            vector_end[itick:itick+2] = y[itick+2:itick+4]
            if i != j: #so that eg. the earth is not pulled by the earth
                dx = y[itick] - y[jtick]
                dy = y[itick+1] - y[jtick+1]
                r = (dx**2+dy**2)**0.5
                ax = (-G * masses[j] / r**3) * dx
                ay = (-G * masses[j] / r**3) * dy
                vector_end[itick+2] += ax
                vector_end[itick+3] += ay          
    return vector_end 

Mercury = Body(name="Mercury",
  x_vec = np.array([4.7357e10 ,0]),
  v_vec = np.array([0,47.36e3]),
  mass = 3.285e23,
  colour = 'blue',
  KE = [],
  radius = [])

Venus = Body(name="Venus",
  x_vec = np.array([1.088e11,0]),
  v_vec = np.array([0,35.02e3]),
  mass = 4.867e24,
  colour = 'pink',
  KE = [],
  radius = [])

Earth = Body(name="Earth",
  x_vec = np.array([1.496e11,0]),
  v_vec = np.array([0,29.78e3]),
  mass = 5.9742e24,
  colour = 'green',
  KE = [],
  radius = [])

Mars = Body(name="Mars",
  x_vec = np.array([2.4288e11,0]),
  v_vec = np.array([0,24.07e3]),
  mass = 6.39e23,
  colour = 'red',
  KE = [],
  radius = [])

Jupiter = Body(name="Jupiter",
  x_vec = np.array([7.4956e11,0]),
  v_vec = np.array([0,13.06e3]),
  mass = 1.8986e27,
  colour = 'orange',
  KE = [],
  radius = [])

Saturn = Body(name="Saturn",
  x_vec = np.array([1.4835e12,0]),
  v_vec = np.array([0,9.68e3]),
  mass = 5.683e26,
  colour = 'crimson',
  KE = [],
  radius = [])

Uranus = Body(name="Uranus",
  x_vec = np.array([2.9513e12,0]),
  v_vec = np.array([0,6.8e3]),
  mass = 8.681e25,
  colour = 'cyan',
  KE = [],
  radius = [])

Neptune = Body(name="Neptune",
  x_vec = np.array([4.475e12,0]),
  v_vec = np.array([0,5.43e3]),
  mass = 1.024e26,
  colour = 'indigo',
  KE = [],
  radius = [])

#constants
G = 6.67e-11
mass_sun = 1.98892e30
conAU = 1.495978707e11

#radius and velocity of asteroid
r = 3.279 *conAU
v = math.sqrt((G*mass_sun)/r)

#kirkwood gap asteroid
Asteroid = Body(name="Asteroid",
  x_vec = np.array([r,0]),
  v_vec = np.array([0,v]),
  mass = 0.95e21,
  colour = "lightblue",
  KE = [],
  radius = [])

#calculating the sun's velocity to be equal and opposite to the system's velocity
mom_bodies = [Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Asteroid]
tot_mom = 0
for index, i in enumerate(range(0,len(mom_bodies)*4,4)):
  tot_mom+= mom_bodies[index].mass*mom_bodies[index].v_vec[1]
v_sun = -1*(tot_mom/mass_sun)

Sun = Body(name="Sun",
  x_vec = np.array([0,0]),
  v_vec = np.array([0,v_sun]),
  mass = mass_sun,
  colour = 'gold',
  KE = [],
  radius = [])

#list of bodies which are to be plotted
bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune, Asteroid]

#running the simulation and appending the x, y, vx, vy values to history
simulation = Simulation(bodies)
simulation.calc_accel(nbody_solve)
simulation.run(500*365*24*60*60, 24*60*60)
history = simulation.history

#calculating kinetic energy
for index, j in enumerate(range(2,len(bodies)*4,4)):
  for time in range(1,len(history)):
    KE = bodies[index].KE
    mass = bodies[index].mass
    kinEn = 0.5*mass*((history[time,j]**2+history[time,j+1]**2))
    bodies[index].KE.append(kinEn)

#calculating distance from origin
for index, j in enumerate(range(0,len(bodies)*4,4)):
  for time in range(1,len(history)):
    AU = 1.495978707e11
    radius = bodies[index].radius
    rad = np.hypot(history[time,j],history[time,j+1])
    bodies[index].radius.append(rad/AU)

#time values for plotting kinetic energy and radius graphs
dt = []
for i in range(0,500*365*24*60*60,24*60*60):
  dt.append(i)

#plotting kinetic energy as a function of time
for index, i in enumerate(range(0, len(bodies) * 4, 4)):
  kinEn = bodies[index].KE
  plt.plot(dt, kinEn , label=bodies[index].name, color = bodies[index].colour)
  plt.title('Kinetic energy as a function of time')
  plt.xlabel('time (s)')
  plt.ylabel('Kinetic energy (J)')
  plt.legend()
  plt.show()

#plotting radius as a function of time
for index, i in enumerate(range(0, len(bodies) * 4, 4)):
  radius = bodies[index].radius
  plt.plot(dt, radius , label=bodies[index].name, color = bodies[index].colour)
  plt.title('Orbital radius as a function time')
  plt.xlabel('time (s)')
  plt.ylabel('Orbital Radius (AU)')
  plt.legend()
  plt.show()

AU = 1.495978707e11

#plotting final locations of each body as a circle
for index, i in enumerate(range(0, len(bodies) * 4, 4)):
  plt.plot((history[-1,i])/AU, (history[-1,i+1])/AU, 'o', color = bodies[index].colour )

#plotting the orbit of each body
for index, i in enumerate(range(0, len(bodies) * 4, 4)):
  plt.plot((history[:,i])/AU, (history[:,i+1])/AU, label=bodies[index].name, color = bodies[index].colour)

plt.title('Orbit of planets and asteroid X around the Sun')
plt.xlabel('x position (AU)')
plt.ylabel('y position (AU)')
plt.legend()
plt.axis('equal')
plt.show()
