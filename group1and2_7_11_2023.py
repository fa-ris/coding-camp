def used_letter(essay):
    characters = ""
    for item in essay:
        for char in item:
            if char not in characters:
                characters += char
    return (len(characters), characters)

def checkbook(list_of_expenses):
    itemsDict = {} # key:value pairs will be item:totalPrice
    total = 0
    for tups in list_of_expenses:
        # input list: [(itemName, price), (itemName, price)]
        itemName = tups[0].lower()
        total += tups[1]
        if itemName in itemsDict:
            itemsDict[itemName] += tups[1]
        else:
            itemsDict[itemName] = tups[1]
    # make a list of tuples to return
    # .items() gives a tuple of (key, value)
    # item[0] -> item name
    # item[1] -> item price
    finalList = list(itemsDict.items())
    finalList.append(("total", total))
    return finalList

def animal_counter(animals):
    aDict = {}
    for a in animals:
        tempAnimal = a[0].upper() + a[1:].lower()
        if not tempAnimal in aDict:
            aDict[tempAnimal] = 1
        else:
            aDict[tempAnimal] += 1
    return aDict



