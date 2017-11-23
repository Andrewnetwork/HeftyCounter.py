import numpy as np

class HeftyNumber:
    def __init__(self,base:"integer base"=10,baseCoef:"[2,3] = 23"=[0]):
        self.base = base
        self.counterSize = 1
        self.baseCoef = np.array(baseCoef)

    def __repr__(self):
        return str(self.baseCoef)

    def b10(self):
        return self.bn(10)

    def bn(self, n):
        pass

    def add(self, quantity):
        pass
