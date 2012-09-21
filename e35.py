#!/usr/bin/python

import math
import random


# this does fermat primality testing on n, for k iterations. I adapted
# this algorithm from the pseudocode on wikipedia for fermat primality
# testing.
def fermat_primality_test(n, k):
    for i in range(k):
        a = random.randint(1, n - 1)
        if pow(a, n-1, n) != 1:
            return False
    return True


# A convenience shortcut to the fermat primality testing method
# above. Uses 32 passes as the default.
def is_probably_prime(num):
    return fermat_primality_test(num, 32)


#returns true if a number is circularly prime, false if not.
def is_circular_prime(num):

    #first convert the number into a list, by making it a string first.
    string_num = str(num)
    list_num = []
    for i in string_num:
        list_num.append(i)
        
    curr_num = list_num

    # iterate (num digits) - 1 times
    for i in range(len(list_num)-1):
        # shift the number's digits left (wrapping around)
        curr_num.append(curr_num.pop(0))

        # if the current circulation isn't prime
        if not is_probably_prime(int("".join(curr_num))):
            # return False
            return False

    # if we've got this far, it must be a circularly prime number
    return True


#this finds all circular primes <= num. It does the old 6k +/- 1 trick
#to cut down on the numbers that need to be checked.
def get_circular_primes_under(num):
    #stores the found numbers
    ret = []

    #since the 6k trick doesn't apply to 2 and 3, add them here
    #manually. Assumes the number is >= 3, which is a fair assumption.
    ret.append(2)
    ret.append(3)

    #loop through all 6k
    for i in range(6, num+1, 6):

        # just a little progress indication
        if i % 6000 == 0:
            print i

        # loop through -1 and +1
        for j in [-1, 1]:
            # if 6k +/- 1 is prime and circularly prime
            if is_probably_prime(i+j) and is_circular_prime(i+j):
                # add it to the list
                ret.append(i+j)

    return ret


# this finds all circular primes <= num, but does so via sieving
# instead of the 6k +/- 1 thing. It's significantly faster, but uses
# much more memory.
def get_circular_primes_under_sieving(num):
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

    print "circular prime finding"

    # now go through all the prime numbers that we sieved
    for i in range(2, num+1, 1):

        if i % 100000 == 0:
            print i

        # and if they're circular primes
        if sieve[i] and is_circular_prime(i):
            # add them to the list
            ret.append(i+j)

    return ret


# seed the random number generator, since fermat primality testing
# relies on random numbers.
random.seed()

upper_limit = 10**6
#upper_limit = 10**7

#circular_primes = get_circular_primes_under(upper_limit)
circular_primes = get_circular_primes_under_sieving(upper_limit)
print circular_primes
print "number of circular primes is: ", len(circular_primes)
