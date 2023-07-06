### Tuples ###

# List: [1, 2, "hello"]

# Tuples are similar to lists
# but enclosed in () instead of []
# tuples usually used in databases
# want to associate 3 pieces of info with a student
# we could change elements in a list
# student = ["mohd.", 15, "physics"]
# student[1]="hello"

def tuples1():
    person = ("Faris", 22, "student")
    print(person)
    print(type(person))

    print(person[1])
    # index can never be out of range
    # we can use -1 for last value

    # we can also do slicing
    slice = person[1:4]
    print(slice)

    # we can have an empty tuple
    # this is denoted by ()
    print(())

    # here, we start to get different to lists...
    myList = [3]
    print(type(myList))

    myTuple = ("Hello")
    print(myTuple, type(myTuple))

    # how can we put a single item in a tuple?
    a = ("Hello",)
    print(a, type(a))
    print(len(a))

    # another difference between the two
    myList = ["apple", 5, "oranges"]
    myList[1] = "bananas"
    print(myList)

    myTuple = ("apple", 5, "oranges")
    myTuple[1] = "bananas"
    print(myTuple)  
# tuples1()


def tuples2():
    # packing a tuple
    x = ("Faris", "student", 22)

    # unpacking a tuple (made easy)
    (name, job, age) = x

    # we can now use these as three different vars
    print(name, type(name))
    print(job, type(job))
    print(age, type(age))

    # difference with lists:
    y = ["Faris", "student", 22]
    # to 'unpack' a list is pretty hard
    name = y[0]
    job = y[1]
    age = y[2]
    print(name, type(name))
    print(job, type(job))
    print(age, type(age))
# tuples2()


def swapping():
    a = 4
    b = 5

    # we want to swap the values, so that:
    # a = 5 and b = 4

    (a, b) = (b, a)
    print(a)
    print(b)
# swapping()

# takes in radius and returns circumf. and area
def circle(r):
    # reminder: ^ does XOR
    # ** does to the power
    area = 3.1415 * (r ** 2)
    circ = 3.1415 * (r * 2)
    return (round(area, 2), round(circ, 2))
# print(circle(5))

# tuples for databases
# function to make grocery database
def groceryList():
    # user inputs item name, price, quantity
    # type stop when done adding
    # build a list of tuples and return the list\
    gList = []
    item = ""
    while item not in ["stop", "enough"]:
        item = input("What is your item name? ")
        if item == "stop":
            break
        price = float(input("Item price? "))
        quant = int(input("How many? "))
        # pack in a tuple...
        entry = (item, price, quant)
        gList.append(entry)
    return gList
print(groceryList())
        
# now, let's buy all our groceries
def buyGroceries(gList):
    cost = 0.0
    for item in gList:
        # unpack items
        (name, price, qty) = item
        print(name + ":" + str(qty) + ", " str(price))
        cost = cost + price * qty
    print("Total cost: " + str(cost))

# Upload your code to github.com!!!
