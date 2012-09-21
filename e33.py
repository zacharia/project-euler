#!/usr/bin/python

import math

# the digits to consider (doesn't include 0 since we want double
# digits and non-multiples of 10)
digits = "123456789"

# this method takes a numerator and a denominator and simplifies the
# fraction to it's simplest representation
def simplify_fraction(numerator, denominator):

    #get the smaller of the top and bottom
    min_num = min(numerator, denominator)

    #store the numerator and denominator in temp variables
    new_numerator = numerator
    new_denominator = denominator

    # loop from the smallest down to 2
    for i in reversed(range(2, numerator+1)):
        # if the current number divides top and bottom
        if new_numerator % i == 0 and new_denominator % i == 0:
            #divide through by it to simplify the fraction
            new_numerator = new_numerator / i
            new_denominator = new_denominator / i

    return new_numerator, new_denominator


# this method find the fractions we're meant to look for
def find_curious_fractions():
    
    # this stores the found fractions
    ret = set()

    # loop through all the possible common digits
    for common_num in digits:
        # loop through the possible second numerator digits
        for top_num in digits:
            # and the possible denominator ones
            for bot_num in digits:
                # loop through the common number being first or second on top
                for top_pos in range(2):
                    # and the same on bottom
                    for bot_pos in range(2):

                        # create the current fraction
                        curr_top = [top_num, top_num]
                        curr_bot = [bot_num, bot_num]
                        #by putting the common number in the top and bottoms
                        curr_top[top_pos] = common_num
                        curr_bot[bot_pos] = common_num

                        # and turn them into ints
                        int_top = int("".join(curr_top))
                        int_bot = int("".join(curr_bot))                        

                        # if the fraction is less than one, and
                        # simplifies to the same thing as when the
                        # common digit is removed
                        if int_top < int_bot and simplify_fraction(int_top, int_bot) == simplify_fraction(int(top_num), int(bot_num)):
                            #we've found one of the fractions
                            ret.add((int_top, int_bot))

    return ret


#find the fractions
fractions = find_curious_fractions()

print "the curious fractions are: ", fractions

#calculate their product
top_product = 1
bot_product = 1

for i in fractions:
    top_product *= i[0]
    bot_product *= i[1]

print "unsimplified: ", top_product, bot_product

#display their simplified product
print "and simplified: ", simplify_fraction(top_product, bot_product)
