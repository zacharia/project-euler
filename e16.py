#!/usr/bin/python

from math import *

num = 2**1000

total = 0
for i in str(num):
    total += int(i)

print total
