import random
from math import sqrt

ptrue = 0.3

nsuccess = 0
ntrials = 0

for i in range(0,10000):
    if(random.random() < ptrue):
        nsuccess += 1
    ntrials += 1

    mean_p = nsuccess/ntrials


    err = 1.96 * sqrt(mean_p*(1-mean_p)/ntrials)
    print(i,mean_p,err)
