# myModule.py
# you can import this

# import myModule
# in another program (note without .py on the import statement)

# a variable in the module
dozen = 12

# that is how the math module made the .pi variable


def greeting():
    print("Hello there!")

# myModule.greeting() will call that function
# from another program, after import myModule


# function to square a number

def square(num):
    return num * num

# call this with myModule.square(n)
