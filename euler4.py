#!/usr/bin/env python

import sys


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


#Adding more crap   
