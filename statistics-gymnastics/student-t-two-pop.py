# do two populations have the same underlying mean

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
#%matplotlib inline

n_trials = 1000000

# number of samples from each population
n_a_draw = 3
n_b_draw = 10

# the random samples
samples_a=np.random.randn(n_a_draw,n_trials)
samples_b=np.random.randn(n_b_draw,n_trials)

# the mean and variances of each sample
sample_a_means = np.sum(samples_a,axis=0)/n_a_draw
sample_a_variances = np.sum(((samples_a-sample_a_means)**2)/(n_a_draw-1),axis=0)

sample_b_means = np.sum(samples_b,axis=0)/n_b_draw
sample_b_variances = np.sum(((samples_b-sample_b_means)**2)/(n_b_draw-1),axis=0)

# computation of the t statistic
# some shit-ass notes off the internet 
# (http://web.mit.edu/~csvoss/Public/usabo/stats_handout.pdf) were wrong
#
# luckily, the wikipedia had the right formula
# https://en.wikipedia.org/wiki/Student%27s_t-test#Independent_two-sample_t-test

sp = np.sqrt(  ((n_a_draw - 1) * sample_a_variances + (n_b_draw - 1)*sample_b_variances)/(n_a_draw + n_b_draw -2))
t = (sample_a_means - sample_b_means)/(sp * np.sqrt( (1./n_a_draw) + (1./n_b_draw)))


fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(1,1,1)

# distribution of t
ax.hist(t,bins=1000,range=(-20,20))

# theoretical distribution of t, note the correction for binning
x = np.linspace(-20,20,100)
ax.plot(x,scipy.stats.t.pdf(x,df=(n_a_draw - 1 + n_b_draw - 1))*n_trials*0.04)

ax.set_yscale("log", nonposy='clip')
plt.savefig("t-two-population-means.png")
