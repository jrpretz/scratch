import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

n_a_draw = 3
n_b_draw = 10

samples_a=np.random.randn(n_a_draw)
samples_b=np.random.randn(n_b_draw)


sample_a_means = np.sum(samples_a,axis=0)/n_a_draw
sample_a_variances = np.sum(((samples_a-sample_a_means)**2)/(n_a_draw-1))

sample_b_means = np.sum(samples_b,axis=0)/n_b_draw
sample_b_variances = np.sum(((samples_b-sample_b_means)**2)/(n_b_draw-1))


sp = np.sqrt(  ((n_a_draw - 1) * sample_a_variances + (n_b_draw - 1)*sample_b_variances)/(n_a_draw + n_b_draw -2))
t = (sample_a_means - sample_b_means)/(sp * np.sqrt( (1./n_a_draw) + (1./n_b_draw)))

# these should match
print(t)
print(scipy.stats.ttest_ind(samples_a,samples_b).statistic)
