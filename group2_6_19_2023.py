# Loops

# Print numbers 1 - 10
'''
print(1)
print(2)
.
.
.
print(10)
.
.
.
print(500000)
'''

# While loops
'''
i = 0
while i < 10:
    print(i)
    i = i + 1
'''
# Basic loop
def loop():
    i = 0
    while i < 10:
        print(i)
        i = i + 1
    print("Done.")
# loop()

# Difference b/w loop and conditional
def cond():
    i = 0
    if i < 10:
        print(i)
        i = i + 1
    print("Done.")
# cond()

# name == "faris" True
# name != "faris" True

# cond1 and cond2 --> both MUST be true
# cond1 or cond2 --> ONE must be true

# Check for correct password
def passCheck(correctPass):
    password = input("What is your password? ")
    tries = 0
    while password != correctPass and tries < 3:
        tries = tries + 1
        password = input("Try again. ")
    if tries >= 3:
        print("LOCKED OUT OF APP!")
    else:
        print("Welcome to the app.")
# passCheck("RFS")

# faris != RFS --> True
# mohammad != RFS --> True
# RFS != RFS --> False


# Average of 'n' numbers
def avg():
    num = input("What is your first number? ")
    add = 0
    count = 0
    while num != "stop":
        add = add + int(num)
        count = count + 1
        num = input("Next number: ")
    avg = add / count
    print("Your average is " + str(avg))
# avg()


# Print up to a known number
def numberPrinter(n):
    i = 0
    while i < n:
        print(i)
        i = i + 1
# numberPrinter(10)


# For loop
def forNumberPrinter(n):
    for i in range(n):
        print(i)
# forNumberPrinter(10)


# range()
# ALWAYS stop at 'stop - 1'
# ALWAYS start at start
# range(stop) -> stop after 'n' times
# range(start, stop) -> run stop - start times
# range(start, stop, step)
# DEFAULT START = 0
# DEFAULT STEP = 1

def forLoops():
    print("range(5)")
    for i in range(5):
        print(i)

    print("range(5, 10)")
    for i in range(5, 10):
        print(i)

    print("range(0, 10, 2)")
    for i in range(0, 10, 2):
        print(i)

    print("range(10, 0, -1)")
    for i in range(10, 0, -1):
        print(i)

    print("range(-5)")
    for i in range(-5):
        print(i) # nothing happens
forLoops()

# Small trick for writing i = i (+-*/) 1
# i = i + 1
# i += 1

# i = i - 1
# i -= 1

# i = i * 5
# i *= 5
