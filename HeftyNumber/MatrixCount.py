import numpy as np
from HeftyNumber import HeftyNumber

class MatrixCount:
    def permGroup(shape,base):
        group = []
        len = shape[0]*shape[1]
        cntr = HeftyNumber(0,base)

        for i in range(base ** len):
            group.append(cntr.paddedNum(len).reshape(shape))
            cntr+=1

        return group
