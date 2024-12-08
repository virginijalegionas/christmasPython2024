def createFrame(goodNames):
    longestName = len(max(goodNames, key=len))
    print(f"The List is:")
    firstLastLine = f"{'*' * (longestName + 4)}"
    print(firstLastLine)
    for name in goodNames:
        nameString = f"* {name}{' ' * (longestName - len(name))} *"
        print(nameString)
    print(firstLastLine)


userInput = input(
    "Enter child names separated by commas (e.g., John, May, Tim, Tommy): ")
# put the names into the lists
if userInput.strip():  # ensure no data is entered
    kidsNames = [x.strip() for x in userInput.split(',')]
    createFrame(kidsNames)
else:
    print("Input cannot be empty. Please enter names.")
