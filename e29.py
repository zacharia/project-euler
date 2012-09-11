#!/usr/bin/python

import math


# this method returns how many unique numbers a^b produces for 2 <= a
# <= a_max, and 2 <= b <= b_max. It does this by generating all the
# numbers and using a set. This works because Python does arbitrary
# size integers natively.
#
# I'm sure there's a better way to work this out, but I don't know it.
def num_unique(a_max, b_max):

    # make an empty set to store the numbers. Use a set for log(n) /
    # O(1) lookups (whichever it is for python) and duplicate removal.
    numbers = set()

    # loop through all combinations of a and b
    for a in range(2, a_max + 1):
        for b in range(2, b_max + 1):
            # add the result of a^b to the set.
            numbers.add(a**b)

    # return the number of elements in the set.
    return len(numbers)

print num_unique(100, 100)
