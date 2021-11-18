#estimates pi using monte carlo simulations
import numpy as np
import matplotlib.pyplot as plt

#create two arrays; one called x and one called y which each contain 1000 randomly and uniformly distributed real numbers between -1 and 1
x=np.random.uniform(-1, 1, 1000)
y=np.random.uniform(-1,1,1000)

#create a plot of y versus x, where the plot markers are points
plt.plot(x,y, '.')

#mathematical expression that defines which (x,y) pairs of data points are located inside a circle of radius 1, centred at the origin
#x^2+y^2<1

#use Boolean masks to identify the points that are inside the circle and overplot them in a different colour and marker size than used in the previous plot
array=(x**2+y**2)
mask=array<1

plt.plot(x[mask],y[mask], '.')
plt.xlabel('x')
plt.ylabel('y')

#how you get an estimate for the value of π by using the number of points inside the circle and the total number of points inside the full square
#pi=4(number of points in circle)/r^2(number of total points)

#calculate an estimate for the value of π and print this to the console
circle=np.sum(mask)
pi=(4*circle)/(1**2*1000)
print(pi)
