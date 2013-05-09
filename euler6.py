#!/usr/bin/env python

#Euler problem number 6

#Sum of squares

import sys

def sum_square(end_value):
    final_sum = 0
    for x in range(1,end_value+1):
        final_sum+=(x*x)
    return final_sum

def square_sum(end_value):
    final_sum=0
    for x in range(1, end_value+1):
        final_sum+=x
    return (final_sum*final_sum)
    


if __name__ == '__main__':


    ssq= sum_square(int(sys.argv[1]))
    sqs= square_sum(int(sys.argv[1]))

    print "Square of the sum from 1 to %d is %d" % (int(sys.argv[1]), sqs)
    print "sum of the squares from 1 to %d is %d" % (int(sys.argv[1]), ssq)
    
    print "different sqs - ssq is", sqs-ssq
