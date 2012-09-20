#!/usr/bin/python

import math


#store the digits we want to pandigital about as a string
digits = "123456789"


#a faster method to compute the desired permutation without iterating
#through all the possibilities. It generates the permutation directly.
def fast_nth_perm(digits, n):

    #temporary storage variables
    curr_num = n - 1
    result = ""

    #go through the digits from the biggest down (i.e. 9 to 0)
    for i in reversed(range(len(digits))):
        #do integer division to get the quotient of curr_num / i!
        quotient = curr_num / math.factorial(int(i))
        #also get the remainder with mod
        remainder = curr_num % math.factorial(int(i))

        #the quotient is the index of the current digit in the desired
        #permutation. Add it to the result.
        result += (digits[quotient])
        # and remove it from the list of digits (each digit can only
        # appear once)
        digits = "%s%s" % (digits[:quotient], digits[quotient+1:])

        #update curr num to be the remainder of the previous
        #curr_num's division.
        curr_num = remainder
        
    return result


# this method divides up a permutation into a multiplicand, mutliplier
# and product based on the arguments given. I could just inline it,
# but I made it a separate method for code clarity.
def split_up_permutation(permutation, mult_pos, eq_pos):
    return permutation[:mult_pos], permutation[mult_pos:eq_pos], permutation[eq_pos:]


# this method finds all the pandigital products and returns them. It
# operates by generating all permutations of the digits 1 through 9,
# and trying all multiplication combinations of those
# permutations. Any valid ones that work out get saved.
def get_pandigital_products():

    #this set stores the products (a set to avoid duplicates)
    ret = set()

    # loop through every permutation (all 9! of them)
    for i in range(1, math.factorial(9)+1):

        #get the current permutation
        curr_permutation = fast_nth_perm(digits, i)
        
        # this is to show progress. Only output every 1000th thing to
        # avoid slowing the program while waiting for output.
        if i % 1000 == 0:
            print i

        # iterate through each possible position for the * sign in the
        # equation made from the permutation.
        for mult_pos in range(1, 7):
            # and then through each possible position for the = sign
            # in the equation made from teh permutation.
            for eq_pos in range(mult_pos+1, 9):

                #split up the permutation into it's component parts
                equation = split_up_permutation(curr_permutation, mult_pos, eq_pos)
                # if the result of the multiplication == the last part
                # of the permutation
                if int(equation[0]) * int(equation[1]) == int(equation[2]):
                    # print the found pandigital product
                    print equation
                    # add the product to the set
                    ret.add(int(equation[2]))
                    
    return ret


# find all the pandigital products
products = get_pandigital_products()
print products
#print the sum
print "the sum is: ", sum(products)
