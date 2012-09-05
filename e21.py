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


def get_sopd_list_up_to(num):
    nums = [i for i in range(1, num)]

    for i in range(len(nums)):
        nums[i] = sum_of_proper_divisors(nums[i])
    
    return nums


def get_amicable_numbers(num_list):
    return_list = set()

    i_counter = 1
    for i in num_list:
        print i_counter
        j_counter = 1
        for j in num_list:
            if j_counter != i_counter and i_counter == j and j_counter == i:
                return_list.add(i)
            j_counter += 1
        
        i_counter += 1

    return return_list


print sum(get_amicable_numbers(get_sopd_list_up_to(10000)))

print 4 in [4, 5, 5, 3, 4]
