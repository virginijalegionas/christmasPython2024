def calculatePrice(ornaments):
    price = 0
    ornamentPrices = []
    # convert ornaments into price values
    for i in range(0, len(ornaments)):
        match ornaments[i]:
            case "*": ornamentPrices.append(1)
            case "o": ornamentPrices.append(5)
            case "^": ornamentPrices.append(10)
            case "#": ornamentPrices.append(50)
            case "@": ornamentPrices.append(100)
            case _:
                return f"undefined symbol: {ornaments[i]} found"
                
    # calculate price
    for i in range(0, len(ornamentPrices)):
        if i != len(ornamentPrices) - 1: # will compare all the array elements except the last one
            if ornamentPrices[i] < ornamentPrices[i+1]: # if next element has higher value, current becomes negative                
                price -= ornamentPrices[i]
            else: # if next element is eaqul or lower, nothing is done
                price += ornamentPrices[i]
        else:
            price += ornamentPrices[i]  # adding last element
    return price


    


xmasTreePrice1 = calculatePrice('***')  # // 3   (1 + 1 + 1)
xmasTreePrice2 = calculatePrice('*o')  # // 4   (5 - 1)
xmasTreePrice3 = calculatePrice('o*')  # // 6   (5 + 1)
xmasTreePrice4 = calculatePrice('*o*')  # // 5  (-1 + 5 + 1)
xmasTreePrice5 = calculatePrice('**o*')  # // 6  (1 - 1 + 5 + 1)
xmasTreePrice6 = calculatePrice('o***')  # // 8   (5 + 3)
xmasTreePrice7 = calculatePrice('*o@')  # // 94  (-5 - 1 + 100)
xmasTreePrice8 = calculatePrice('*#')  # // 49  (-1 + 50)
xmasTreePrice9 = calculatePrice('@@@')  # // 300 (100 + 100 + 100)
xmasTreePrice10 = calculatePrice('#@')  # // 50  (-50 + 100)
#xmasTreePrice11 = calculatePrice('#@Z')  # // undefined (Z is unknown)
xmasTreePrice12 = calculatePrice('')  # // 0
xmasTreePrice13 = calculatePrice('*o^#@') # //34  -1-5-10-50+100
xmasTreePrice14 = calculatePrice('@#^o*') # //166  100+50+10+5+1

print(f"Cristmas Tree Price 1: {xmasTreePrice1}")
print(f"Cristmas Tree Price 2: {xmasTreePrice2}")
print(f"Cristmas Tree Price 3: {xmasTreePrice3}")
print(f"Cristmas Tree Price 4: {xmasTreePrice4}")
print(f"Cristmas Tree Price 5: {xmasTreePrice5}")
print(f"Cristmas Tree Price 6: {xmasTreePrice6}")
print(f"Cristmas Tree Price 7: {xmasTreePrice7}")
print(f"Cristmas Tree Price 8: {xmasTreePrice8}")
print(f"Cristmas Tree Price 9: {xmasTreePrice9}")
print(f"Cristmas Tree Price 10: {xmasTreePrice10}")
print(f"Cristmas Tree Price 11: {calculatePrice('#@Z')}")
print(f"Cristmas Tree Price 12: {xmasTreePrice12}")
print(f"Cristmas Tree Price 12: {xmasTreePrice13}")
print(f"Cristmas Tree Price 12: {xmasTreePrice14}")
