def findMissingNumbers(nums):
    maxNumber = max(nums)
    missingNumbers = []
    for i in range(1, maxNumber + 1):
        if i not in nums:
            missingNumbers.append(i)
    
    return missingNumbers


print(findMissingNumbers([1, 2, 4, 6]))  # [3, 5]
print(findMissingNumbers([4, 8, 7, 2]))  # [1, 3, 5, 6]
print(findMissingNumbers([3, 2, 1, 1]))  # []
print(findMissingNumbers([5, 5, 5, 3, 3, 2, 1]))  # [4]
