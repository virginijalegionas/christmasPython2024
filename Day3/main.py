import json


def organizeInventory(inventory):
    toysGroups = {}
    for item in inventory:
        if not item["category"] in toysGroups.keys():
            toysGroups[item["category"]] = {}
        if not item["name"] in toysGroups[item["category"]].keys():
            toysGroups[item["category"]][item["name"]] = 0
        toysGroups[item["category"]][item["name"]] += item["quantity"]
    return toysGroups


# input data
inventory = [
    {"name": 'doll', "quantity": 5, "category": 'toys'},
    {"name": 'car', "quantity": 3, "category": 'toys'},
    {"name": 'ball', "quantity": 2, "category": 'sports'},
    {"name": 'car', "quantity": 2, "category": 'toys'},
    {"name": 'racket', "quantity": 4, "category": 'sports'}
]
groupedInventory = organizeInventory(inventory)
# print grouped data in a json style
print(f"first data set grouping:\n{json.dumps(groupedInventory, indent=1)}\n")
# second input data
inventory2 = [
    {"name": 'book', "quantity": 10, "category": 'education'},
    {"name": 'book', "quantity": 5, "category": 'education'},
    {"name": 'paint', "quantity": 3, "category": 'art'}
]
print(f"second data set grouping:\n{json.dumps(
    organizeInventory(inventory2), indent=1)}\n")
