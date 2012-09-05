#!/usr/bin/python

from math import *

def is_prime_naive(num):
    num_sqrt = int(ceil(sqrt(num)))
    for i in range(2,num_sqrt+1):
        if num % i == 0:
            return False    
    return True


def sum_of_primes(num):
    curr_num = 0
    total = 5 #to account for 2 and 3

    while curr_num < num:
        if curr_num % 1000 == 0:
            print curr_num,total
        curr_num += 6
        if curr_num - 1 < num and is_prime_naive(curr_num - 1):
            total += curr_num - 1
        if curr_num + 1 < num and is_prime_naive(curr_num + 1):
            total += curr_num + 1
        
    return total

print sum_of_primes(2000000)
