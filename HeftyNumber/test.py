from HeftyNumber import HeftyNumber

# A HeftyNumber in base 30 with a seed vector of size 1 ( this expands as needed ).
hn = HeftyNumber(1,30)

# We can add a base 10 number to our hefty number. ( Will be adding full features for all bases soon )
hn.add(1000000000)

# Prints a vector representation of 1000000000 in base 30.
print(hn)

# Prints a vector representation of 1000000000 in base 10.
print(hn.b10())