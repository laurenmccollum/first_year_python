#using numerical partial difference method to solve laplace's equation to calculate heat distribution across a simple two dimensional plate

import numpy as np

#student number 40260823

#boundary conditions
a = 0
b = 8
c = 2
d = 3

#array dimensions
iterations = 30
length = 4
width = 4

#initial condition
Tinitial = 0

#creating array
array = np.empty((iterations+1,width,length))
array.fill(Tinitial)

#set boundary conditions
array[:,3,1:3]=a
array[:,1:3,3]=b
array[:,0,1:3]=c
array[:,1:3,0]=d

#calculate T values at each iteration
for k in range(0,iterations):
  for i in range(1,length-1):
    for j in range(1,width-1):
      array[k+1,i,j]=(array[k,i-1,j] + array[k,i+1,j] + array[k,i,j-1] + array[k,i,j+1])/4

print(array[iterations,:,:])
