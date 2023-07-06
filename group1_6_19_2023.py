# Loops
'''
i = 0
while i < 10:
    print(i)
    i = i + 1
'''

# While loops
def loop():
    i = 0
    while i < 10:
        print(i)
        i = i + 1
    print("Done!")
# loop()

def cond():
    i = 0
    if i < 10:
        print(i)
        i = i + 1
    print("Done!")
# cond()

# name == "Faris"
# name != "Faris"
# cond1 and cond2 -> both MUST be true
# cond1 or cond2 -> ONE must be true

# Password checker
def passwordCheck(correctPass):
    pw = input("What is your password? ")
    numOfTries = 0
    while pw != correctPass and numOfTries < 3:
        numOfTries = numOfTries + 1
        pw = input("Wrong! Try again. ")
    if numOfTries >= 3:
        print("LOCKED OUT OF ACCOUNT.")
    else:
        print("Welcome to the app.")
# passwordCheck("RFS")


# Find average of 'n' numbers
def avg():
    text = input("What is your first number? ")
    sum1 = 0
    count = 0
    while text != "stop":
        if text != "stop":
            text = int(text)
            sum1 = sum1 + text
            count = count + 1
        text = input("Next number? ")
    avg = sum1 / count
    print("Average is " + str(avg))
#avg()


# Print "Hello" 3 times
def three():
    count = 0
    while count < 3:
        print("Hello")
        count = count + 1
# three()

def nTimes(n):
    count = 0
    while count < n:
        print("Hello")
        count = count + 1
# nTimes(10000000) # do not do this!


# For loops
def listing(n):
    '''
    i = 0
    while i < n:
        print(i + 1)
        i = i + 1
    '''
    for i in range(n):
        print(i)
# listing(10)

# range() function
# range(stop)
# range(start, stop)
# range(start, stop, step)

def forLoops():
    print("range(5)")
    for i in range(5):
        print(i)

    print("range(1, 10)")
    for i in range(1, 10):
        print(i)

    print("range(1, 10, 2)")
    for i in range(1, 10, 2):
        print(i)

    print("range(10, 1, -1)")
    for i in range(10, 1, -1):
        print(i)
# forLoops()

