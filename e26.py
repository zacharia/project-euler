#!/usr/bin/python

import math


# I adapted this algorithm from wikipedia's page on cyclic numbers:
# en.wikipedia.org/wiki/Cyclic_number
#
# It generates the first num_digits decimal numbers of 1 / N using
# long division.
def generate_unit_fraction_decimal_places(num, num_digits):
    b = 10
    p = num
    t = 0
    r = 1
    n = 0

    #this stores the numbers created so far
    ret = ""

    #until we hit the desired number of decimal places
    while len(ret) < num_digits:

        # do long division to get the next decimal number
        t += 1
        x = r * b
        d = x / p
        r = x % p
        n = n * b + d

        #add it to ret
        ret = "%s%s" % (ret, d)

    #return the decimal places (as a string).
    return ret


# This finds the cycle in a string, using hare and tortoise, and
# returns the length of the cycle (only, not any other information
# about it).
#
# This code is adapted from the hare and tortoise code given on the
# wikipedia page on 'Cycle Detection'.
def find_cycle_length(string):

    #initialize the hare and tortoise
    hare_pos = 2
    tortoise_pos = 1

    # run them, checking not just the current positions, but also
    # neighbouring ones (in case of the numbers coincidentally being
    # the same but not actually at the start of a cycle). I found that
    # checking the last two was enough, but this might not hold for
    # numbers > 1000.
    while string[hare_pos] != string[tortoise_pos] or string[hare_pos-1] != string[tortoise_pos-1] or string[hare_pos-2] != string[tortoise_pos-2]:
        tortoise_pos += 1
        hare_pos += 2

    # the difference between their positions is the length of the
    # cycle.
    return hare_pos - tortoise_pos


# this finds the number, N, with the longest recurring cycle in the
# decimal representation of 1 / N.
def find_longest_recurring_cycle(num):

    #these store the max length and what number generates it.
    max_length = -1
    max_num = -1

    # Check the length of the cycles of all eligible unit fractions.
    #
    # This only needs to check every prime number, but I haven't
    # implemented only checking them, instead, it only checks each odd
    # number, which makes it twice as fast for much less effort than
    # generating a sieving system to only check primes.
    for i in range(3, num+1, 2):

        # get the decimal places.
        curr_num = generate_unit_fraction_decimal_places(i, 2000)

        #find the cycle length
        curr_length = find_cycle_length(str(curr_num))

        #display it to assist in progress feedback
        print i, curr_length

        #if it's bigger than what we've found before, record it.
        if curr_length >= max_length:
            max_length = curr_length
            max_num = i

    # Display the number, cycle length and decimal places of the
    # biggest.
    print max_num, max_length
    print generate_unit_fraction_decimal_places(max_num, 2000)


find_longest_recurring_cycle(999)
