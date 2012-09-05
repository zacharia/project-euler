#!/usr/bin/python

from math import *

ans = 0

for a in range(1,1000):
    #print a
    for b in range(a,1000):
        #b = 500 - a
        for c in range(b,1000):
            if a + b + c == 1000 and a**2 + b**2 == c**2:
                ans = a * b * c
                print a,b,c
                print ans
            
