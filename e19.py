#!/usr/bin/python

from math import *

days_norm = {"January" : 31,
             "February" : 28,
             "March" : 31,
             "April" : 30,
             "May" : 31,
             "June" : 30,
             "July" : 31,
             "August" : 31,
             "September" : 30,
             "October" : 31,
             "November" : 30,
             "December" : 31,
             }

days_leap = days_norm.copy()
days_leap["February"] = 29

month_order = ("January",
               "February",
               "March",
               "April",
               "May",
               "June",
               "July",
               "August",
               "September",
               "October",
               "November",
               "December")

week_days = ("Monday",
             "Tuesday",
             "Wednesday",
             "Thursday",
             "Friday",
             "Saturday",
             "Sunday",)

curr_day = "Sunday" #start the day before
curr_day_index = 6

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print is_leap_year(1)
print is_leap_year(4)
print is_leap_year(96)
print is_leap_year(100)
print is_leap_year(400)
print is_leap_year(800)

counter = 0

for year in range(1900, 2001):
#for year in range(1900, 1905):

    is_leap = is_leap_year(year)

    print year
    
    for month in month_order:
        print "\t", month
        if is_leap:
            for date in range(1, days_leap[month] + 1):
                curr_day_index = (curr_day_index + 1) % 7
                print "\t\t", date, "\t", curr_day_index, week_days[curr_day_index]
                if year >= 1901 and year <= 2000:
                    if date == 1 and week_days[curr_day_index] == "Sunday":
                        counter += 1
        else:
            for date in range(1, days_norm[month] + 1):
                curr_day_index = (curr_day_index + 1) % 7
                print "\t\t", date, "\t", curr_day_index, week_days[curr_day_index]

                if year >= 1901 and year <= 2000:
                    if date == 1 and week_days[curr_day_index] == "Sunday":
                        counter += 1

print counter
