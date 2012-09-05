#!/usr/bin/python

from math import *

def sum_of_digits(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total

print sum_of_digits(factorial(100))
