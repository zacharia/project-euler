#!/usr/bin/python

import math
import random


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


# this does fermat primality testing on n, for k iterations. I adapted
# this algorithm from the pseudocode on wikipedia for fermat primality
# testing.
def fermat_primality_test(n, k):
    if n == 1:
        return False
    
    for i in range(k):
        a = random.randint(1, n - 1)
        if pow(a, n-1, n) != 1:
            return False
    return True


# A convenience shortcut to the fermat primality testing method
# above. Uses 32 passes as the default.
def is_probably_prime(num):
    return fermat_primality_test(num, 32)


# this method finds the largest n-digit pandigital prime. It's
# basically a culled and optimized brute force, which tries all
# possible permutations.
def get_largest_pandigital_prime():

    # this stores candidates for the largest prime.
    candidates = []
    
    # loop over the possible values of n (from the largest (9) down to
    # the smallest (1))
    for i in reversed(range(1, 10)):
        # get the current candidate digits (i.e. 1..n) from the digits
        # variable, above.
        curr_digits = digits[:i]
        print curr_digits
        # now, go through all of those digits
        for j in reversed(range(len(curr_digits))):
            # if the current digit is a valid end digit for a prime
            # (i.e. odd and not 5)
            if curr_digits[j] in ("1", "3", "7", "9"):
                # make a note of that digit
                curr_end_digit = curr_digits[j]
                # and all the other digits except that digit
                curr_other_digits = curr_digits[:j] + curr_digits[j+1:]

                print curr_end_digit, curr_other_digits

                # now go through all permutations of the other digits
                for k in reversed(range(1, math.factorial(len(curr_other_digits)))):
                    curr_num = int(fast_nth_perm(curr_other_digits, k) + curr_end_digit)
                    # if the current number is prime
                    if is_probably_prime(curr_num):
                        #add it to candidates
                        print "prime found: ", curr_num
                        candidates.append(curr_num)

        # once we've got one or more candidates, and have tried all
        # numbers of the current length, we can quit
        if len(candidates) > 0:
            break

    # return the biggest candidate
    return max(candidates)
                    
# seed the prng for fermat primality testing
random.seed()

#get the answer
print get_largest_pandigital_prime()
