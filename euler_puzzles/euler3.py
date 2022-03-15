#!/usr/bin/env python

#This script finds the largest prime number of a numerical argument

import sys

numx = int(sys.argv[1] )

factors = [1]
#starting factor
x=2 

print "number to start with:", numx

while x<=numx:
    rem = numx % x
    if rem == 0:
        factors.append(x)
        numx = numx/x 
    else:
        x+=1


print "factors:", factors
print "largest prime factor:", max(factors)
