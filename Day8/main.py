def drawRace(indices, length):
    emptyRaceTrack = "~" * length
    race = ""
    lastIndex = len(indices) - 1
    for i in range(0, len(indices)):
        if indices[i] == 0:
            deerRace = f"{" " * (lastIndex - i)}{emptyRaceTrack} /{i+1}\n"
        elif indices[i] == -1:
            deerRace = f"{" " * (lastIndex - i)
                          }{emptyRaceTrack[: indices[i]] + "r"} /{i+1}\n"
        else:
            deerRace = f"{
                " " * (lastIndex - i)}{emptyRaceTrack[: indices[i]] + "r" + emptyRaceTrack[indices[i] + 1:]} /{i+1}\n"
        race += deerRace
    return race


indices = [0, 5, -3]
length = 10
print(drawRace(indices, length))

indices2 = [2, -1, 0, 5]
length2 = 8
print(drawRace(indices2, length2))

indices3 = [3, 7, -2]
length3 = 12
print(drawRace(indices3, length3))
