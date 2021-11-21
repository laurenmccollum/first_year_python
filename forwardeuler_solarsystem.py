#implements the forward Euler method to model the orbits of the four closest planets to the Sun.  
#assumes that each planet only feels the Sun's gravitational pull (and not that of the other planets) and that motion is confined to the xy-plane. 

import numpy as np
import matplotlib.pyplot as plt

# defining constants
G = 6.67408E-11  # gravitational constant
M = 1.989E30  # mass of sun
steps = 100000 #number of steps


# functions for gravitational force
def Force(x, y, m):
    Fx = -G * M * m * ((x) / (x ** 2 + y ** 2) ** (3 / 2))
    Fy = -G * M * m * ((y) / (x ** 2 + y ** 2) ** (3 / 2))
    return Fx, Fy


# array order= mercury, venus, earth and mars
x0 = np.array([46.00E09, 107.48E09, 147.09E09, 206.62E09])
y0 = np.array([0, 0, 0, 0])
vx0 = np.array([0, 0, 0, 0])
vy0 = np.array([58.98E3, 35.26E3, 30.29E3, 26.50E3])
m = np.array([0.33011E24, 4.8675E24, 5.9724E24, 0.64171E24])
dt = np.array([87.97, 224.7, 365.25, 686.98]) * 24 * 3600 / steps

# arrays for mercury
xm = np.zeros(steps)
ym = np.zeros(steps)
vxm = np.zeros(steps)
vym = np.zeros(steps)
xm[0] = x0[0]
ym[0] = y0[0]
vxm[0] = vx0[0]
vym[0] = vy0[0]

# array for venus
xv = np.zeros(steps)
yv = np.zeros(steps)
vxv = np.zeros(steps)
vyv = np.zeros(steps)
xv[0] = x0[1]
yv[0] = y0[1]
vxv[0] = vx0[1]
vyv[0] = vy0[1]

# array for earth
xe = np.zeros(steps)
ye = np.zeros(steps)
vxe = np.zeros(steps)
vye = np.zeros(steps)
xe[0] = x0[2]
ye[0] = y0[2]
vxe[0] = vx0[2]
vye[0] = vy0[2]

# array for mars
xma = np.zeros(steps)
yma = np.zeros(steps)
vxma = np.zeros(steps)
vyma = np.zeros(steps)
xma[0] = x0[3]
yma[0] = y0[3]
vxma[0] = vx0[3]
vyma[0] = vy0[3]

# values for sun
xs = 0
ys = 0

n = 0
while n < (steps - 1):
    Fx, Fy = Force(x0, y0, m)
    xn = x0 + vx0 * dt
    yn = y0 + vy0 * dt
    vxn = vx0 + (Fx / m) * dt
    vyn = vy0 + (Fy / m) * dt

    # assigns values to the mercury array
    xm[n + 1] = xn[0]
    ym[n + 1] = yn[0]
    vxm[n + 1] = vxn[0]
    vym[n + 1] = vyn[0]

    # assigns values to venus array
    xv[n + 1] = xn[1]
    yv[n + 1] = yn[1]
    vxv[n + 1] = vxn[1]
    vyv[n + 1] = vyn[1]

    # assigns values to earth
    xe[n + 1] = xn[2]
    ye[n + 1] = yn[2]
    vxe[n + 1] = vxn[2]
    vye[n + 1] = vyn[2]

    # assigns values to earth
    xma[n + 1] = xn[3]
    yma[n + 1] = yn[3]
    vxma[n + 1] = vxn[3]
    vyma[n + 1] = vyn[3]

    # edits values before looping
    x0 = xn
    y0 = yn
    vx0 = vxn
    vy0 = vyn
    n += 1

plt.plot(xm, ym, ':', color='blue')  # trajectory of mercury
plt.plot(xv, yv, ':', color='orange')  # trajectory of venus
plt.plot(xe, ye, ':', color='green')  # trajectory of earth
plt.plot(xma, yma, ':', color='red')  # trajectory of mars
plt.plot(x0[0], y0[0], 'ob', color='blue')
plt.plot(x0[1], y0[1], 'ob', color='orange')
plt.plot(x0[2], y0[2], 'ob', color='green')
plt.plot(x0[3], y0[3], 'ob', color='red')
plt.plot(xs, ys, 'o', color='black')
plt.xlabel('$X0$', fontsize=12)
plt.ylabel('$Y0$', fontsize=12)
plt.title('The orbits of the inner 4 planets around the Sun', fontsize=14)
plt.legend(['$Mercury$', '$Venus$', '$Earth$', '$Mars$'], fontsize=12)
plt.show()

print('Maximum distance of Mercury, Venus, Earth and Mars from the Sun respectively:')
print(max(((xm ** 2) + (ym ** 2)) ** 0.5), 'm')
print(max(((xv ** 2) + (yv ** 2)) ** 0.5), 'm')
print(max(((xe ** 2) + (ye ** 2)) ** 0.5), 'm')
print(max(((xma ** 2) + (yma ** 2)) ** 0.5), 'm', '\n')

print('Minimum distance of Mercury, Venus, Earth and Mars from the Sun respectively:')
print(min(((xm ** 2) + (ym ** 2)) ** 0.5), 'm')
print(min(((xv ** 2) + (yv ** 2)) ** 0.5), 'm')
print(min(((xe ** 2) + (ye ** 2)) ** 0.5), 'm')
print(min(((xma ** 2) + (yma ** 2)) ** 0.5), 'm', '\n')

print('Mean distance of Mercury, Venus, Earth and Mars from the Sun respectively:')
print(np.mean(((xm ** 2) + (ym ** 2)) ** 0.5), 'm')
print(np.mean(((xv ** 2) + (yv ** 2)) ** 0.5), 'm')
print(np.mean(((xe ** 2) + (ye ** 2)) ** 0.5), 'm')
print(np.mean(((xma ** 2) + (yma ** 2)) ** 0.5), 'm', '\n')

print('Maximum velocity of Mercury, Venus, Earth and Mars respectively:')
print(max(((vxm ** 2) + (vym ** 2)) ** 0.5), 'ms^-1')
print(max(((vxv ** 2) + (vyv ** 2)) ** 0.5), 'ms^-1')
print(max(((vxe ** 2) + (vye ** 2)) ** 0.5), 'ms^-1')
print(max(((vxma ** 2) + (vyma ** 2)) ** 0.5), 'ms^-1', '\n')

print('Minimum velocity of Mercury, Venus, Earth and Mars respectively:')
print(min(((vxm ** 2) + (vym ** 2)) ** 0.5), 'ms^-1')
print(min(((vxv ** 2) + (vyv ** 2)) ** 0.5), 'ms^-1')
print(min(((vxe ** 2) + (vye ** 2)) ** 0.5), 'ms^-1')
print(min(((vxma ** 2) + (vyma ** 2)) ** 0.5), 'ms^-1', '\n')

print('Mean velocity of Mercury, Venus, Earth and Mars respectively:')
print(np.mean(((vxm ** 2) + (vym ** 2)) ** 0.5), 'ms^-1')
print(np.mean(((vxv ** 2) + (vyv ** 2)) ** 0.5), 'ms^-1')
print(np.mean(((vxe ** 2) + (vye ** 2)) ** 0.5), 'ms^-1')
print(np.mean(((vxma ** 2) + (vyma ** 2)) ** 0.5), 'ms^-1', '\n')
