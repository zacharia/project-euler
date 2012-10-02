#!/usr/bin/python

import math
import random
import copy


#store the digits we want to pandigital about as a string
digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# This method checks whether a number (expressed as a list of digits)
# meets the requirements laid out in the question, and returns
# True/False.
def num_meets_requirements(num):
    return int("%d%d%d" % tuple(num[1:4])) % 2 == 0 and\
        int("%d%d%d" % tuple(num[2:5])) % 3 == 0 and\
        int("%d%d%d" % tuple(num[3:6])) % 5 == 0 and\
        int("%d%d%d" % tuple(num[4:7])) % 7 == 0 and\
        int("%d%d%d" % tuple(num[5:8])) % 11 == 0 and\
        int("%d%d%d" % tuple(num[6:9])) % 13 == 0 and\
        int("%d%d%d" % tuple(num[7:10])) % 17 == 0


# I got this algorithm from wikipedia. Given a permutation of a
# sequence as input, it produces the next lexicographical permutation
# after the given one. It seems to work perfectly
def get_next_perm(curr_perm):
    # this algorithm works in place, so make a copy
    new_perm = curr_perm

    # find the largest k such that a[k] < a[k+1]
    k = len(curr_perm) - 2
    while k > 0 and new_perm[k] >= new_perm[k+1]:
        k -= 1

    # if we don't find such a k, we've been given the max perm, so
    # return it. We can't go anywhere from here
    if k < 0:
        return curr_perm

    # find the largest l such that a[k] < a[l]
    l = len(curr_perm) - 1
    while l > 0 and new_perm[k] >= new_perm[l]:
        l -= 1

    # swap a[k] and a[l]
    temp = new_perm[k]
    new_perm[k] = new_perm[l]
    new_perm[l] = temp

    # reverse the sequence from a[k+1] to the final element a[n]
    new_perm[k+1:] = reversed(new_perm[k+1:])

    # return the new permuation
    return new_perm


# This method iterates through all permutations of the digits 0 - 9
# and finds those that meet the question's requirements.
def get_special_pandigital_nums():
    # A set to store the numbers that match
    nums = set()
    # curr_perm stores the current permutation. Start with the digits
    # listed in ascending order.
    curr_perm = digits

    # go through each permuation (all 10! of them)
    for i in range(math.factorial(len(digits))):

        # to indicate progress
        if i % 100000 == 0:
            print i

        # if the number meets the requirements
        if num_meets_requirements(curr_perm):
            # output it
            thing = [str(i) for i in curr_perm]
            curr_perm_int = int("".join(thing))
            print "found one:", curr_perm_int
            # add it to the set
            nums.add(curr_perm_int)

        # update curr_perm to the next lexicographical permutation
        curr_perm = get_next_perm(curr_perm)

    return nums


# print the sum of the found numbers
print sum(get_special_pandigital_nums())
