import numpy as np
import matplotlib.pyplot as plt

height = 5
density = 1

radius = np.array([9.3, 7, 8.6, 6.7, 5.5, 9, 7.3, 7.4, 8.3, 7.7])
mass = np.array([1500, 700, 1200, 800, 450, 1200, 850, 900, 1000, 800])

# volume of a cylinder = pi*r^2*h where h=height, r=radius and pi=unknown value
# density = mass/volume

radius_squared = radius ** 2
y = mass


def ls_best_fit(x, y):  # x = r^2, y = mass and pi = gradient/(height*density)= gradient/5
    x = radius_squared
    y = mass
    x_bar = np.sum(x) / len(x)
    y_bar = np.sum(y) / len(y)
    m = (np.sum((x - x_bar) * (y - y_bar))) / (np.sum((x - x_bar) ** 2))
    c = y_bar - (m * x_bar)
    return (m, c)


m, c = ls_best_fit(radius_squared, mass)
mass_of_best_fit = m * radius_squared + c
mass_theoretical = density * np.pi * radius_squared * height

plt.plot(radius_squared, mass_of_best_fit, color='black', linestyle='solid', lw='1')
plt.plot(radius_squared, mass_theoretical, color='blue', linestyle='dotted')
plt.plot(radius_squared, mass, '.', color='red')
plt.legend(['Best Fit', 'Theoretical', 'Pie Mass'])
plt.title('Plot of masses of the pies as a function of the square of their radii')
plt.xlabel('$radius^2$/$cm^2$')  # dollar signs allow superscripts to be displayed on the graph
plt.ylabel('mass/g')

pi = m / 5

print("Pi =", pi)
print("Best fit gradient =", m)
print("Best fit intercept =", c)
