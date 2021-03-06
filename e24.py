#!/usr/bin/python

import math
import copy

#store the digits as a string
digits = "0123456789"
# smaller set for testing
#digits = "0123"

#the index of the desired permutation
target_number = 1000000
#target_number = 4

#this returns all lexocigraphical (or however it's spelt) permutations
#of the digits given in sorted order. Assumes all the characters in
#the argument are unique
def permute(digits):
    
    if len(digits) == 1:
        #there's only one way to order one thing...
        return [ digits ]
    else:
        #...but N! to order N

        #call recursively on one fewer digits
        smaller_permutations = permute(digits[1:])

        #make an empty list to store the permutations we'll generate
        curr_permutations = []

        # go through each of the (N-1)! permutations
        for i in smaller_permutations:
            #and make N copies with the current digit in each possible
            #position.
            for j in range(len(digits)):
                curr_element = i
                curr_element = "%s%s%s" % (curr_element[:j], digits[0], curr_element[j:])
                curr_permutations.append(curr_element)

        #sort the permutations
        curr_permutations.sort()

        #and return them (all N! of them)
        return curr_permutations


# This is slightly more efficient method of getting the Nth
# permutation than pure brute force. It only generates the
# permutations that have to be manually calculated (e.g. if we want
# the 3rd out of 10000 permutations, we already know what some of the
# first digits will be).
#
# There's probably a more efficient way of generating the permutation
# directly, but I'm not sure what it is.
def get_nth_perm(digits, n):
    # if N is less than (number of digits - 1)!
    if n < math.factorial(len(digits)-1):
        # we know the first digit of the Nth permutation will be
        # digits[0], so recurse on digits[1:]
        return digits[0] + get_nth_perm(digits[1:], n)
    else:
        #otherwise, generate all the permutations
        perms = permute(digits)
        
        # and take the Nth.
        return perms[n-1]

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

# call the method to get our answer
#print get_nth_perm(digits, target_number)

#the faster algorithm
print fast_nth_perm(digits, target_number)
