#!/usr/bin/python

import math

target_num_divisors = 5

def incorrect_factorize(num):
    factors = set()
    current_num = num
    current_num_sqrt = int(math.ceil(math.sqrt(current_num)))
    current_i = 2

    factors.add(1)
    
    while current_i <= current_num_sqrt:
        if current_num % current_i == 0:
            #print "%d divides %d!" % (current_i, current_num)
            factors.add(current_i)
            factors.add(num / current_i) #if this line is included, it gets all factors, not just the prime ones
            current_num = current_num / current_i
            #print "now trying %d" % current_num
            current_num_sqrt = int(math.ceil(math.sqrt(current_num)))
            #print "going up to %d" % current_num_sqrt
            current_i = 2
        else:
            current_i = current_i + 1

    factors.add(current_num)
    factors.add(num / current_num)
    factors.add(num)

    return factors


def factorize(num):
    factors = set()
    num_sqrt = int(math.ceil(math.sqrt(num)))
    
    for i in range(1, num_sqrt+1):
        if num % i == 0:
            #print "%d divides %d!" % (i, num)
            factors.add(i)
            factors.add(num / i) #if this line is included, it gets all factors, not just the prime ones
            
    return factors


def iterate_triangle_numbers(max_count, max_num_factors):
    curr_num = 0
    counter = 0
    
    while counter < max_count:
        counter += 1
        curr_num += counter

        factors = factorize(curr_num)

        if len(factors) > max_num_factors:
            print counter, curr_num, len(factors), factors
            break
        
        # this block outputs everything each iteration
        #
        # factor_list = list(factors)
        # factor_list.sort()
        # print counter, "\t", curr_num, "\t", len(factor_list), "\t", factor_list

        # this block outputs less regularly for use in big cases
        #
        if counter % 1000 == 0:
           print counter, "\t", curr_num, "\t", len(factors)
        
iterate_triangle_numbers(10000000, 500)
#iterate_triangle_numbers(10000000, 5)
