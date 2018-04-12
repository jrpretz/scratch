import random
from math import sqrt

class Bandit:
    def __init__(self,pwin):
        self.pwin = pwin

    def play(self):
        if(random.random() < self.pwin):
            return 1
        return 0


class Scorecard:
    def __init__(self):
        self.mean = 0.5
        self.ci = 0.5

        self.ntrials = 0
        self.nwin = 0

    def record(self,winloss):
        if(winloss):
            self.nwin += 1
        self.ntrials += 1
        self.mean = self.nwin/self.ntrials
        if(self.nwin == 0):
            self.ci = 1.0
        else:
            self.ci = 1.96 * sqrt(self.mean * (1-self.mean)/self.ntrials)

    def getUL(self):
        ul = self.mean  + self.ci
        if ul > 1:
            ul = 1
        return ul

    def getMean(self):
        return self.mean

bandit1 = Bandit(0.2)
score1 = Scorecard()

bandit2 = Bandit(0.21)
score2 = Scorecard()

for i in range(0,10000):
    chosenMachine = 0
    if(score1.getUL() > score2.getUL()):
        res = bandit1.play()
        score1.record(res)
        chosenMachine = 1
    else:
        res = bandit2.play()
        score2.record(res)
        chosenMachine = 2

    print(i,chosenMachine,score1.getMean(),score1.getUL(),score2.getMean(),score2.getUL())
