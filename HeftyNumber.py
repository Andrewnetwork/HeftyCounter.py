import numpy as np

class HeftyNumber:
    def __init__(self, length, base):
        self.base = base
        self.counterSize = length
        self.vect = np.zeros(length)

    def __repr__(self):
        return str(self.vect)

    def b10(self):
        return self.bn(10)

    def bn(self, n):
        a = HeftyNumber(1, n)
        idx = self.counterSize - 1
        countr = 0
        while idx >= 0 and self.vect[idx] != 0:
            r = self.vect[idx] * (self.base ** countr)
            a.add(r)
            countr += 1
            idx -= 1
        return a

    def add(self, quantity):

        if quantity != 0:
            remainder = quantity
            additionRemainder = 0
            counterIndex = 0
            additionTemp = 0
            digitCount = 1
            cond = True

            # Convert quantity to the counters base and add it to the counter at the same time.
            while cond:
                counterIndex = self.counterSize - digitCount
                additionTemp = (self.vect[counterIndex] + (remainder % self.base) + additionRemainder)
                self.vect[counterIndex] = additionTemp % self.base
                additionRemainder = int(additionTemp) // int(self.base)
                remainder = remainder // self.base

                if (additionRemainder > 0 or remainder > 0) and digitCount >= self.counterSize:
                    # Overflow.
                    self.vect = np.insert(self.vect, 0, 0)
                    self.counterSize += 1

                digitCount += 1

                cond = remainder > 0 or additionRemainder > 0