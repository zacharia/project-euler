#!/usr/bin/python

import math
import random


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


#returns true if a number is a truncatable prime, false if
#not. Assumes the number is already prime.
def is_truncatable_prime(num):
    
    #check the number in one direction
    
    curr_num = str(num)
    # until we've checked all the digits in one direction
    while len(curr_num) > 0:
        #if the stripped number isn't prime
        if not is_probably_prime(int(curr_num)):
            # this is not a truncatable prime
            return False

        #strip off a digit
        curr_num = curr_num[1:]
        
    #check the number in the other direction, as above but taking
    #digits off the other end.
        
    curr_num = str(num)
    while len(curr_num) > 0:
        if not is_probably_prime(int(curr_num)):
            return False
        #take a digit off the other end
        curr_num = curr_num[0:len(curr_num)-1]

    #if we've got to this point, it must be a truncatable prime.
    return True


# this finds all truncatable primes <= num, but does so via sieving
# and checking all primes numbers it finds for truncatability. The
# brute force approach.
def get_truncatable_primes_under_sieving(num):
    #stores the found numbers
    ret = []

    # this array stores the sieve. Initially everything is prime.
    sieve = [ True for i in range(num+1) ]

    print "sieving"

    # loop up to the square root of the upper limit
    for i in range(2, int(math.ceil(math.sqrt(num)))):

        if i % 100 == 0:
            print i

        #if the current number is prime
        if sieve[i] == True:
            #then make all of it's factors non-prime
            for j in range(i**2, num+1, i):
                sieve[j] = False

    print "truncatable prime finding"

    # now go through all the prime numbers that we sieved
    for i in range(11, num+1, 1):

        if i % 100000 == 0:
            print i

        # and if they're truncatable
        if sieve[i] and is_truncatable_prime(i):
            # add them to the list
            ret.append(i)

    return ret


# a much more intelligent way of finding the truncatable primes. Start
# with 2, 3, 5, 7, and 9 and add odd digits to them, stopping when the
# result stops being prime.
#
# Then check the numbers we got through that approach in the other
# direction, to ensure they are truncatable primes.
def find_truncatable_primes():

    # this array stores the candidate numbers we're generating. It
    # starts with 2, 3,5,7 and 9.
    candidates = [2,3,5,7,9]
    # this set stores the right to left truncatable primes that we
    # find.
    rl_truncatable_primes = set()

    #until we're out of candidates.
    while len(candidates) > 0:

        # make an array to store the new candidates that we find in
        # this round.
        new_candidates = []

        # loop through each of the current candidates.
        for i in candidates:
            # loop through each odd digit
            for j in [1,3,5,7,9]:
                #try adding each odd digit to the current candidate
                curr_num = int(str(i) + str(j))

                #if adding it gives us a new prime number
                if is_probably_prime(curr_num):
                    # add the new number to new_candidates
                    new_candidates.append(curr_num)
                # otherwise
                else:
                    # if the old number was longer than one digit
                    if len(str(i)) > 1:
                        # add it to the set of right to left
                        # truncatable primes.
                        rl_truncatable_primes.add(i)

        # replace candidates, with the new candidates we found in this
        # round.
        candidates = new_candidates

    #this stores the actual truncatable primes (truncatable l->r and
    #r->l)
    truncatable_primes = set()

    # go through all of the r->l truncatable primes
    for i in rl_truncatable_primes:
        # if it's also truncatable the other way
        if is_truncatable_prime(i):
            # add it to the set of fully truncatable primes
            truncatable_primes.add(i)

    # return the set of fully truncatable primes.
    return truncatable_primes


# seed the random number generator, since fermat primality testing
# relies on random numbers.
random.seed()

# an upper limit for the sieving approach.
upper_limit = 10**6

# # The slower, sieving approach to finding the truncatable primes
# truncatable_primes = get_truncatable_primes_under_sieving(upper_limit)
# print truncatable_primes
# print "sum of truncatable primes is: ", sum(truncatable_primes)

# the smarter approach to finding the truncatable primes
truncatable_primes =  find_truncatable_primes()
print truncatable_primes
print "the sum is: ", sum(truncatable_primes)
