### Exceptions and Exception Handling ###
def divide(a, b):
    print(a / b)
'''
divide(10, 2)
divide(0, 10)
divide(10, 0)
'''

# We will use exception handling here
def divide2(a, b):
    try:
        # best case is this works
        print(a / b)
    except:
        # but in the worst case, we will do this except block
        print("You cannot divide by zero.")
    # after these, we can continue writing any code we want
'''
divide2(10, 2)
divide2(10, 0)
'''

def divide3(a, b):
    try:
        print(a / b)
    except:
        print("You cannot divide by zero.")
    finally:
        # optional: but will run regardless of try/except 
        print("Done trying this division.")

# myList = [1, 2, 3]
# print(myList[5]) -> this gives us an error (index out of bounds)
def error1():
    myStr = "Hello"
    try:
        print(myStr[10])
    except:
        print("Index out of bounds, try another index.")
    print("Do more things after try/except.")

# Input checking
def error2():
    try:
        x = input("Type a number: ")
        y = int(x)
        print(y * 2)
    except:
        print("User input must be a number.")






### Files and I/O ###

# This is different to what we have done so far,
# since changes stay after the program is complete.
# File lifetime is longer than that of the program.


# Reading a file #
# open(filename, mode)
# filename -> string, with full filename, including extension (.txt, .csv)
# mode -> "w": write; "a": append; "r": read
# file.close()


# Opens a file called filename
# Filename is a str
def readFile(filename):
    file = open(filename, "r")
    # print(type(file))
    text = file.read()
    print(text)
    file.close()
# readFile("poem.txt")

# Function to split our text into a list, by line
'''
Line1
Line2
Line3
'''
# Output: [Line1, Line2, Line3]
def readFileList1(fname):
    myFile = open(fname, "r")
    text = myFile.read()
    myFile.close()
    textList = text.split("\n") # \n = new line character (enter/return)
    print(textList)
readFileList1("poem.txt")


# Using the built-in method to do this
def readFileList2(fname):
    aFile = open(fname, "r")
    myList = aFile.readlines()
    aFile.close()
    print(myList)
#readFileList2("poem.txt")


# checking if file exists or not
def readFile(fname):
    try:
        f = open(fname, "r")
        line = f.readline()
        f.close()
    except:
        print("File " + fname + " does not exist.")
        return
    print(line, end="")
readFile("po1em.txt")


# writing to files
def writeFile(fname):
    try:
        f = open(fname, "w")
        f.write("This is line 1.\n")
        f.write("This is line 2.\n")
        f.close()
    except:
        print("Sorry - file write failed.")
#writeFile("newPoem.txt")

def appendFile(fname):
    try:
        f = open(fname, "a") # append: write at the end of the file
        f.write("This is line 3.\n")
        f.close()
    except:
        print("File does not exist")
appendFile("newPoem.txt")
