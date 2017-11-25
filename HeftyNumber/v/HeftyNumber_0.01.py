import numpy as np
import math

class HeftyNumber:
    def __init__(self,baseCoef:"[2,3] = 23"=[0],base:"integer base"=10):
        self.base = base

        if type(baseCoef) is list:
            self.baseCoef = np.matrix(baseCoef)
        else:
            numStr = str(baseCoef)
            coef = np.matrix([int(i) for i in numStr])
            self.baseCoef = self.b10bn(coef, base)

        self.base10 = self.toB10()

    def __repr__(self):
        return str(self.baseCoef)

    def argmin_s(self, x, base, power) -> "[min,arg_min]":

        minVal, lastMinVal = 1, 1
        fundamental = base ** power

        for i in range(0, base):
            minVal = x - fundamental * i

            if (minVal < 0):
                return [lastMinVal, i - 1]
            if (minVal == 0):
                return [minVal, i]

            lastMinVal = minVal

        return [minVal, i]

    #TODO: vectorize
    def subtract(self,vect,scalar):
        pass

    def baseVect(self, base, n):
        num = [1]

        r = 1
        for i in range(n):
            r = base * r
            num = [r] + num

        return np.matrix(num)

    def b10bn(self,b10Num, base) -> "ndarry":
        if (base == 1):
            return np.ones(b10Num)

        logNum = math.log(b10Num, base)
        num    = []

        if logNum == 1:
            nDigits = 2
        else:
            nDigits = math.ceil(logNum)

        for i in range(nDigits - 1, 0, -1):
            b10Num, idx = self.argmin_s(b10Num, base, i)
            num.append(idx)

        num.append(b10Num)

        return np.matrix(num)

    def b10(self):
        return self.base10

    def toB10(self):
        rVect = self.baseVect(self.base, self.baseCoef.shape[1] - 1)
        return self.baseCoef * rVect.T

    def bn(self, n):
        b10Num = int(self.b10())
        return self.b10bn(b10Num,n)

    def add(self, quantity):
        pass
