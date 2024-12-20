def distributeWeight(weight):
    boxRepresentations = {
        1: [" _ ", "|_|"],
        2: [" ___ ", "|___|"],
        5: [" _____ ", "|     |", "|_____|"],
        10: [" _________ ", "|         |", "|_________|"]
    }
    availableBoxes = [10, 5, 2, 1]
    boxesNeededToPack = []
    # calculate the boxes needed for packing gift
    while weight > 0:
        for i in range(0, len(availableBoxes)):
            if weight >= availableBoxes[i]:
                boxesNeededToPack.append(availableBoxes[i])
                weight -= availableBoxes[i]
                break
    # print packed gift
    boxesNeededToPack = boxesNeededToPack[::-1]
    for a in range(0, len(boxesNeededToPack)):
        match boxesNeededToPack[a]:
            case 1:  # either you need print only box-1 or box-1 is followed by box-2, box-5, box-10
                if len(boxesNeededToPack) == 1:
                    for i in range(0, len(boxRepresentations[boxesNeededToPack[a]])):
                        print(boxRepresentations[1][i])
                else:
                    if a == 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 2:
                        print(f"{boxRepresentations[1][0]}")
                        print(f"{boxRepresentations[1][1]}{
                              boxRepresentations[1][0].strip()}")
                    if a == 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 5:
                        print(f"{boxRepresentations[1][0]}")
                        print(f"{boxRepresentations[1][1]}{
                              boxRepresentations[2][0].strip()}")
                    if a == 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 10:
                        print(f"{boxRepresentations[1][0]}")
                        print(f"{boxRepresentations[1][1]}{
                              boxRepresentations[1][0].strip() * 2}{boxRepresentations[5][0].strip()}")
            case 2:  # either you need print only box-2
                if len(boxesNeededToPack) == 1:
                    for i in range(0, len(boxRepresentations[boxesNeededToPack[a]])):
                        print(boxRepresentations[2][i])
                else:
                    # or box-2 is at the top and followed by box-2 box-5, box-10
                    if a == 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 2:
                        print(f"{boxRepresentations[2][0]}")
                        print(f"{boxRepresentations[2][1]}")
                    if a == 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 5:
                        print(f"{boxRepresentations[2][0]}")
                        print(f"{boxRepresentations[2][1]}{
                              boxRepresentations[1][0].strip()}")
                    if a == 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 10:
                        print(f"{boxRepresentations[2][0]}")
                        print(f"{boxRepresentations[2][1]}{
                              boxRepresentations[5][0].strip()}")
                    # or box-2 is in the middle and followed by box-5, box-10
                    if a > 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 5:
                        print(f"{boxRepresentations[2][1]}{
                              boxRepresentations[1][0].strip()}")
                    if a > 0 and a + 1 < len(boxesNeededToPack) and boxesNeededToPack[a+1] == 10:
                        print(f"{boxRepresentations[2][1]}{
                              boxRepresentations[5][0].strip()}")
                    # or box-2 at the end
                    if a == len(boxesNeededToPack) - 1:
                        print(f"{boxRepresentations[2][1]}")
            case 5:  # either you need print only box-5
                if len(boxesNeededToPack) == 1:
                    for i in range(0, len(boxRepresentations[boxesNeededToPack[a]])):
                        print(boxRepresentations[5][i])
                else:  # or box-5 is at the top and followed by box-10
                    if a == 0 and a + 1 < len(boxesNeededToPack):
                        print(f"{boxRepresentations[5][0]}")
                        print(f"{boxRepresentations[5][1]}")
                        print(f"{boxRepresentations[5][2]}{
                              boxRepresentations[2][0].strip()}")
                    # or box-5 is in the middle and followed by box-10
                    if a > 0 and a + 1 < len(boxesNeededToPack):
                        print(f"{boxRepresentations[5][1]}")
                        print(f"{boxRepresentations[5][2]}{
                              boxRepresentations[2][0].strip()}")
                    # or box-5 is at the end
                    if a == len(boxesNeededToPack) - 1:
                        print(f"{boxRepresentations[5][1]}\n{
                              boxRepresentations[5][2]}")
            case 10:  # either only one box-10 exists or box-10 is on the top and followed by another box-10
                if len(boxesNeededToPack) == 1 or (a == 0 and a + 1 < len(boxesNeededToPack)):
                    for i in range(0, len(boxRepresentations[boxesNeededToPack[a]])):
                        print(boxRepresentations[10][i])
                else:  # box-10 at the end
                    print(f"{boxRepresentations[10][1]}\n{
                          boxRepresentations[10][2]}")
    return ""


print(f"1\n{distributeWeight(1)}")
print(f"2\n{distributeWeight(2)}")
print(f"3\n{distributeWeight(3)}")
print(f"4\n{distributeWeight(4)}")
print(f"5\n{distributeWeight(5)}")
print(f"6\n{distributeWeight(6)}")
print(f"7\n{distributeWeight(7)}")
print(f"8\n{distributeWeight(8)}")
print(f"9\n{distributeWeight(9)}")
print(f"10\n{distributeWeight(10)}")
print(f"11\n{distributeWeight(11)}")
print(f"13\n{distributeWeight(13)}")
print(f"14\n{distributeWeight(14)}")
print(f"15\n{distributeWeight(15)}")
print(f"17\n{distributeWeight(17)}")
print(f"18\n{distributeWeight(18)}")
print(f"19\n{distributeWeight(19)}")
print(f"20\n{distributeWeight(20)}")
print(f"30\n{distributeWeight(30)}")
print(f"37\n{distributeWeight(37)}")
