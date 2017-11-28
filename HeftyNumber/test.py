from HeftyNumber import HeftyNumber
from DigitUtils import DigitUtils
from MatrixCount import MatrixCount

# A HeftyNumber in base 30 with a seed vector of size 1 ( this expands as needed ).
#hn = HeftyNumber(1,30)

# We can add a base 10 number to our hefty number. ( Will be adding full features for all bases soon )
#hn.add(1000000000)

# Prints a vector representation of 1000000000 in base 30.
#print(hn)

# Prints a vector representation of 1000000000 in base 10.
#print(hn.b10())

#z = HeftyNumber(1,15)
#z.add(8767589898984)
#print(z)
#print(z.bn(10))
import numpy as np

k = 930929309293092930929309293092930929829823832898398239238298323832328398329839283982938928398329839829839829389283
a = HeftyNumber(1000,base=2)

#f = HeftyNumber(k,base=1000000000000000)
#for i in range(2,100,1):
    #z = HeftyNumber(k,base=i)
    #print(DigitUtils.countPrimeDigits(z,[0,1,2,3,4,5,6,7,8,9]))
    #print(DigitUtils.countPrimeDigits(z, 0)[0]/z.n())

#MatrixCount.permGroup((2,2),2)
a = MatrixCount.permGroup((2,2),2)
for i in a:
    print(i)

#a = HeftyNumber(10,base=2)
#print(a)
#print( a.map2Lex({0:"a",1:"b"}) )

#lex = {0:' ',1:'A',2:'N',3:'D',4:'R',5:'E',6:'W'}
#a = HeftyNumber(np.matrix([[1,2,3,4,5,6]]),base=7)
#print( a.map2Lex(lex) )
