import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

X = np.zeros(shape=(2000,2))
y = np.zeros(2000)

X[0:1000,:] = np.random.normal(scale=0.4,loc=0,size=(1000,2))
#X[1000:2000,:] = np.random.normal(scale=0.4,loc=-1,size=(1000,2))
X[1000:2000,0:1] = np.random.normal(scale=0.4,loc=-1,size=(1000,1))
X[1000:2000,1:2] = np.random.normal(scale=0.4,loc=0.3,size=(1000,1))
y[0:1000]=1
y[1000:2000]=0

print X.shape,y.shape

fig = plt.figure(figsize=(8,6))
inset = fig.add_subplot(111)

inset.plot(X[:,0][np.where(y==1)],X[:,1][np.where(y==1)],'.')
inset.plot(X[:,0][np.where(y==0)],X[:,1][np.where(y==0)],'.')

from sklearn.linear_model import LogisticRegression


clf = LogisticRegression()
clf.fit(X,y)

print clf.coef_,clf.intercept_

xplot = np.linspace(-1.5,2.5,100)
yplot = (-xplot * clf.coef_[0][0]  - clf.intercept_)/clf.coef_[0][1]


inset.set_xlim(-3,3)
inset.set_ylim(-3,3)

inset.plot(xplot,yplot)
plt.savefig('simple-logistic-regression.png',bbox_inches='tight')

