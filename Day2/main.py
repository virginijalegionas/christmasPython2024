def createFrame(goodNames):
    longestName = len(max(goodNames, key=len))
    firstLastLine = f"{'*' * (longestName + 4)}\n"
    nameList = firstLastLine
    for name in goodNames:
        nameString = f"* {name}{' ' * (longestName - len(name))} *\n"
        nameList = nameList + nameString
    nameList = nameList + firstLastLine
    print(f"The List is: \n{nameList}")

user_input = input("Enter child names separated by commas (e.g., John, May, Tim, Tommy): ")
# put the names into the lists
if user_input.strip(): #ensure no data is entered
    kidsNames = [x.strip() for x in user_input.split(',')]
    createFrame(kidsNames)
else:
    print("Input cannot be empty. Please enter names.")
