import re


def fixPackages(packages):
    # pattern to find the element we should reverse first
    pattern = r"\(\w*\)"
    packSplit = []
    isMatch = re.search(pattern, packages)
    while isMatch:
        packSplit.append(packages[:isMatch.start()])
        packSplit.append(packages[isMatch.start():isMatch.end()])
        packSplit.append(packages[isMatch.end():])
        packSplit[1] = packSplit[1].strip("(")
        packSplit[1] = packSplit[1].strip(")")
        packSplit[1] = packSplit[1][::-1]
        packages = ''.join(packSplit)
        packSplit = []
        isMatch = re.search(pattern, packages)
    return packages


inputString = "(abc(def(gh)i)(jk))"
fixedString = fixPackages(inputString)
print(f"Package was: {inputString}")
print(f"Fixed Package is: {fixedString}")
