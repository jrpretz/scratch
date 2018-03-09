# computing the student-t distribution by hand and plotting against
# the theoretical distribution

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

x = np.linspace(-20,20,100)

n_draw = 5
n_samples = 100000

# computing means and variances
samples=np.random.randn(n_draw,n_samples)
sample_means = np.sum(samples,axis=0)/n_draw
sample_variances = np.sum((samples - sample_means)**2,axis=0)/(n_draw-1)

# compuring the 't' variable
t=sample_means/((np.sqrt(sample_variances)/np.sqrt(n_draw)))

fig = plt.figure(figsize=(5,3))
ax = fig.add_subplot(1,1,1)

# theoretical distribution. The 0.4 is for the finite binning. 
ax.plot(x,scipy.stats.t.pdf(x,df=n_draw - 1)*n_samples*0.4)
ax.set_yscale("log", nonposy='clip')

# 'by hand' distribution
dummy=ax.hist(t,bins=100,range=(-20,20))    

ax.set_title("Student T - 4 dof")

plt.savefig("student-t.png")
