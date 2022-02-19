#!/usr/bin/env python


import sys
import math

def generate_primes(max_prime):
    current_val = 3
    primes = [2]
    add_to_list = 1
    while current_val<=max_prime:
        marker = math.ceil(current_val/3.0)
        for x in primes:
            if x<=marker:
                if (current_val%x == 0):
                    add_to_list = 0
                    break
            else:
                break
        if add_to_list == 1:
            primes.append(current_val)
        current_val+=1
        add_to_list=1
        #print current_val
    return primes

if __name__ == "__main__":
    newprimes = generate_primes(int(sys.argv[1]))
    #print newprimes
    print sum(newprimes)
