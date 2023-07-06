# Conditionals
# if (condition):
#   do something
#   print(...)
#   do multiple things
'''
def grades(grade):
    if (grade > 90):
        print("Congrats! You got an A.")
grades(95) # prints the above
grades(60) # does nothing

def gradesComplex(grade):
    if (grade > 90):
        print("Congrats! You got an A.")
    else:
        print("You did not get an A.")
gradesComplex(95)
gradesComplex(60)

def finalGrade(grade):
    if (grade > 90):
        print("You got an A")
    elif (grade > 80):
        print("You got a B")
    elif (grade > 70):
        print("You got a C")
    else:
        print("You failed")
finalGrade(75)


# True / False in Python
95 > 90 ==> True
90 > 95 ==> False
True False
if (True):
    # do something
if (False):
    # do something
0 ==> False
1, 2, 3, ... ==> True
if (1):
    # do something
if (0):
    # this will not execute
"" ==> False
"efiuhwefuhewfh" ==> True

# Combining conditions
80 < x < 90
x > 80 and x < 90
'''
x = 85
if (x > 80 and x > 90):
    print("Hello")
if (x > 80 or x < 50):
    print("Bye")


def minCoins():
    total = int(input("How much money do you have? "))
    tens_cnt = total // 10 # eg: 37 // 10 = 3
    five_cnt = (total - (tens_cnt * 10)) // 5
    twos_cnt = (total - ((tens_cnt * 10) + (five_cnt * 5))) // 2
    ones_cnt = (total - ((twos_cnt * 2) + (tens_cnt * 10) + (five_cnt * 5))) // 1
    print(tens_cnt, ", ", five_cnt, ", ", twos_cnt, ", ", ones_cnt)
minCoins()
