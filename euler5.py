#!/usr/bin/env python

def find_factors(multiple):
    #Write a funciton here that reduces a multiple to its simplest factors
    factors = []
    divisor = 2
    quotient = multiple
    while (quotient>=divisor):
        result = quotient % divisor
        if result ==0:
            factors.append(divisor)
            quotient = quotient/divisor
        else:
            divisor+=1
    return factors

print find_factors(2520)

def test_factors(multiple,factor):
    if multiple%factor == 0:
        return True
    else:
        return False

# For each value from 2-20:
# find the factor of that number
# Ensure that all factors reside in the list of factors for the multiple. If not, add
# In the end, find the product of all facotrs

factors = {}

for x in range(2,20):
    values = find_factors(x)
    values_dict = {}
    for z in values:
        values_dict[z] = values.count(z)
    for y in values_dict:
        if y in factors:
            if factors[y]<values_dict[y]:
                factors[y]=values_dict[y]
        else:
            factors[y] = values_dict[y]

print factors

answer = 1
for x in factors:
    answer=answer*(x**factors[x])

print answer

