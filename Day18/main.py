import re


def findInAgenda(agenda, phone):
    # put child list into array
    childrenInfoList = agenda.split('\n')
    fixedChildInfoList = []
    phonePattern = r"(\+[\d*\-\d*]+)"
    namePattern = r"\<(.*)\>"
    # fixing list
    for childInfo in childrenInfoList:
        # get childs name
        isNameMatch = re.search(namePattern, childInfo)
        childName = isNameMatch.group(1)
        # get childs phone
        isPhoneMatch = re.search(phonePattern, childInfo)
        childPhone = isPhoneMatch.group(1)
        # get childs address
        childAddress = childInfo.replace(childPhone, "")
        childAddress = childAddress.replace(childName, "")
        childAddress = childAddress.replace("<>", "").strip()
        # assembling all info into fixed array
        childInfo = {"name": childName,
                     "phone": childPhone, "address": childAddress}
        fixedChildInfoList.append(childInfo)
    # finding a child
    childrenFound = [{"name": child["name"], "address": child["address"]}
                     for child in fixedChildInfoList if phone in child["phone"]]
    childrenCount = len(childrenFound)
    if childrenCount == 1:
        print(childrenFound[0])
    elif childrenCount > 1:
        print("Too many results found")
    else:
        print("No results found")



agenda = '''+34-600-123-456 Calle Gran Via 12 <Juan Perez>
Plaza Mayor 45 Madrid 28013 <Maria Gomez> +34-600-987-654
<Carlos Ruiz> +1-800-555-0199 Fifth Ave New York'''
findInAgenda(agenda, "34-600-123-456")
findInAgenda(agenda, "111")
findInAgenda(agenda, "1")
