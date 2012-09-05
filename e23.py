#!/usr/bin/python

import math


def factorize(num):
    factors = set()
    num_sqrt = int(math.ceil(math.sqrt(num)))
    
    for i in range(1, num_sqrt+1):
        if num % i == 0:
            #print "%d divides %d!" % (i, num)
            factors.add(i)
            factors.add(num / i) #if this line is included, it gets all factors, not just the prime ones
            
    return factors


def get_proper_divisors(num):
    factors = set()
    num_sqrt = int(math.ceil(math.sqrt(num)))
    
    for i in range(1, num_sqrt+1):
        if num % i == 0:
            #print "%d divides %d!" % (i, num)
            factors.add(i)
            factors.add(num / i) #if this line is included, it gets all factors, not just the prime ones

    factors.remove(num)
            
    return factors


def sum_of_proper_divisors(num):
    return sum(get_proper_divisors(num))


def is_abundant(num):
    if sum_of_proper_divisors(num) > num:
        return True
    else:
        return False

    
def get_abundant_numbers_up_to(num):
    results = []

    for i in range(12, num+1):
        if is_abundant(i):
            results.append(i)

    return results


#here's a better way, pre-calculate it. This is much faster
def get_all_sums_of_abundant_nums(list_of_abundants):
    results = set()

    for i in list_of_abundants:
        print i
        for j in list_of_abundants:
            results.add(i + j)

    return results


def sum_of_ints_not_equal_to_sum_of_abundants(lower, upper, all_sums):
    total = 0
    
    for i in range(lower, upper+1):
        if i % 1000 == 0:
            print i
        if i not in all_sums:
            total += i

    return total


loa = get_abundant_numbers_up_to(28200)
all_sums = get_all_sums_of_abundant_nums(loa)

print sum_of_ints_not_equal_to_sum_of_abundants(1, 28123, all_sums)

