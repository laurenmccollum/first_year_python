#Finds the value of x for which T is at a minimum. In accordance with Fermat's principle, this will define the path that light travels from point A to point B.
#Then shows that for this minimizing value of x, Snell's law holds.

import numpy as np
import matplotlib.pyplot as plt

a = 2
b = 3
l = 7
c = 299792458 #speed of light in vacuum
v1 = c
v2 = 0.5 * c

def time(x):
    return (np.sqrt(x ** 2 + a ** 2)/v1) + (np.sqrt((l - x) ** 2 + b ** 2) / v2)


x = np.linspace(0, 7, 10000)  # range over which function is calculated

plt.plot(x, time(x), color='black', linestyle='dashed')
plt.legend(['Minimum'])
plt.title('Plot of time against distance')
plt.xlabel('x/m')
plt.ylabel('T(x)/s')
plt.show()

print(f"Minimizing value of x (by brute-force):x = {x[np.argmin(time(x))]}")  # brute force method

# gradient descent method

x0 = 8
xn = x0
gamma = c / 10  # the learning rate
iterations = 100
xn_array = np.zeros(iterations)

for i in range(iterations):
    xn = xn - gamma * (xn / (v1 * np.sqrt(xn ** 2 + a ** 2)) - (l - xn) / (v2 * np.sqrt((l - xn) ** 2 + b ** 2)))
    xn_array[i] = xn

plt.plot(x, time(x), color='black', linestyle='dashed')
plt.plot(xn_array, time(xn_array), 'o', color='red', linestyle='solid')
plt.legend(['Brute Force Approach', 'Gradient Descent Minimization'])
plt.title('Plot of time against distance')
plt.xlabel('x/m')
plt.ylabel('T(x)/s')
plt.show()

print(f"Minimizing value of x (by 100 iterations of gradient descent):x = {xn}")

#verifying snell's law

theta1 = np.arctan(xn / a)
theta2 = np.arctan((l - xn) / b)
lhs = np.sin(theta2) / np.sin(theta1)

print(f"sin(theta_2)/sin(theta_1) = {lhs}")
print(f"v2/v1 = {v2 / v1}")

