### Lists ###
# Similar to str, int, this is a data type

# To make a list, use [] and seperate components w/ commas (,)
# Very similar operations to strs
def lists1():
    myList1 = ["red", "blue", "green"]
    myList2 = [1, 4, 6]
    print(myList1)
    print(myList2)
    print(type(myList1))
    myList3 = ["red", 5, 7.8]
    print(type(myList3))
    print(myList3[1])
    print(type(myList3[1]))
    print(len(myList3))   
# lists1()

# Strings are not mutable
# Lists ARE
def lists2():
    myList = ["apples", 7, "fred"]
    print(myList)
    # Change lists at position 1
    myList[1] = 2.8
    print(myList)

    # We cannot do this:
    # myStr = "Hello"
    # myStr[1] = "f"
    # This gives an error
# lists2()

def addList():
    fruits = ["apples", "oranges"]
    print(fruits, len(fruits))

    # Add bananas to the list
    # This does not work
    # fruits = fruits + "bananas"

    fruits.append("bananas")
    # To add to end of list, use list.append(...)

    fruits = fruits + ["straberries"]
    # We can only add things of the same type
    print(fruits)
# addList()


def lists3():
    myStr = ""
    myList = [] # empty list
    print(myList, len(myList))
    myList.append("Faris")
    print(myList, len(myList))
# lists3()

# Removing items from list
def lists4():
    myList = ["apples", "oranges", "bananas", "tomatoes"]
    print(myList, len(myList))
    del(myList[-1])
    print(myList, len(myList))
# lists4()

# Lists are VERY similar to strings
# .append()
# del(index)
# max(), min()
# .index()
# sort()
# slicing
# We will see these after the break


def listSlice():
    myStr = "Hello World"
    print(myStr[1:4]) # ell

    myList = ["apples", "oranges", "bananas", 1, 3, 5]
    print(myList[1:5])
    print(myList[1:100])
    print(myList[30:50])
    list2 = []
    print(myList[0:5])

    # Slicing to reverse a list
    print(myList[::-1])
# listSlice()


# We can also make lists of lists
def listOfLists():
    myList = [["h", "i", "j"], 6, "hello"]
    print(len(myList))
    print(type(myList))
    print(type(myList[0]))
    newList = myList[0] # ["h", "i", "j"]
    print(newList[1])
    print(myList[0][1])
listOfLists()

def loopOnStrings():
    myList = [["a", "b", "c"], [1, 2, 3, 4]]
    for item in myList:
        for char in item:
            print(char)
loopOnStrings()

# This is what we call a nested loop


def harderLoop():
    myList = [[1, 2, 3], 5, "hi", ["hello", "world"]]
    for item in myList:
        if type(item) != list:
            print(item)
        else:
            for char in item:
                print(char)
harderLoop()
