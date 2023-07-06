# String indexing
# s = "hello"
# s[1]

# Every character in a string has an index number
# Start: 0
# End: len(string) - 1
# s = "hello"
# First index (0): 'h' --> s[0]
# Last index (4): 'o' --> s[4]
# s[5] --> gives an error, as length is 5
'''
s = "hello"
print(s[0])
print(s[2])
print(s[4])

s = "dfgiuhfiuhasefihweiufhqriwhiquewrh"
print(s[-1])
print(s[len(s) - 1]) # don't really do this

def index(s):
    print("The first character of s is: ")
    print(s[0])

    print("The second character is:" )
    print(s[1])

    print("The last character is: ")
    print(s[-1])

    # print("This does not work: ")
    # print(s[50])
    # gives string index out of range
index("hello")

s = "Hello"
print(s[-2])
print(s[-3])
print(s[-5])
# From the negatives, only -1 is frequently used


# Review of loops for strings
def loop1(s):
    for char in s:
        print(char)
loop1("freddie")

def loop2(s):
    for i in range(len(s)):
        print(i, s[i])
loop2("freddie")
        
# More advanced string functions

# Function to return a string with every other letter
## faris --> frs
def everyOther(s):
    t = ""
    for i in range(0):
        # check if number is even
        if i % 2:
            t = t + s[i]

    #for i in range(0, len(s), 2):
     #   t = t + s[i]

    return t
print("Here")
print(everyOther("faris"))


# Slicing
s = "ramallah friends school"
print(s[9:16])

# Slicing rules
# used to extract specific range of indeces
# string[start : stop + 1]
# string[start : stop + 1 : step]
# string[0:-1:2]
# string[0::2]
# Default values:
# start = 0
# end = len(s) - 1
# step = 1

# Examples of slicing
def slicing():
    s = "elephant"
    print(s[2:5])
    print(s[4:108968960])
    print(s[12:16])
    # Recreate the everyOther() function
    print(s[0:-1:2])
    print(s[0::2])
    print(s[::2])
    # All 3 of the above do the same thing
    print(s[::-1])
slicing()


# Final built-in string methods
def stringMethods(s):
    print(s.isdigit())
    print(s.isupper()) # checks if string is upper case
    print(s.islower())
stringMethods("sdfnsndfn")
stringMethods("2539723489")
'''

def moreMethods(s):
    print(s.upper()) # turn to upper case
    print(s.lower()) # turn to lower case
moreMethods("uhUbIYsiudgIUghefbu")


def evenMoreMethods(s):
    # removes all leading and trailing whitespace
    # eg: s = "   iwefihjw  hnlsknd   "
    # becomes "iwefihjw  hnlsknd"
    print(s.strip())
    # if input given, remove starting and ending instances
    # of input
    # s = ", faris,"
    # becomes " faris"
    print(s.strip(","))

    # find
    # gives index of first instance
    # of input
    # if input is not in string
    # returns -1
    print(s.find("h"))
    if "h" in s:
        print(s.index("h"))
    else:
        print(-1)

# Find second occurance of a character in a string
# s = "hellohello"
# string.find("h")
# firstInstance = 0
# ellohello
# "ellohello".find(h)
def secondFind(string, char):
    firstInstance = string.find(char)
    slice = string[firstInstance + 1:]
    secondInstance = slice.find(char)
    print(firstInstance + secondInstance + 1)
secondFind("elephant", "e")

    
    
    
