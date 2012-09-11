#!/usr/bin/python

import math
import random

# -max_num to +max_num is the range to check for a and b
max_num = 1000


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


# This evaluates the quadratic formula using the given arguments. This
# would probably be quicker if inlined, but I separated it out for
# clarity's sake.
def eval_quadratic(n, a, b):
    return n**2 + a * n + b


# This determines how long a chain of primes the quadratic formula
# makes, with the a and b given as args.
def num_primes_produced(a, b):

    #this stores the length of the chain.
    count = 0

    #iterate n from 0 up
    for n in range(100):
        #evaluate the quadratic formula with the current n
        curr_num = eval_quadratic(n,a,b)

        #if it's bigger than 2 and prime
        if curr_num >= 2 and is_probably_prime(curr_num):
            #increase the counter
            count += 1
        # otherwise
        else:
            # return how long a chain we got
            return count

    #return how long a chain we got.
    return count


# This method iterates over all possible a and b values, and finds the
# max one.
def naive_brute_force(number_range):

    #for storing details about the max.
    max_primes = -1
    max_primes_a = "unassigned"
    max_primes_b = "unassigned"

    #iterate all values of a
    for a in range(-number_range, number_range + 1):
        print a
        #iterate all values of b.
        for b in range(-number_range, number_range + 1):
            #see how long a prime chain we get with the current a and b
            curr_num = num_primes_produced(a, b)

            #if it's bigger than the current max
            if curr_num > max_primes:
                #replace the current max
                max_primes = curr_num
                max_primes_a = a
                max_primes_b = b

    #return the biggest.
    return max_primes, max_primes_a, max_primes_b


# A much faster algorithm than brute force. The quadratic formula only
# produces primes when b is prime (consider n = 0), so we only need to
# check the cases where b is a prime number.
def smart_brute_force(number_range):

    #stores the max information
    max_primes = -1
    max_primes_a = "unassigned"
    max_primes_b = "unassigned"

    #loop b through all 6k from 6 to 1000 (since primes are always of
    #the form 6k +/- 1).
    for b in range(6, number_range+1, 6):

        #check how long a prime chain b - 1 produces and store the max
        #if it's bigger than what we've got.
        if is_probably_prime(b-1):
            print b-1
            
            for a in range(-number_range, number_range + 1):
                curr_num = num_primes_produced(a, b-1)
                if curr_num > max_primes:
                    max_primes = curr_num
                    max_primes_a = a
                    max_primes_b = b-1

        #and how long a prime chain b + 1 makes. store the max if
        #bigger.
        if is_probably_prime(b+1):
            print b+1
            
            for a in range(-number_range, number_range + 1):
                curr_num = num_primes_produced(a, b+1)
                if curr_num > max_primes:
                    max_primes = curr_num
                    max_primes_a = a
                    max_primes_b = b+1

    # return the biggest chain found.
    return max_primes, max_primes_a, max_primes_b, max_primes_a * max_primes_b


# seed the random number generator, since fermat primality testing
# relies on random numbers.
random.seed()

#print naive_brute_force(max_num)
print smart_brute_force(max_num)
