### Dictionaries ###

# Reminder:
# lists -> [5, "hello", [1, 2, 3]]
# tuples -> (5, "hi") or (6,)
# Can we use {} for lists or tuples?

# Dictionaries are similar to lists
# They use {}, not [] nor ()
# We store key, value pairs
# dict = {"hello":"word for greeting"}

# the keys in a dict can be strings or any data type
# but keys must be unique
# lists: [5, 5, 5]
# dict: {5:"hi", 5:"hello"} not allowed
# values can be anything, no need to be unique

def dict1():
    # dict of keys: letters, values: numbers
    myDict = {"a":1, "b":2, "c":3, 1:50}
    print(type(myDict))
    print(len(myDict)) # we have 3 PAIRS
    # indexing in lists and tuples:
    # listOrTuple[index]
    # dict[index] defeats the purpose of using a dictionary
    print(myDict["b"])
    print(myDict[1])
    # we are not indexing
    # we are looking up
    # when we use [], we are getting the VALUE
    # of the KEY we look up
# dict1()


# Function to count number of vowels in a string
def countVowels(string):
    count = {"a":0, "e":0, "i":0, "o":0, "u":0}
    # 5 keys, one for each vowel
    # all starting with unknown quantity (0)
    for c in string:
        if c == "a":
            count["a"] = count["a"] + 1
        elif c == "e":
            count["e"] = count["e"] + 1
        elif c == "i":
            count["i"] = count["i"] + 1
        elif c == "o":
            count["o"] = count["o"] + 1
        elif c == "u":
            count["u"] = count["u"] + 1
    print(count)
# countVowels("qwiofbcqnnewirouvnqwewiqoeufbsb")
            
# Function to look up student grades
namesAndGrades = [("faris", 50), ("mohammad", 90), ("ahmad", 75)]
def lookUpGrades(student):
    for tups in namesAndGrades:
        if tups[0] == student:
            print(tups[1])
            break
# lookUpGrades("ahmad")

gradesDict = {"faris":50, "mohammad":90, "ahmad":75}
def betterLookup(student):
    print(gradesDict[student])
# betterLookup("ahmad")


def dicts2():
    print(gradesDict)
    print(list(gradesDict.keys()))
    print(list(gradesDict.values()))
    sum = 0
    for grade in gradesDict.values():
        sum += grade
    print(sum / len(gradesDict))
#dicts2()

def modifyDict():
    # to add a new key:value pair to your dictionary:
    gradesDict["basil"] = 100
    print(gradesDict)

    # if key already exists, override data already there
    gradesDict["faris"] = 0
    print(gradesDict)

    # to delete a key:value pair:
    del(gradesDict["faris"])
    print(gradesDict)

    # you should always check before deleting:
    if "yousef" in gradesDict:
        del(gradesDict["yousef"])
    else:
        print("Yousef not in this dictionary")
# modifyDict()

def delete(name):
    if name in gradesDict:
        del(name)
    else:
        print("Name not in dictionary")

# Letter frequency
# for example, "dad" to give us {"d":2, "a":1}
def freq(word):
    letters = {} # empty dictionary
    for char in word:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    return letters
print(freq("earioubnsdkjvbsdkjvbsdjaf"))
