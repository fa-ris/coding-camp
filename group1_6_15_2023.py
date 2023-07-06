# Conditionals
# if my favorite subject is Biology
# then I should take Biology in IB
# otherwise, I should take Chemistry

#if condition:
    # do something
    # can do multiple things

'''
x = 20
if (x > 25):
    print("x is above 15")
'''

def gradeCalc(grade):
    if (grade > 90):
        print("Congrats! You passed!")
    else:
        print("Better luck next time")
gradeCalc(65) # Better luck next time
gradeCalc(95) # Congrats!


def grades(grade):
    if (grade > 90):
        print("You got an A")
    elif (grade > 80):
        print("You got a B")
    elif (grade > 70):
        print("You got a C")
    else:
        print("You got an F")
grades(50)
grades(90)

'''
# True / False: different representations
90 > 70 : True
60 > 70 : False
70 > 70 : False
70 >= 70: True

name == "Faris" # is equal to
name != "Faris" # not equal to

True # this is true, run the condition
False # this is false, do not do the condition

if (True):
    print("Hi")

if (0):# 0 evaluates as False
if False: # False evaluates as False
if 70 > 90: # 70 > 90 is False

'''







def foodDelivery(tax_percentage, food_cost, distance):
    tax_percentage = int(tax_percentage)
    tax = (tax_percentage / 100) * food_cost
    tip = (tax + food_cost) * 0.2
    deliveryFee = 5 + distance
    totalCost = round((tax + food_cost + tip + deliveryFee), 2)
    print("Your total is " + str(totalCost) + " NIS. Delivery is expensive.")
foodDelivery(10, 20, 40)
foodDelivery(5, 2, 25)



def minCoins():
    tens = int(input("How many 10 NIS do you have? "))
    five = int(input("How many 5 NIS do you have? "))
    twos = int(input("How many 2 NIS do you have? "))
    ones = int(input("How many 1 NIS do you have? "))
    total = float((tens * 10) + (five * 5) + (twos * 2) + (ones * 1))
    tens_cnt = total // 10 # eg: 37 // 10 = 3
    five_cnt = (total - (tens_cnt * 10)) // 5
    twos_cnt = (total - ((tens_cnt * 10) + (five_cnt * 5))) // 2
    ones_cnt = (total - ((twos_cnt * 2) + (tens_cnt * 10) + (five_cnt * 5))) // 1
    print(tens_cnt, ", ", five_cnt, ", ", twos_cnt, ", ", ones_cnt)
minCoins()
