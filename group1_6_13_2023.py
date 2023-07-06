'''
# These are simple print lines.
print("Hello world")
print("My name is Faris.")

# This is a comment.
# These are used to explain code to a reader.
# Anything after the '#' is ignored by IDLE.

# print("Comment.")

# Python can also do math.
print(3)
print(45)
print(3 + 45)# add operation
print(45 - 3) # subtract
print(3 * 4) # multiply
print(12 / 4) # divide

# It can also combine words with math.
print("3 + 4 = ", 3 + 4)
print("45 - 3 = ", 45 - 3)
print("3 x 4 = ", 3 * 4)
print("15 / 3 = ", 15 / 3)

# Single and double quotes both work.
# If you start with one, you must continue.
print('Hi.')
print("Hi.")

# BODMAS (Order of operations)
print("3 * (4 + 2)", 3 * (4 + 2))
# Power done using **, not ^
print("(7 - 2) * (81 / 3 ^ 2) = ", (7 - 2) * (81 / 3 ** 2))

# Space or no space is the same.
print(3+4)
print(3 + 4)
'''

'''
This is called a comment block.
This is used to:
(a) Comment long code.
(b) Describe long code.
'''

print("This is outside the comment.")

# Some more complex math operations
print("13 / 2 = ", 13 / 2) # regular division
print("13 // 2 = ", 13 // 2) # floor division
print("3 ^ 2 = ", 3 ** 2) # power
print("29 % 2 = ", 29 % 2) # remainder

# Rounding
x = 1.032384789347
print(round(x, 2)) # rounds 'x' to 2 decimals
y = 12.23480971239081723
print(round(y, 5)) # rounds 'y' to 5 decimals
print(round(y, 2))

# Simple variable examples
x = 3 # 'x' is a variable
y = 4
print("x * y = ", x * y)

# Rules for naming variables
# (1) Variable names MUST start with a letter
# (upper or lower case) or underscore (_)
# (2) Variable names CANNOT start with a number
# (3) VN MUST only have letters, numbers, and _
# (4) VNs are case-sensitive (age =/= AgE)
# (5) No spaces

'''
x = 1
X = 1
_x = 1
9x = 1 # DOES NOT WORK
x-3 = 1 # DOES NOT WORK
'''

# Naming etiquette:
# Not neccessary but good to have.
# (1) Start with a lower case letter.
# (2) Use camel-case for long names:
# farisqadan -> farisQadan (not faris_qadan)
# (3) Use descriptive names!
# Not x, but height. Not y, but width.


# Data types
# Numbers and words
# ints, and strings
# Strings
name = "Faris" # string
print(name)
name2 = "Faris"
print(name2)
num = "1.23"

# Ints
x = 1 # int (integer, not decimal number)
y = 2
print(x)
print(x * y)

# Floats
z = 1.2324 # float (decimal number)
f = 3.214252
d = 3.0
print(z * f)

# Tool to find data type:
x1 = "2" # expected: string (str)
x2 = 2 # expected: int
x3 = 2.0 # expected: float
print(type(x1)) # type tool
print(type(x2))
print(type(x3))

# Type conversion / casting
x = "3" # str
print("x is of type ", type(x))
y = "5"
print(x + y) # 3 + 5 = 35 (wrong)

x = int(x)
y = int(y)
print(type(x))
print(x + y)

'''
x = "faris"
x = int(x)
DOES NOT WORK, since "faris" is not a number.
'''

x = 35
print(type(x))
x = str(x)
print(type(x))


