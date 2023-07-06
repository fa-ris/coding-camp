'''
print("Hello world") # this is a line of code
print("My name is Faris.")

# This is a comment.
# These are used to explain our code.
# Anything after '#' is not run by Python.
# print("Hi!")

# Python can do math
print("3 + 4 = ", 3 + 4)
print("5 - 3 = ", 5 - 3)
print("5 * 3 = ", 5 * 3)
print("15 / 3 = ", 15 / 3)

# Spaces do not matter.
print(3+4)
print(3 + 4)

# BODMAS (Order of operations)
print((7+2) * (81 / 9))
print((7+2) * (81 / (3 ** 2))) # 3 ** 2 = 3 ^ 2


# Python can do more complex math
print("13 / 2 = ", 13 / 2)
print("13 // 2 = ", 13 // 2) # floor division
print("29 % 2 = ", 29 % 2) # remainder
print("3 ^ 2 = ", 3 ** 2) # power


# Rounding
x = 1.234902390872349 # round to 2 DP
print(round(x, 2))
print(round(x, 6))


# Variables
x = 1
y = 5
height = 12
width = 123.78
print(height)
print(width)


# Naming variables
# MUST start with _ or small/large letter
# MUST only contain letters, numbers, and _
# NO -, *, /, ,
# age =/= aGe =/= AgE

# Etiquette for naming variables
# Start name with small letter
# Multi-word names, use camel-case
# farisqadan x
# faris_qadan x
# farisQadan (yes)

_x = 5
x12349asjdha = 1

'''

'''
This is a comment block.
We use this to comment long blocks of code.
We also use it to describe code.
'''

# Variable types
x = 5 # int (integer)
y = 1.5 # float (decimal)
z = "Faris" # str (string)

# Strings expanded
name = "Ali"
surname = "Qadan"
print(name)
num = "2"
num2 = "5"
print(num + num2)# 2 + 5 = 25

num = int(num)# convert "2" to 2
num2 = int(num2) # convert "5" to 5
print(num + num2)

print(type(num))

x = "5"
print(type(x))

'''
name = "Saeed"
name = int(name)
'''

fl = "5.2345"
print(type(fl))
'''
fl = int(fl)
print(fl)
'''
fl = float(fl)
print(type(fl))

x = 2
print(type(x))

x = float(x)
print(x)

x = str(x)
print(type(x))


# Addition of strings
name = "Faris"
surname = "Qadan"
sentence = name + " " + surname

print(sentence)

#sentence = "Hi, my name is " + name + ". My age is " + 22 + "."
sentence = "Hi, my name is " + name + ". My age is " + str(22) + "."

print(sentence)


# User input
name = "Faris"
name = input("What is your name? ")
age = input("How old are you? ")
sentence = "Hi, my name is " + name + ". My age is " + age + "."
print(sentence)
