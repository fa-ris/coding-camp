'''
# Functions
# print("string")
# round(number, 2)
# input("question")

# Average of 3 numbers
def average(num1, num2, num3):
    add = num1 + num2 + num3
    avg = add / 3
    return avg
print(average(1, 2, 3))

# Average of 4 numbers
def average4(num1, num2, num3, num4):
    add = num1 + num2 + num3 + num4
    avg = add / 4
    return avg
print(average4(56, 13, 12, 1))

# Find average of friends' ages
def friends():
    friend1 = input("What is your age? ")
    friend2 = input("What is your age? ")
    friend3 = input("What is your age? ")
    add = int(friend1) + int(friend2) + int(friend3)
    avg = add / 3
    avg = round(avg, 3)
    sentence = "The average age is " + str(avg)
    return sentence
print(friends())
'''

'''
def marsWeight():
    weight = input("What is your weight? ")
    weight = float(weight)
    mars = 0.38 * weight
    mars = round(mars, 2)
    sentence = "If you weigh " + str(weight) + " on Earth, you will weigh " + str(mars) + " on Mars."
    return sentence
print(marsWeight())
'''

def coffee():
    radius = float(input("Diameter? ")) / 2
    height = float(input("Height? "))
    sentence = "The cup fits " + str(round(3.14 * (radius ** 2) * height, 2))
    return sentence
print(coffee())
