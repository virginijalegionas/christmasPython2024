#simple solution using python intertools
""" import itertools

def generateGiftSets(gifts):
    combinations = []
    for i in range(1, len(gifts) + 1):
        combinations.extend(itertools.combinations(gifts, i))

    # Print all combinations
    print(f"Total amount of combinations is: {len(combinations)}")
    for combination in combinations:        
        print(combination)
    return """

def generateGiftSets(gifts):
    numberOfGifts = len(gifts)
    allCombinations = []
    binaryCombinations = []    
    i = 1
    binaryFormat = '{0:0'+str(numberOfGifts)+'b}' # {0:05b}
    while True:
        combination = list(binaryFormat.format(i))[::-1] #reversing array and trying to solve sorting issue, but sorts only partially
        if len(combination) <= numberOfGifts:
            i += 1
            binaryCombinations.append(combination)
        else:
            break
    #converting binary arrays into the gift arrays
    for element in binaryCombinations:        
        giftCombination = []
        for a in range(0, numberOfGifts):
            if element[a] == '1':
                giftCombination.append(gifts[a])
        allCombinations.append(giftCombination)

    print(f"Total amount of combinations is: {len(allCombinations)}")   
    sortedByLenghtCombinations = sorted(allCombinations, key= lambda x: len(x))
    for comb in sortedByLenghtCombinations:
        print(comb)
    return 

generateGiftSets(['car', 'doll', 'iPad', 'puzzle', 'socks'])
generateGiftSets(['car', 'doll', 'puzzle'])
generateGiftSets(['ball'])
generateGiftSets(['game', 'pc'])