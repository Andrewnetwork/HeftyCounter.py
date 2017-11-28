import numpy as np

class DigitUtils:
    def countPrimeDigits(heftyNum,digits)->"[counts per digit]":
        if type(digits) is not list:
            digits = [digits]

        cntDict = dict.fromkeys(digits,0)

        for i in np.nditer(heftyNum.baseCoef):
            if i in digits:
                cntDict[int(i)] += 1

        return cntDict

