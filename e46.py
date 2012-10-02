#!/usr/bin/python

import math
import random


# this method uses the sieve of eratosthenes to generate all the
# primes up to N. It returns an array, A, where, A[i] is True for
# primes and False for composite numbers.
def get_primes_up_to_n_sieve_of_eratosthenes(num):

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

    return sieve


# this method take the array made by the sieve of eratosthenes, and
# changes it so that the entry for composite numbers is the index of
# the next smallest prime. This is used to speed up the search later.
def process_table(table):
    last_prime = 2
    for i in range(2, len(table)):
        if table[i]:
            last_prime = i
        else:
            table[i] = last_prime


# this method makes a set() of all the square numbers up to num. I
# figure that storing the square numbers ahead of time will be quicker
# than determining if a difference is a square number later. That
# might not be true, but it's good enough for the purposes of this
# exercise.
def make_set_of_squares(num):
    # this stores the index of the current square number.
    curr_num = 0
    # this set stores all the square numbers we make
    square_nums = set()

    # until we get into square numbers that are bigger than num.
    while curr_num**2 < num:
        # advance to the next square number
        curr_num += 1
        # add it to the set.
        square_nums.add(curr_num**2)

    return square_nums


# this method determines whether a number can be written as the sum of
# a prime and twice a square number. It uses the prime and square
# tables to accelerate computation.
def num_meets_requirements(num, prime_table, square_table):

    # find the biggest prime smaller than num from the table
    curr_prime = prime_table[num]

    # try all the primes less than the number
    while curr_prime >= 2:
        # if half the number minus that prime is a square number
        if (num - curr_prime) / 2 in square_table:
            # this number works
            return True

        # otherwise, try the next smaller prime
        curr_prime = prime_table[curr_prime-1]

    # if none of the primes work for this number, it disproves the
    # conjecture.
    return False


# this method determines the smallest odd composite number that can't
# be written as the sum of a prime and twice a square number.
def find_answer(prime_table, square_table):

    # go through the odd numbers in the prime table
    for i in range(9, len(prime_table), 2):

        if i % 101 == 0:
            print i

        # if it's a prime number, skip it
        if prime_table[i] == True:
            continue

        # if we find a number that doesn't meet the requirements,
        # we've found the answer.
        if not num_meets_requirements(i, prime_table, square_table):
            print "found it! It is: ", i
            return
        

# the biggest number to try up to. Used to stop infinite execution
max_num = 10000
# create a sieve of eratosthenes.
sieve = get_primes_up_to_n_sieve_of_eratosthenes(max_num)
# process the sieve so that composite numbers store the index of the
# biggest prime smaller than them
process_table(sieve)
# make a set of all the square numbers up to max_num
squares =  make_set_of_squares(max_num)

# use all the above stuff to find the answer
find_answer(sieve, squares)
