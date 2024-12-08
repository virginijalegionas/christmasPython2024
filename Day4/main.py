import math


def createXmasTree(treeLevels, treeSymbol):
    xmasTree = ""
    treeWidht = treeLevels * 2 - 1
    for i in range(1, treeLevels + 1):
      #  if i != treeLevels: #
        levelTreeWidht = i * 2 - 1
        undescoreNumber = math.floor((treeWidht - levelTreeWidht) / 2)
        xmasTree += f"{'_' * undescoreNumber}{treeSymbol *
                                              levelTreeWidht}{'_' * undescoreNumber}\n"

    # adding trunk
    undescoreForTrunk = math.floor((treeWidht - 1) / 2)
    trunkString = f"{'_' * undescoreForTrunk}#{'_' * undescoreForTrunk}\n"*2
    xmasTree += trunkString
    return xmasTree


height = input(
    "Please add the height of the tree, only numbers 1 to 100 are allowed:")
treeSymbol = input(
    "Please add tree symbol, only first symbol will be taken:")
treeHeight = int(height)
if (type(treeHeight) == int and (treeHeight > 1 and treeHeight <= 100) and treeSymbol.strip()):
    xmasTree = createXmasTree(treeHeight, treeSymbol[0])
    with open("./Day4/output.txt", "w") as f:
        f.write(xmasTree)
    print("Check the file, Xmas tree is waiting for you!!!")
else:
    print(
        "There was no character added or tree height is not in this range [1,100]. Try another time")
