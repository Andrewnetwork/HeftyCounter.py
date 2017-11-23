from HeftyNumber import HeftyNumber

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

k = 930929309293092930929309293092930929829823832898398239238298323832328398329839283982938928398329839829839829389283
a = HeftyNumber(k,base=10)
print(a.bn(2))



