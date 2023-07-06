# Advanced string methods

# String indexing
s = "hello"
'''
print(s[0]) # we start counting at 0, not 1
print(s[1])
print(s[4])
print(len(s))
'''

# the index we want goes in the [square] brackets
# the result of this is one single character]
# always start count at 0
# always end count at len(s) - 1

def index(s):
    print("First index: ")
    print(s[0])

    print("Second index: ")
    print(s[1])

    print("Last index: ")
    print(s[len(s) - 1])
    print(s[-1])

    print("Second to last index: ")
    print(s[-2]) # don't usually use this
# index("faris")

s = "hello"
# print(s[-5])
# print(s[5]) # does not work


# Review of loops from last time
def loop1(s):
    for c in s:
        print(c)
loop1("hello")

# Rewriting loop1() using indeces
def loop2(s):
    for i in range(len(s)):
        print(s[i], i)
loop2("hello")


# Function that returns a string with every other letter
# ramallah --> rmla
def everyOther(s):
    t = ""
    for i in range(0, len(s), 2):
        t = t + s[i]
    return t
def everyOther1(s):
    t = ""
    for i in range(len(s)):
        if i % 2 == 0:
            t = t + s[i]
    return t
# these two do the same thing
print(everyOther("ramallah"))
print(everyOther1("ramallah"))


# Slicing
# s = "Ramallah"
# t = "allah"
# t = s[3:7]
# Generally:
# string[start:stop + 1]
# string[start:stop + 1:step]
# Default values:
# start = 0
# end = len(string) - 1
# step = 1

def slicing():
    st = "elephant"

    print(st[2:5])

    # No error for this
    print(st[4:100])

    # No error, but prints nothing
    print(st[12:16])

    # Rewrite everyOther() using slicing
    print(st[0:len(st):2])
    print(st[0::2])
    print(st[::2])

    # Rewrite reverse()
    print(st[::-1])
slicing()


# Some more string methods
def moreStrMethods(s):
    print(s.isdigit())
    print(s.isupper())
    print(s.islower())
moreStrMethods("jkhKJHkuGHiugk")

def evenMoreMethods(s):
    print(s.lower())
    print(s.upper())
evenMoreMethods("cjHGkuGhjvbhVBjh345b")

def moreMethods(s):
    # Removes all whitespace before and after string
    # s = "   ihish  ikhjjkh   "
    # returns "ihish  ikhjjkh"
    print(s.strip())
    print(s.strip(","))
    # s = ", faris,"
    # becomes " faris"

    # find: find first instance of input
    # if the string doesn't have the input, -1
    print(s.find("h"))

# Find second instance of character in string
# elephant, e
# we should get 2, not 0
def secondFind(character, string):
    firstInstance = string.find(character) # 0
    slice = string[firstInstance + 1:]
    secondInstance = slice.find(character) # 1
    return firstInstance + secondInstance + 1
print(secondFind("e", "elephant"))

