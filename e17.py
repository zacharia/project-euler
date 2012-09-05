#!/usr/bin/python

from math import *

number_length_ones = {"0" : 0,
                      "1" : 3,
                      "2" : 3,
                      "3" : 5,
                      "4" : 4,
                      "5" : 4,
                      "6" : 3,
                      "7" : 5,
                      "8" : 5,
                      "9" : 4,
                      }

number_length_teens = {"0" : len("ten"),
                       "1" : len("eleven"),
                       "2" : len("twelve"),
                       "3" : len("thirteen"),
                       "4" : len("fourteen"),
                       "5" : len("fifteen"),
                       "6" : len("sixteen"),
                       "7" : len("seventeen"),
                       "8" : len("eighteen"),
                       "9" : len("nineteen"),
                       }

number_length_tens = {"0" : 0,
                      "1" : -50000,
                      "2" : len("twenty"),
                      "3" : len("thirty"),
                      "4" : len("forty"),
                      "5" : len("fifty"),
                      "6" : len("sixty"),
                      "7" : len("seventy"),
                      "8" : len("eighty"),
                      "9" : len("ninety"),
                      }

number_length_hundreds = number_length_ones


def get_num_letters(num):
    if len(num) == 3:
        if num[1] == num[2] == "0":
            return number_length_hundreds[num[0]] + len("hundred")
        else:
            return number_length_hundreds[num[0]] + len("hundred") + len("and") + get_num_letters(num[1:])
    
    elif len(num) == 2:
        if num[0] == "1":
            return number_length_teens[num[1]]
        else:
            return number_length_tens[num[0]] + get_num_letters(num[1:])
    
    elif len(num) == 1:
        return number_length_ones[num[0]]

    else:
        print "Error num too weird"
        return -1


def convert(num):
    if num > 1000 or num <= 0:
        print "Error num out of range"
        return -1
    
    elif num == 1000:
        return len("onethousand")

    else:
        return get_num_letters(str(num))
        

def num_letters_up_to(num):
    total_letters = 0
    for i in range(num):
        print i+1, "\t", convert(i+1)
        total_letters += convert(i+1)
    return total_letters


print num_letters_up_to(1000)
print convert(342)
print convert(115)
