#!/usr/bin/python

import math

def first_fib_num_of_length_n(length):
    curr_num = -1
    old_1 = 1
    old_2 = 1
    curr_term = 2

    while len(str(curr_num)) != length:
        #print curr_term, curr_num
        curr_num = old_1 + old_2
        old_2 = old_1
        old_1 = curr_num
        curr_term += 1
        #print curr_num

    return curr_term

print first_fib_num_of_length_n(1000)
