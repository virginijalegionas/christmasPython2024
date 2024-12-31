from collections import Counter


def fixGiftList(received, expected):
    missing = {}
    extra = {}
    # Subtract list2 from list1 using Counter
    counter1 = Counter(expected)
    counter2 = Counter(received)
    missingGifts = list((counter1 - counter2).elements())
    extraGifts = list((counter2 - counter1).elements())
    for missingGift in missingGifts:
        if not missingGift in missing.keys():
            missing[missingGift] = 0    
        missing[missingGift] +=1
    for extraGift in extraGifts:
        if not extraGift in extra.keys():
            extra[extraGift] = 0
        extra[extraGift] +=1

    

    return missing, extra



missing, extra = fixGiftList(['puzzle', 'car', 'doll', 'car'], ['car', 'puzzle', 'doll', 'ball'])
print(f"TESTIGN DATA1\nMissing Toys: {missing}\nExtra Toys:{extra}\n")
missing, extra = fixGiftList(['book', 'train', 'kite', 'train'],['train', 'book', 'kite', 'ball', 'kite'])
print(f"TESTIGN DATA2\nMissing Toys: {missing}\nExtra Toys:{extra}\n")
missing, extra = fixGiftList(['bear', 'bear', 'car'],['bear', 'car', 'puzzle', 'bear', 'car', 'car'])
print(f"TESTIGN DATA3\nMissing Toys: {missing}\nExtra Toys:{extra}\n")
missing, extra = fixGiftList(['bear', 'bear', 'car'], ['car', 'bear', 'bear'])
print(f"TESTIGN DATA4\nMissing Toys: {missing}\nExtra Toys:{extra}\n")


