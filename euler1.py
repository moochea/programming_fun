#!/usr/bin/env python

values = []
total = 0

max_num=1000

for x in range(0,max_num):
    if (x%3 == 0) or (x%5==0):
        values.append(x)
        total+=x

print values
print total
