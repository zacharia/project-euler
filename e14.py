#!/usr/bin/python

from math import *

def reduce(num):
    curr_num = num
    counter = 1

    while curr_num != 1:
        if curr_num % 2 == 0:
            curr_num = curr_num / 2
        else:
            curr_num = 3 * curr_num + 1
        counter += 1

    return counter


def naive_solution(max_num):
    max_chain_length = -1
    max_chain_number = -1

    for i in range(1, max_num + 1):

        if i % 10000 == 0:
            print i

        curr_chain_length = reduce(i)
        if curr_chain_length > max_chain_length:
            max_chain_length = curr_chain_length
            max_chain_number = i

    print max_chain_number, max_chain_length


def clever_reduce(num, table):
    curr_num = num
    counter = 1

    while curr_num != 1:
        #print "\t", num, counter, curr_num
        if curr_num < num and table[curr_num] != 0:
            table[num] = counter + table[curr_num] - 1
            #print table
            #print "Exiting early with", counter + table[curr_num]
            return counter + table[curr_num] - 1
        elif curr_num % 2 == 0:
            curr_num = curr_num / 2
        else:
            curr_num = 3 * curr_num + 1
        counter += 1

    table[num] = counter
    #print table
    return counter


def clever_solution(max_num):
    max_chain_length = -1
    max_chain_number = -1

    results_table = [ 0 for i in range(1000000+1+1)]

    for i in range(1, max_num + 1):

        if i % 10000 == 0:
            print i

        curr_chain_length = clever_reduce(i, results_table)
        #results_table[i] = curr_chain_length
        
        if curr_chain_length > max_chain_length:
            max_chain_length = curr_chain_length
            max_chain_number = i

    print max_chain_number, max_chain_length


#table = [0 for i in range(1000)]
#for i in range(1,10):
#    print reduce(i), clever_reduce(i, table)
#naive_solution(100000)
clever_solution(1000000)
