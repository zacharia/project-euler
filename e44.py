#!/usr/bin/python

import math
import random
import copy

# this global list stores the first N pentagonal_numbers. I figured
# it'd be quicker to store them than to recalculate them all the time.
pentagonal_numbers_list = []
# this set stores them for quicker lookup
pentagonal_numbers_set = set()


# this method generates the first N pentagonal_numbers and returns a
# list of them.
def generate_first_n_pentagonal_nums(n):
    ret_list = []
    ret_set = set()

    for i in range(1,n+1):
        curr_num = i * (3 * i - 1) / 2
        ret_list.append(curr_num)
        ret_set.add(curr_num)

    return ret_list, ret_set


# This finds the minimum. It's probably not the most efficient way,
# but it's better than a naive brute force.
def find_min_pentagonal_diff(pn_list, pn_set):
    # this stores the running minimum we've found so far
    min_diff = 999999999
    min_index1 = -1
    min_index2 = -1

    # iterate i from the first to the second last element
    for i in range(len(pn_list)-1):

        # indicates progress
        if i % 100 == 0:
            print i, "/", len(pn_list)

        # this is used for terminating the search early.
        exit_loop = False
        
        # iterate j from i to the end of the list (i.e. compare all
        # pairs of the elements in the list)
        for j in range(i+1, len(pn_list)):
            #print pn_list[i], pn_list[j]

            #calculate the current difference between the elements
            curr_diff = pn_list[j] - pn_list[i]

            #if the difference is a pentagonal number
            if curr_diff in pn_set:

                #then calculate the sum
                curr_sum = pn_list[j] + pn_list[i]

                # if the sum is pentagonal
                if curr_sum in pn_set:

                    #we've found a candidate
                    print "found candidates! they are: ", pn_list[i], pn_list[j]
                    print "their difference is: ", curr_diff

                    # make a note of the candidate
                    min_index1 = i
                    min_index2 = j
                    min_diff = curr_diff

                    #stop searching
                    exit_loop = True
                    break

        # this is for stopping searching early
        if exit_loop:
            break

    # now we've found x1 and x2, such that P(x1) +/- P(x2) is
    # pentagonal. However, there may be smaller valid answer pairs in
    # the range (x1,x2), so we need to check for them.

    # loop i from x1 to x2-1
    for i in range(min_index1, min_index2-1):
        # and loop j from i+1 to x2
        for j in range(i+1, min_index2):
            # work out the difference between the ith and jth
            # pentagonal numbers.
            curr_diff = pn_list[j] - pn_list[i]
            # if it's smaller than our current candidate and is
            # pentagonal
            if curr_diff < min_diff and curr_diff in pn_set:
                # get the sum of the numbers
                curr_sum = pn_list[j] + pn_list[i]
                # if the sum's pentagonal
                if curr_sum in pn_set:
                    # update and display our current minimum
                    print "found better candidates! they are: ", pn_list[i], pn_list[j]
                    print "their difference is: ", curr_diff
                    min_index1 = i
                    min_index2 = j
                    min_diff = curr_diff


# pre-calculate all the pentagonal_numbers, as both a list and a set
pentagonal_numbers_list, pentagonal_numbers_set = generate_first_n_pentagonal_nums(5000)

# work out the answer
find_min_pentagonal_diff(pentagonal_numbers_list, pentagonal_numbers_set)
