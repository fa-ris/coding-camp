# Loops and Strings

def loop():
    # For loop
    for i in range(5):
        print(i)
    # While loop 
    i = 0
    while i < 5:
        print(i)
        i += 1 # == i = i + 1

# s = "word"
# print(s)
# s = int(s)

def strLoop(s):
    # s here is a string parameter
    # print every character in 's'
    # eg: s = "hello"
    # ==> h, e, l, l, o
    for character in s:
        print(character)
# 'character' can be any variable name
# typically: character, char, c, i, faris
# iterates through the string letter by letter
# strLoop("hello")


def strLength(s):
    length = 0
    for char in s:
        length = length + 1
    return length
# print(strLength("hello"))
# print(strLength("oiygidhgiurhiuwhqweihiuh"))

# len(string)
# Built-in, like round(), or print()
# print(len("hello"))


# Count number of vowels in str
def vowels(string):
    # vowels: A, a, E, e, ..., U, u
    vow = 0
    for letter in string:
        if letter in "AaEeIiOoUu":
            print(letter)
            vow = vow + 1
    return vow
# print(vowels("elephant"))
# print(vowels("ElepHAnt"))

# Return True if all character in 0-9
# Return False if any character not 0-9
def isDigit(s):
    result = True
    for letter in s:
        if letter not in "0123456789":
            result = False
            break
    if s == "":
        result = False
    return result
'''
print(isDigit("023872874")) #True
print(isDigit("379872k23472358972598897287")) #False
print(isDigit("")) #False
print(isDigit("_")) #False
'''

# More on loops
def loop1():
    # For loop
    for i in range(5):
        print(i)
    # While loop 
    i = 0
    while i < 5:
        print(i)
        i += 1 # == i = i + 1

# break: if the program hits this statement,
# it immediately quits the loop and
# moves to the next code after the loop

# continue: skip the next iteration of the loop
# example: on i = 5, skip 5, and move to i = 6

# pass: do nothing, not used very often

# Using break, continue, pass
def example():
    word = "go team"
    for letter in word:
        if letter in "ae":
            break
        if letter in "gt":
            continue
        if letter in " ":
            pass
        print(letter)
    print("Done")
# example()

# Create copy of a string
def strcpy(s):
    t = ""
    for char in s:
        t = t + char
        print(char)
        print(t)
    return t

# s = "Ramallah Friends School"
# We want to remove spaces from s
# RamallahFriendsSchool
# s[8] = "" does NOT work

# Function to remove spaces from string
def despace(s):
    t = ""
    for char in s:
        if char not in " ":
            t = t + char
    return t
# print(despace("Ramallah Friends School"))


# Function to reverse a string
# faris -> siraf
def reverse(s):
    t = ""
    for i in range(len(s) - 1, -1, -1):
        t = t + s[i]
    return t
print(reverse("hello"))

# Another more creative way to reverse a string
def reverse1(s):
    t = ""
    for char in s:
        t = char + t
        # usually, we do t = t + char
    return t
print(reverse1("faris"))


# s = cat
# return cattac
# s = faris
# return farissiraf
def mirror(s):
    s = reverse(s) # used the function we wrote
    t = ""
    for char in s:
        t = char + t + char
    return t
print(mirror("hello"))
