#!/usr/bin/python

import math

target_num = 600851475143
#target_num = 144

prime_factors = []

def is_prime(num):
    print "determining if %d is prime" % num
    num_sqrt = int(math.ceil(math.sqrt(num)))
    print "the square root of %d is %d. Looping from 2 to that" %(num, num_sqrt)
    for i in range(2,num_sqrt+1):
        if num % i == 0:
            print "Oh no! %d is a factor of %d. It's not prime" % (i, num)
            return False
    print "We found no factors! %d is prime" % num
    return True

current_num = target_num
current_num_sqrt = int(math.ceil(math.sqrt(current_num)))
current_i = 2

while current_i <= current_num_sqrt:
    if current_num % current_i == 0:
        print "%d divides %d!" % (current_i, current_num)
        prime_factors.append(current_i)
        current_num = current_num / current_i
        print "now trying %d" % current_num
        current_num_sqrt = int(math.ceil(math.sqrt(current_num)))
        print "going up to %d" % current_num_sqrt
        current_i = 2
    else:
        current_i = current_i + 1

prime_factors.append(current_num)

print "The factors:"
for i in prime_factors:
    print i
