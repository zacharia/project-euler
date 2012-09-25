#!/usr/bin/python

import math


#store the digits we want to pandigital about as a string
digits = "123456789"


#a faster method to compute the desired permutation without iterating
#through all the possibilities. It generates the permutation directly.
def fast_nth_perm(digits, n):

    #temporary storage variables
    curr_num = n - 1
    result = ""

    #go through the digits from the biggest down (i.e. 9 to 0)
    for i in reversed(range(len(digits))):
        #do integer division to get the quotient of curr_num / i!
        quotient = curr_num / math.factorial(int(i))
        #also get the remainder with mod
        remainder = curr_num % math.factorial(int(i))

        #the quotient is the index of the current digit in the desired
        #permutation. Add it to the result.
        result += (digits[quotient])
        # and remove it from the list of digits (each digit can only
        # appear once)
        digits = "%s%s" % (digits[:quotient], digits[quotient+1:])

        #update curr num to be the remainder of the previous
        #curr_num's division.
        curr_num = remainder
        
    return result


# this finds the largest 1-9 pandigital 9-digit number that can be
# formed as the concatenated product of an integer (X) with 1,2...n (n
# > 2).
#
# It works by iterating through the permutations of 1..9 from
# 987654321 down to 123456789. For each number it checks whether the
# number can be made as a concatenated product. Since the first b
# digits must be the number itself (i.e. X multiplied by 1, which is
# X), we can just consider the numbers formed from the first b digits,
# where b is in the range 1..5.
def get_largest_pandigital_concatenated_product():

    # loop through all the permutations from the biggest down
    for i in reversed(range(1, math.factorial(9)+1)):
        # calculate the current permutation
        curr_permutation = fast_nth_perm(digits, i)
        # convert it to a string
        curr_permutation_string = str(curr_permutation)
        
        # try various values of b (1 to 5 in this case)
        for j in range(1,6):

            # turn the first b (j in this case) digits into a number
            curr_num = int(curr_permutation_string[0:j])

            # this stores the concatenated product of curr_num and
            # 1,2,..n
            concatenated_product = ""

            # now form the concatenated product of curr_num
            for k in range(1,5):
                concatenated_product += str(curr_num * k)

                # if the current concatenated product is 9 digits long
                # and equals the current permutation, we've found the
                # biggest.
                if len(concatenated_product) == 9 and concatenated_product[0:9] == curr_permutation_string:
                    return curr_num, curr_permutation_string
                

# get the answer and print it.
print get_largest_pandigital_concatenated_product()
