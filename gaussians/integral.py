import numpy as np
import math

class Gaussian1d:
    def __init__(self,mu,sigma):
        self.sigma = sigma
        self.mu = mu

    def __call__(self,x):
        return (1./(self.sigma*np.sqrt(2.*np.pi))) * np.exp(-(x-self.mu)*(x-self.mu)/(2*self.sigma*self.sigma))

    def integralAbove(self,x):
        return (1. - math.erf((x-self.mu)/(self.sigma*np.sqrt(2.))))/2.        

    def integralBetween(self,xlow,xhigh):
        a = math.erf((xlow-self.mu)/(self.sigma*np.sqrt(2.)))
        b = math.erf((xhigh-self.mu)/(self.sigma*np.sqrt(2.)))
        return (b-a)/2


class Gaussian2d:
    def __init__(self,x_mu,y_mu,sigma):
        self.x_mu = x_mu
        self.y_mu = y_mu
        self.sigma = sigma

    def __call__(self,x,y):
        a = (1/(self.sigma*self.sigma*2*np.pi))
        b = np.exp(-((x-self.x_mu)**2)/(2*self.sigma*self.sigma))
        c = np.exp(-((y-self.y_mu)**2)/(2*self.sigma*self.sigma))
        return  a * b * c

    def integralBetween(self,x_low,x_high,y_low,y_high):
        xs = np.linspace(x_low,x_high,1000)
        ys = np.linspace(y_low,y_high,1000)
        dx = (x_high - x_low)/1000.
        dy = (y_high - y_low)/1000.

        xx,yy = np.meshgrid(xs,ys)

        tot = self.__call__(xx,yy) 

        return np.sum(tot)* dx * dy
        

g = Gaussian2d(0.5,2.,1.0)

#print(g.integralBetween(-10,10,-10,10))

g1 = Gaussian1d(0.5,1.0)
g2 = Gaussian1d(2.,1.0)

#print(g.integralBetween(0,10,0,10))
#print(g1.integralBetween(0,10)*g2.integralBetween(0,10))



print(g.integralBetween(-10,10,-10,10))
print(g.integralBetween(0,1,-10,10))
a1 = g1.integralBetween(0,1)*g2.integralBetween(-10,10)
print(a1)

