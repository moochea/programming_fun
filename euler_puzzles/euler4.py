#!/usr/bin/env python

#This script finds the largest 6 digit palindrom which is a multiple of two 3 digit factors

# palindrom x*x = number where number is the same read back and forth
# abccba

# Check for palindrome:
# 6 digit number: num abcdef

def check_palindrome(num):
    numstr=str(num)
    first= numstr[0:3]
    last = numstr[3:]
    last_sorted = last[2] + last[1] + last[0]
    return last_sorted == first

# Check palindromes which are 6 digit numbers, from 100001 to 999999?
# Looking for largest, start from 999999

x1=999
x2=999
newvalue=580085

print newvalue

while x1>100:
    result = x1*x2
#    print "%d * %d = %d " % (x1,x2,result)
    if result > newvalue:
        if check_palindrome(result):
            newvalue = result
            print newvalue
            x2=999
            x1-=1
        else:
            if x2>101:
                x2-=1
            else:
                x2=999
                x1-=1
    else:
        x2=999
        x1-=1


