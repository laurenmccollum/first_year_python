#A bag contains five red beads, three green beads, and two blue beads.
#Two beads are drawn from the bag at random, without replacement.  Each bead is equally likely to be drawn.  
#Monte Carlo simulation models this problem and provides estimates to the following questions:
#What is the probability that the first bead drawn is red?
#What is the probability that at least one of the two beads drawn is red?
#What is the probability that the second bead drawn is red, given that the first bead drawn is red?

import numpy as np

times=1000000
na=0
first_red=0
one_red=0
both_red=0

while na<times:
    nb=0
    bag=['red','red','red','red','red','green','green','green','blue','blue']
    picks=[]
    while nb<2:
        pick=np.random.choice(bag)
        picks.append(pick)
        bag.remove(pick)
        nb+=1
    if picks[0]=='red':
        first_red+=1
    if(picks[0]=='red')|(picks[1]=='red'):
        one_red+=1
    if(picks[0]=='red')&(picks[1]=='red'):
        both_red+=1
    na+=1
    
print('probability first bead is red=', first_red/times)
print('probability at least one red=', one_red/times)
print('probability second red given first red=', both_red/first_red)
