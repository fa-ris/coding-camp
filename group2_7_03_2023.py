def triangle_calculator(h):
    sum = 0
    for i in range(1, h + 1):
        sum += i * i # sum = sum + i * i
        print(str(i) * i)
    print("Sum of triangle is " + str(sum))
# triangle_calculator(7)


def new_scrabble(word, bonus, swap):
    score = 0
    count = 0
    for c in word:
        if c in "gt":
            temp = 6
        elif c in "aeiou":
            temp = -2
        elif c in "hjnwp":
            temp = 3
        else:
            temp = 1
        if count == bonus and bonus != -1:
            score += temp * 2
        else:
            score += temp
        count += 1
    if swap:
        score *= -1
    print(score)
'''
new_scrabble("python", 2, False)
new_scrabble("oxyphenbutazone", 0, True)
'''
