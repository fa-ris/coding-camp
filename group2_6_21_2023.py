# Loops and Strings

# Print every individual character in s
def strLoop(string):
    for character in string:
        print(character)
# strLoop("hello")

# We can use any variable name instead of character
# Usually, we use character, char, c
# letter, l
# We CAN use f, i, var
    
# Function to find length of a string
def length(s):
    l = 0 # counting length
    for letter in s:
        l = l + 1
    return l

# Built-in, just like round(), print()
# print(len("hello"))


# Count number of vowels in a string
def vowels(s):
    l = 0
    for letter in s:
        if letter in "AaEeIiOoUu":
            l = l + 1
            print(letter)
    return l
# print(vowels("Elephant"))


# Function returns True if s is digit
# Otherwise, it returns False
# "2304972349747" -> True
# "987485f28347837" -> False
# ==, != (equal, not equal)
def isDigit(s):
    result = True
    for char in s:
        if char not in "0123456789":
            result = False
            break # stop the loop
    if s == "":
        result = False
    return result

'''
print(isDigit("2304972349747"))
print(isDigit("987485f28347837"))
print(isDigit(""))
print(isDigit("77d23489997777777777723461111111111892736187266735421347155123512531124618273617822222222222222222222222222222222222222222999999999999999999999999999999999999111111111119997234627862374672364723647823647236476234784628376482648723648726347263487264876256234661230912830918230912134728936527361284071623487906587923648756318745178234389465803178710634"))
'''

# Break, continue, pass
# break: stop the loop and move to code
# right after loop

# continue: skip to the next iteration
# eg: if i = 5, go to i = 6

# pass: literally does nothing

# Function to test these words out
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

# Copying strings
def strcpy(s):
    t = ""
    for c in s:
        t += c
    return t
print(strcpy("hello"))

# s = "Ramallah Friends School"
# out = "RamallahFriendsSchool"
def despace(s):
    t = ""
    for c in s:
        if c not in " ":
            t = t + c
    return t
print(despace("Ramallah Friends School"))


# Function to reverse a string
# hello --> olleh
def reverse(s):
    t = ""
    for c in s:
        # order of addition makes a difference
        t = c + t
    return t
print(reverse("hello"))

# Function to mirror a string
# cat --> cattac
# faris --> farissiraf
def mirror(s):
    # using function we already wrote
    s = reverse(s) # code reuse
    t = ""
    for char in s:
        t = char + t + char
    return t
print(mirror("faris"))

### String library ###
import string
# module for the built-in strings below

def builtInStrings():
    print("Letters: " + string.ascii_letters)
    print("Digits: " + string.digits)
    print("Lowercase: " + string.ascii_lowercase)
    print("Punctuation: " + string.punctuation)
    print("Whitespace: " + string.whitespace)
builtInStrings()

# This is all for the sake of readability
