def distributeWeight(weight):
    weight2 = weight
    boxRepresentations = {
        1: [" _ ", "|_|"],
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"]
    }
    availableBoxes = [10, 5, 2, 1]
    boxesNeededToPack = []
    # calculate the boxes needed for packing gift
    for i in range(0, len(availableBoxes)):
        while weight >= availableBoxes[i]:
            boxesNeededToPack.append(availableBoxes[i])
            weight -= availableBoxes[i]
    # print packed gift
    boxesNeededToPack = boxesNeededToPack[::-1]
    thePrint = ""
    previousBoxWidth = 0
    for box in boxesNeededToPack:
        currentBox = boxRepresentations[box]
        for b in range(0, len(currentBox)):
            if b == 0:
                if previousBoxWidth == 0:
                    thePrint += f"{currentBox[b]}\n"
                else:
                    cuttedString = currentBox[b].strip()
                    cuttedString = cuttedString[(previousBoxWidth-1):]
                    thePrint += f"{cuttedString}\n"
            else:
                if b == len(currentBox) - 1:
                    thePrint += f"{currentBox[b]}"
                else:
                    thePrint += f"{currentBox[b]}\n"
        previousBoxWidth = len(currentBox[0])

    return f"////{weight2}\n{thePrint}\n"


print(distributeWeight(1))
print(distributeWeight(2))
print(distributeWeight(3))
print(distributeWeight(4))
print(distributeWeight(5))
print(distributeWeight(6))
print(distributeWeight(7))
print(distributeWeight(8))
print(distributeWeight(9))
print(distributeWeight(10))
print(distributeWeight(11))
print(distributeWeight(13))
print(distributeWeight(14))
print(distributeWeight(15))
print(distributeWeight(17))
print(distributeWeight(18))
print(distributeWeight(19))
print(distributeWeight(20))
print(distributeWeight(30))
print(distributeWeight(37))
