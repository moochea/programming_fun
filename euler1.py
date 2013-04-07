#!/usr/bin/env python

# This script finds the total of all the numbers between 0 and max_num which are evenly divisible by 3 and/or 5

values = []
total = 0

max_num=1000

for x in range(0,max_num):
    if (x%3 == 0) or (x%5==0):
        values.append(x)
        total+=x

print values
print total
