#!/usr/bin/python

import math


# this method finds the value of p (<= 1000) for which there are the
# most solutions to the equations a + b + c = p and a^2 + b^2 = c^2.
#
# This is a brute force approach with some minor optimizations. I'm
# sure there's a faster way to do it, but I don't know it.
def find_max_p_slow():

    #these variables store details about the running maximum
    max_p = -1
    max_p_count = -1

    # try every even value of p. We know that p can't be odd.
    for p in range(2, 1000+1, 2):
        print p

        #this stores the number of valid right angle triangles we can
        #get from the current p
        curr_p_count = 0

        # loop all values of c
        for c in range(1,p):
            # work out what a + b is equal to
            a_b_total = p - c

            # then loop through the values of a and b, cleverly in one
            # loop, since they're in a linear relationship to each
            # other.
            for a in range(1, a_b_total):
                b = a_b_total - a

                # if the current a,b and c all check out
                if a**2 + b**2 == c**2:
                    # increase our counter
                    curr_p_count +=1 

        # update the max if necessary.
        if curr_p_count > max_p_count:
            max_p_count = curr_p_count
            max_p = p

    # return the max found
    return max_p, max_p_count


print find_max_p_slow()

