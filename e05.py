#!/usr/bin/python

from math import *

def gcd(num1, num2):
    a = num1
    b = num2
    while b != 0:
        t = b
        b = a % b
        a = t
    return a

def lcm(a, b):
    return (a * b) / (gcd(a,b))

def get_lowest_num(num):
    result = 1
    for i in range(2,num+1):
        result = lcm(result,i)
    return result

print get_lowest_num(20)
