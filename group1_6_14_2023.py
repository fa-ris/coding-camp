'''
# String concatenation (addition)
x = 22
print(type(x))

y = "3"
x = "5"
print(y + x)

x = 22
x = str(x)
print(type(x))

#sentence = "My name is Faris, age is " + 22
sentence = "My name is Faris, age is " + str(22)
print(sentence)

# User input
'''
name = input("What is your name? ")
age = input("What is your age? ")
sentence = "My name is " + name + " and age is " + age + "."
print(sentence)
'''

# Tools
# print("fkhskj")
# round(variable, 2)
# input("")
print(round(1.2323423, 2))

# Average of 3 numbers
def average(num1, num2, num3):
    add = num1 + num2 + num3
    avg = add / 3
    return avg

print(average(5, 6, 7))

# Average of 4 numbers
def average4(num1, num2, num3, num4):
    add = num1 + num2 + num3 + num4
    avg = add / 4
    return avg

print(average4(5, 6, 7, 8))

def averageOfFriends():
    friend1 = input("How old are you? ")
    friend2 = input("How old are you? ")
    friend3 = input("How old are you? ")
    add = int(friend1) + int(friend2) + int(friend3)
    avg = add / 3
    avg = round(avg, 2)
    sentence = "The average age of these friends is " + str(avg) + "."
    return sentence

print(averageOfFriends())
'''

def marsWeight():
    earthWeight = input("What is your weight? ")
    earthWeight = float(earthWeight)
    mars = 0.38 * earthWeight
    mars = round(mars, 2)
    sentence = "If you weigh " + str(earthWeight) + " on Earth, you will weigh " + str(mars) + " on Mars."
    return sentence
print(marsWeight())

def coffee():
    diameter = input("What is your diameter? ")
    height = input("What is your height? ")
    volume = 3.14 * ((float(diameter) / 2)) ** 2 * float(height)
    sentence = "Your cup fits " + str(volume) + " amount of coffee."
    return sentence
print(coffee())
