#!/usr/bin/python

from math import *

def sum_of_squares(num):
    total = 0
    for i in range(1,num+1):
        total += (i * i)
    return total

def square_of_sum(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total * total

def diff(num):
    return square_of_sum(num) - sum_of_squares(num)

print diff(100)
