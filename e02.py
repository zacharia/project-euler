#!/usr/bin/python

max_size = 4000000

i1 = 0
i2 = 1
curr = -1

total = 0

while curr < max_size:
    curr = i1 + i2
    i1 = i2
    i2 = curr
    
    if curr % 2 == 0:
        total = total + curr

print total
