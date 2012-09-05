#!/usr/bin/python

from math import *

num1 = 999
num2 = 999

def is_palindrome(num):
    num_string = str(num)
    half_length = int(ceil(len(num_string) / 2.0))
    for i in range(0, half_length):
        #print "%d: does %c == %c?" % (i, num_string[i], num_string[len(num_string) - i - 1])
        if num_string[i] != num_string[len(num_string) - i - 1]:
            return False
    return True

curr_num = num1 * num2
curr_biggest = -1

for i in reversed(range(1,num1+1)):
    for j in reversed(range(1,num2+1)):
        curr_num = i * j
        if is_palindrome(curr_num) and curr_num > curr_biggest:
            curr_biggest = curr_num

print curr_biggest
