#!/usr/bin/python

max_size = 1000

total = 0

for i in range(1, max_size):
    if i % 3 == 0 or i % 5 == 0:
        print i
        total += i

print total
