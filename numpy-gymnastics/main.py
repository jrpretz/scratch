
import numpy as np

print "Setting seed manually so this is deterministic"
np.random.seed(0)

print "Generating some random data"
X = np.random.rand(100,3)

print "X shape",X.shape

print X

print "Printing the first 5 rows"
print X[0:5,:]

print "Printing the first column"
print X[:,0]

print "A matrix for us to multiply by"
a = np.random.rand(3,5)

print "And multiplying it"
print np.dot(X, a).shape

b = np.zeros(shape=(3,1))
b[0] = 1.0
print b.shape
c = np.dot(X,b)
print c.shape

print X[0][0],c[0]
print X[1][0],c[1]
print X[2][0],c[2]


print "Adding a column of ones"
tot = np.append(np.ones((X.shape[0],1)),X,axis=1)

print tot[0][0],"should be 1"
print tot[1][0],"should be 1"
print tot[2][0],"should be 1"
