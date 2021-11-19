#calculates and plots the orbital position of earth over a time t using 4th order runge-kutta
import numpy as np 
import matplotlib.pyplot as plt

#function which calculates acceleration as a result of gravitational forces
def orbit(u):
    M = 1.98892e30
    G = 6.67e-11
    x,y,vx,vy = u
    r = np.hypot(x,y) #the np.hypot() function is used to calculate the hypotenuse for the right-angled triangle
    f = G*M/r**3
    return np.array([vx, vy, -f*x, -f*y])

#function which calculates the 4 runge-kutta approximations and returns the new acceleration
def RK4step(f,u,dt):
    k1 = dt*f(u)
    k2 = dt*f(u+0.5*k1)
    k3 = dt*f(u+0.5*k2)
    k4 = dt*f(u+k3)
    return u + (k1+2*k2+2*k3+k4)/6

#combines the runge kutta function into an integration loop
def RK4integrate(f, y0, tspan):
    y = np.zeros([len(tspan),len(y0)])
    y[0,:]=y0
    for k in range(1, len(tspan)):
        y[k,:] = RK4step(f, y[k-1], tspan[k]-tspan[k-1])
    return y

dt = 24*60*60 #time step
t = np.arange(0,365.25*24*60*60,dt) #runs for a time of 1 year with time step dt
y0 = np.array([1.496e11, 0, 0, 29.78e3]) #x and y position and velocity values for Earth

#calls the RK4integrate function and assigns new values to x, y, vx and vy for Earth
sol_RK4 = RK4integrate(orbit, y0, t) 
x,y,vx,vy = sol_RK4.T

AU = 1.495978707e11

plt.plot(x/AU,y/AU, label='Earth', color = 'green') #plotting the position of Earth
plt.plot(0,0,'o', label='Sun', color = 'gold') #plotting the stationary Sun at the origin
plt.axis('equal')
plt.title("Orbit of Earth around the Sun")
plt.xlabel("x position (AU)")
plt.ylabel("y position (AU)")
plt.legend()
plt.show()
