import numpy as np
import math

class HeftyNumber:
    def __init__(self,base:"integer base"=10,baseCoef:"[2,3] = 23"=[0]):
        self.base = base

        if type(baseCoef) is list:
            self.baseCoef = np.array(baseCoef)
        else:
            numStr = str(baseCoef)
            self.baseCoef = np.array([int(i) for i in numStr])

    def __repr__(self):
        return str(self.baseCoef)

    # TODO: vectorize
    def __argmin_s(self, x, base, power) -> "[min,arg_min]":

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

        if n == 1:
            return np.array(num)
        else:
            r = 1
            for i in range(n):
                r = base * r
                num = [r] + num

            return np.matrix(num)

    #TODO: vectorize
    def b10bn(self,b10Num, base) -> "ndarry":
        if (base == 1):
            return np.ones(b10Num)

        logNum = math.log(b10Num, base)
        num = []

        if logNum == 1:
            nDigits = 2
        else:
            nDigits = math.ceil(logNum)

        for i in range(nDigits - 1, 0, -1):
            b10Num, idx = self.argmin_s(b10Num, base, i)
            num.append(idx)

        num.append(b10Num)

        return np.array(num)

    def b10(self):
        rVect = self.baseVect(self.base, self.baseCoef .shape[0] - 1)
        return self.baseCoef * rVect.T

    def bn(self, n):
        b10Vect = self.b10()
        return self.b10bn(b10Vect,n)

    def add(self, quantity):
        pass
