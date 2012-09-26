#!/usr/bin/python

import math


# A much faster than brute force approach to getting the nth digit of
# the irrational number. It counts up in orders of magnitude, and then
# extracts the nth digit.
def get_nth_digit(n):
    # this is how many digits long the current numbers are (starts at
    # 1 for 1,2,..,9; then it's 2 for 10,11,..99; etc.)
    digit_length = 1
    # this is how many numbers of the current digit length there are
    # (9 for 1,2,..,9; 90 for 10,11,..,99; etc.)
    numbers_in_that_range = 9
    # this is the position of the first number in the irrational
    # number that has digit_length digits (1 for 1..9, 10 for 11..99,
    # etc.)
    start_of_range = 1
    # and this is the position of the last number with digit_length
    # digits (9 for 1..9, 189 for 10..99, etc.)
    end_of_range = 9

    # until our number range includes n. Once this is finished,
    # start_of_range < n < end_of_range.
    while end_of_range < n:
        # increase the digit length
        digit_length += 1
        # work out how many digits there are of that length (10 times
        # as many as for the previous one)
        numbers_in_that_range *= 10
        # work out the position of the first digit of the numbers with
        # the new number of digits.
        start_of_range = end_of_range + 1
        # also work out the end of the range
        end_of_range = end_of_range + (digit_length * numbers_in_that_range)

    # calculate the offset of the nth digit from the first digit of
    # the first number that shares the same number of digits as the
    # nth number.
    offset = n - start_of_range
    # work out what the actual number is that contains the nth digit.
    num_numbers_in = offset / digit_length
    # work out which digit of that number is the nth digit
    digit_of_number = offset % digit_length
    
    # then calculate that nth digit from the number and return it
    return int(str(10**(digit_length-1) + num_numbers_in)[digit_of_number])


# this method calculates the product of the desired digits of the
# irrational number.
def get_answer_product():
    product = 1
    for i in range(0, 7):
        product *= get_nth_digit(10**i)

    return product


print get_answer_product()
