from functools import reduce
from collections import Counter


def findMissingNumbers(nums):
    maxNumber = reduce(max, nums)
    allNumbers = []
    a = 1
    while a <= maxNumber:
        allNumbers.append(a)
        a += 1
    # Subtract arrays to get the missing numbers
    counter1 = Counter(allNumbers)
    counter2 = Counter(nums)
    missingNumbers = list((counter1 - counter2).elements())

    return missingNumbers


print(findMissingNumbers([1, 2, 4, 6]))  # [3, 5]
print(findMissingNumbers([4, 8, 7, 2]))  # [1, 3, 5, 6]
print(findMissingNumbers([3, 2, 1, 1]))  # []
print(findMissingNumbers([5, 5, 5, 3, 3, 2, 1]))  # [4]
