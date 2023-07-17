def plantFinder(old_file, new_file, plant_size):
    file = open(old_file, "r")
    lines = file.readlines() # list of everything: ["name\n", ..., "\n", ...]
    file.close()
    cleanLines = [] # big list of plant lists
    temp = [] # for each individual plant
    for line in lines:
        if line == "\n":
            cleanLines.append(temp) # temp: [name, lifespan, size, price]
            temp = [] # clear 'temp' list for the next plant to use
        else:
            temp.append(line.strip()) # otherwise, remove \n from every comp.
    newFile = open(new_file, "w")
    plantsDict = {}
    for line in cleanLines:
        if line[2] == plant_size:
            plantsDict[line[0]] = float(line[1])
            for n in line:
                newFile.write(n + "\n") # 'enter' after we just inputed info
            newFile.write("\n") # 'enter' after each plant we write
    newFile.close()
    return plantsDict

print(plantFinder("plants.txt", "small_plants.txt", "Small"))    
print(plantFinder("plants.txt", "medium_plants.txt", "Medium"))
print(plantFinder("plants.txt", "large_plants.txt", "Large"))

def plantSplitter(new_file, num_people, tax):
    file = open(new_file, "r")
    lines = file.readlines()
    file.close()
    total = 0
    for i in range(3, len(lines), 5):
        total += float(lines[i][1:].strip())
    total += (tax * total)
    return round(total / num_people, 2)
print(plantSplitter("large_plants.txt", 7, 0.6))
