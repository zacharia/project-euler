#!/usr/bin/python

import math
import random
import copy


# this determines if a number, X, is a triangle number or not. It
# works by determining if sqrt(1+8X) is an integer. For the reasoning
# on why it works, please see the comments in my solution to problem
# 42.
def is_triangle_num(num):
    value = math.sqrt(1 + 8 * num)
    return value - math.floor(value) == 0


# this determines if a number, X, is a pentagonal number or not. It
# works on the same principle as is_triangle_num() above, but with
# solving for the pentagonal number equation instead. It doesn't
# optimize down as neatly as the triangle number one does though,
# since the quadratic equation's denominator is 6.
def is_pentagonal_num(num):
    value = (1.0 + math.sqrt(1 + 24 * num)) / 6.0
    return value - math.floor(value) == 0


# this finds the smallest number larger than the Nth hexagonal number
# (N is the argument), which is triangle, pentagonal and hexagonal. It
# works by iterating over the hexagonal numbers and finding one that
# is triangle and pentagonal.
#
# The reason I iterate through the hexagonal numbers, not either of
# the others is because I believe hexagonal numbers grow more quickly
# than the other two (2n^2 insteaad of 0.5n^2 or 1.5n^2). Hence, we
# should theoretically hit the next minimum quicker going through the
# hexagonal numbers than through the other two.
def find_smallest_tph_num(min_index):

    #curr index stores the index of the hexagonal number we're
    #currently at.
    curr_index = min_index + 1

    # until we find our answer
    while True:
        #calculate the next hexagonal number
        curr_num = curr_index * (2 * curr_index - 1)

        if curr_index % 10000 == 0:
            print curr_index, curr_num

        # if it's also pentagonal and triangle
        if is_pentagonal_num(curr_num) and is_triangle_num(curr_num):
            # return it, it's the answer
            return curr_num

        #otherwise, move on to the next hexagonal number
        curr_index += 1


# get the answer, starting at the 143rd hexagonal number
print find_smallest_tph_num(143)
