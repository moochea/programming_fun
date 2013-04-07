#!/usr/bin/env python

# This script finds the total of all the even numbers in the fibonacci sequence up to and less than max_num
values = []
total = 0

max_num=4000000

num1 = 1
num2 = 2


while num2< max_num:
    if (num2%2==0):
        values.append(num2)
        total +=num2
    num3 = num2+num1
    num1 = num2
    num2 = num3


print values
print total
