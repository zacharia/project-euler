#!/usr/bin/python

from math import *


# determine if a number is a palindrome
def is_palindrome(num):
    # get the number as a string
    num_string = str(num)

    #determine the halfway point of the number
    half_length = int(ceil(len(num_string) / 2.0))

    #loop up to that halfway point
    for i in range(0, half_length):
        #check the current number and it's mirror digit in the second
        #half of the string match.
        if num_string[i] != num_string[len(num_string) - i - 1]:
            return False

    #if we've got this far, it must be a palindrome.
    return True


# determine if a number is a palindrome in binary
def is_palindrome_in_binary(num):
    # get the number in binary as a string
    num_string = str(bin(num))
    # remove the prefix "0b"
    num_string = num_string[2:]

    #determine the halfway point of the number
    half_length = int(ceil(len(num_string) / 2.0))

    #loop up to that halfway point
    for i in range(0, half_length):
        #check the current number and it's mirror digit in the second
        #half of the string match.
        if num_string[i] != num_string[len(num_string) - i - 1]:
            return False

    #if we've got this far, it must be a palindrome.
    return True


# finds all numbers less than num that are palindromes in base 10 and
# 2.
def find_all_palindromes(max_num):
    ret = []

    #loop through every number
    for i in range(max_num+1):

        if i % 100000 == 0:
            print i
            
        # check if it's a palindrome in both bases
        if is_palindrome(i) and is_palindrome_in_binary(i):
            ret.append(i)

    return ret


palindromes = find_all_palindromes(10**6)
print palindromes
print "sum = ", sum(palindromes)
