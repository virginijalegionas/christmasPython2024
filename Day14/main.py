def minMovesToStables(reindeer, stables):
    minMoves = 0
    reindeer.sort()
    stables.sort()
    for i in range(0, len(reindeer)):
        minMoves += abs(reindeer[i] - stables[i])
    return minMoves


print(f"Minimal moves to arange the reindeer: {
      minMovesToStables([2, 6, 9], [3, 8, 5])}")
print(f"Minimal moves to arange the reindeer: {
      minMovesToStables([1, 1, 3], [1, 8, 4])}")
print(f"Minimal moves to arange the reindeer: {
      minMovesToStables([1, 2, 3], [1, 2, 3])}")
