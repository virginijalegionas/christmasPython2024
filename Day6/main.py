def inBox(box):
    charBox = []
    #put string into array
    for i in range(0, len(box)):
        charBox.append(list(box[i]))

    boxHeight = len(charBox)
    boxWidth = len(charBox[0])
    while True:
        added = False
        found = False
        for y in range(0, boxHeight):
            for x in range(0, boxWidth):
                if charBox[y][x] == "*":
                    found = True
                    if (y == 0 or y == boxHeight - 1) or (x == 0 or x == boxWidth - 1):
                        return False
                    if charBox[y-1][x] == " ":
                        charBox[y-1][x] = "*"
                        added = True
                    if charBox[y+1][x] == " ":
                        charBox[y+1][x] = "*"
                        added = True
                    if charBox[y][x-1] == " ":
                        charBox[y][x-1] = "*"
                        added = True
                    if charBox[y][x+1] == " ":
                        charBox[y][x+1] = "*"
                        added = True
        if not found:
            return False
        if not added:
            return True


print(inBox([
    "#####",
    "# * #",
    "#   #",
    "# #  ",
    "#####"
]))  # ➞ false

print(inBox([
    "####",
    "#  #",
    "# #*",
    "#  #",
    "####"
]))  # ➞ false

print(inBox([
    "####",
    "#  #",
    "#  #",
    "# *#",
    "####"
]))  # ➞ true

print(inBox([
    "###",
    "#*#",
    "###"
]))  # ➞ true

print(inBox([
    "####",
    "#* #",
    "#  #",
    "####"
]))  # ➞ true

print(inBox([
    "#####",
    "#   #",
    "#  #*",
    "#####"
]))  # ➞ false

print(inBox([
    "#####",
    "#   #",
    "#   #",
    "#   #",
    "#####"
]))  # ➞ false
