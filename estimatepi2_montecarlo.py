#estimating pi 10 times and calculating mean and standard deviation
import numpy as np

#enclose the Monte Carlo simulation in a loop which runs 10 times
na=0
pi_array=np.zeros(10)

while na<10:
    x=np.random.uniform(-1, 1, 10000)
    y=np.random.uniform(-1,1,10000)
    
    #x^2+y^2<1
    array=(x**2+y**2)
    mask=array<1
    
    #pi=4(number of points in circle)/r^2(number of total points)
    circle=np.sum(mask)
    pi=(4*circle)/(1**2*10000)
    print(pi)
    
    #store the 10 different estimates of π that you get in an array
    pi_array[na]=pi
    
    na+=1

#calculate the mean and standard deviation of these 10 values
print('mean=',np.mean(pi_array))
print('standard deviation=',np.std(pi_array))
