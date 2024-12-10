import re


def fixPackages(packages):
    # pattern to find the element we should reverse first
    pattern = r"\((\w*)\)"
    if "(" in packages and ")" in packages:
        packSplit = re.split(pattern, packages)
        packSplit[1] = packSplit[1][::-1]
        packages = ''.join(packSplit)
        packages = fixPackages(packages)
    return packages


inputString = "abc(def(gh)i)jk"
fixedString = fixPackages(inputString)
print(f"Package was: {inputString}")
print(f"Fixed Package is: {fixedString}")
