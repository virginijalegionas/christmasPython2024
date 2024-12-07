def prepareGifts(gifts):
    sortedGifts = sorted(gifts)
    uniqueGifts = []
    for x in range(len(sortedGifts)):
        if sortedGifts[x] != sortedGifts[x-1] or x == 0:
            uniqueGifts.append(sortedGifts[x])  
    if len(uniqueGifts) > 0:
        print(f"unique gift array: {uniqueGifts}")
    else:
        print("There are no gifts, the list remains empty")
#SMART ONE LINE SOLUTTION: sortedGifts = sorted(set(gifts))


user_input = input("Enter numbers separated by commas (e.g., 2, 2, 9, 5, 3, 2): ")
# Convert the input string into a list of integers
if user_input.strip():     #ensure that data was added
    try:
        santasGifts = [int(x) for x in user_input.split(',') if x.strip()]  
        prepareGifts(santasGifts)      
    except ValueError:
                print("Please enter valid numbers separated by commas.")
else:
    santasGifts = []  # If input is empty, assign an empty list

