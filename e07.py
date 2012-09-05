#!/usr/bin/python

from math import *
from random import *

def inefficient_num_primes_less_than(num):
    outer_sum = 0

    for j in range(1, num+1):
        inner_sum = 0
        for s in range(1,int(floor(sqrt(j))) + 1):
            inner_sum += ( floor((j - 1) / float(s)) - floor(float(j) / s) )
        
        outer_sum += floor( (2.0 / j) * (1 + inner_sum))

    return num - 1 + outer_sum

def inefficient_nth_prime(num):
    sum = 0

    sum_upper_count_val = 2 * ( int(floor(num * log(num))) + 1 )

    for k in range(1,sum_upper_count_val + 1):
        if k % 100 == 0:
            print "%d of %d" % (k, sum_upper_count_val)
        sum += (1 - floor(num_primes_less_than(k) / num) )

    return 1 + sum


def is_prime_naive(num):
    num_sqrt = int(ceil(sqrt(num)))
    for i in range(2,num_sqrt+1):
        if num % i == 0:
            return False    
    return True


def nth_prime_naive(num):
    primes_found = 0
    curr_num = -1

    while primes_found < num:
        curr_num += 2
        if is_prime_naive(curr_num):
            primes_found += 1
            if primes_found % 1000 == 0:
                print "prime %d found: %d" % (primes_found, curr_num)
        
    return curr_num


#meant to do miller-rabin primality test, but doesn't work, and I
#don't know why.
def is_prime_mr(n, k):
    assert(n > 3 and n % 2 != 0)
    #print "got input of: %d" % n

    n_sub_1 = n - 1
    #print "n - 1 = %d" % n_sub_1
    d = n_sub_1
    s = 0
    while d % 2 == 0:
        s += 1
        d = d / 2
        #print "d: %d and s: %d" % (d, s)

    for i in range(k):
        a = randint(2, n - 2)
        #print a
        x = a**d % n
        if x == 1 or x == n - 1:
            continue

        for r in range(1, s):
            x = x**2 % n
            if x == 1:
                return False
            if x == n - 1:
                break

        return False
        
    return True

def nth_prime_mr(num, k):
    primes_found = 3
    curr_num = 3

    while primes_found < num:
        curr_num += 2
        if is_prime_mr(curr_num, k):
            primes_found += 1
            #if primes_found % 1000 == 0:
                #pass
            print "prime %d found: %d" % (primes_found, curr_num)
        
    return curr_num



#print nth_prime_naive(345)

seed()

#number = 2**(32-1) + 1
#print "mr: %d" % is_prime_mr(number, 1)
#print "naive: %d" % is_prime_naive(number)

#print is_prime_mr(13, 10)

#for i in range(1,30):
#    print "%d: mr: %d | naive: %d" % (i, nth_prime_mr(i, 40), nth_prime_naive(i))

print nth_prime_naive(10001)
