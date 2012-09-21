#!/usr/bin/python

import math

#determines whether a number is equal to the sum of it's digits factorial.
def factorial_digits_equals_num(num):
    #get the sum of the digits factorial
    total = 0
    for i in str(num):
        total += math.factorial(int(i))

    # check if it's equal to the number
    return total == num


# this method finds all the numbers that are equal to the sum of their
# digits factorial, up to max_num.
def find_all_the_numbers(max_num):
    ret = []

    #loop through each number from 3 to max_num
    for i in range(3, max_num):

        #this gives some indication of progress
        if i % 10000 == 0:
            print i
            
        # if it meets the criteria, add it to ret
        if factorial_digits_equals_num(i):
            ret.append(i)

    return ret


#note that I determined the upper limit to go to here experimentally,
#by finding the first N digit number of all 9's, that was larger than
#the sum of it's digits factorial.
numbers = find_all_the_numbers(9999999)

print numbers
print sum(numbers)
