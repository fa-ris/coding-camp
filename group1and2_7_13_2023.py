### CSV Files ###

# CSV: Comma Seperated Value (file.csv)
# header, header, header
# data, data, data
# data, data, data

# time (s), mass (g), speed (m/s)
# 50, 60, 1000
# 123, 1231, 123114

def csvRead(fname):
    '''
    try:
        file = open(fname, "r")
    except:
        print("File does not exist")
    '''
    file = open(fname, "r") # r indicates reading, not writing

    # read and print the header line
    # which describes the data below
    # time(s), mass(g), speed(m/s)
    header = file.readline() # a string
    # removes any leading/trailing whitespace
    header = header.strip()
    header = header.split(",")
    print(header)

    # how many variables are in my data?
    # print(len(header))

    # list to hold our data
    # this will be a list of lists
    # each list will be data for each header
    data = []

    # all row data now in 'rows'
    rows = file.readlines()

    # at this point, we are done with our file
    # we HAVE TO close it
    file.close()

    # print(rows)

    for row in rows:
        # 'row' represents a string
        # which represents one line in city_crime.csv
        line = row.strip().split(",")
        # whitespace includes '\n'

        # we now have a list of our data point
        # [year, ranking, city, rate]
        data.append(line)
    print(data)
# csvRead("city_crime.csv")

    






### Modules ###
# Module is some code someone else wrote
# which performs functionality we may need
# import nameOfModule

# this is also a way to organize your code
# they are still Python files

# there are some modules that come with Python download
# math, random, os, time, string, sys


# let's start with math
'''
in the math module:
def division(a, b):
    fff
    ifjwsifjeij
def mult(a, b):
    iegirgier

-
-
-
import math
math.mult(a, b)
'''

import math

def mathDemo():
    print(round(math.pi, 5)) # pi up to ~10 d.p.
    print(type(math.pi))

    # to find square root:
    print(math.sqrt(25.0))
# mathDemo()

# let's say we only need math.sqrt
# we can import only math.sqrt:
from math import sqrt
# we can now use sqrt() function from math


# we can give our modules nicknames
import math as m
# instead of math.pi, we would use m.pi, etc.
# more useful for something like:
# import ufhsiunsaiuvnsa as u



# Random...
import random

def randomDemo():
    print(random.randrange(3, 9))
    print("Roll the dice...") # 1-6
    print(random.randrange(1, 7)) # [1, 7)

    # random decimal number
    print(random.random()) # 0 -> 0.999999....
# randomDemo()



import time
# this allows us to use physical time in our programs
def timeDemo():
    start = time.process_time()
    # how long has my program been running?

    for i in range(1000000000):
        pass
    stop = time.process_time()
    print(stop - start)
#timeDemo()

import myModule as my
def myModuleTest():
    print(my.dozen)
    print(my.greeting())
    print()
    print(my.square(13))
myModuleTest()


