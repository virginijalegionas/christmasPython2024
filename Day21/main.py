def waklTree(current, height):
    leftHeight = 0
    rightHeight = 0
    if current["left"] != None:
        leftHeight = waklTree(current["left"], height + 1)
    if current["right"] != None:
        rightHeight = waklTree(current["right"], height + 1)    
    return max([leftHeight, rightHeight, height])


def treeHeight(tree):
    if tree == None:
        return 0    
    height = waklTree(tree, 1)
    return height


tree = {
    "value": '🎁',
    "left": {
        "value": '🎄',
        "left": {
            "value": '⭐',
            "left": None,
            "right": None
        },
        "right": {
            "value": '🎅',
            "left": None,
            "right": None
        }
    },
    "right": {
        "value": '❄️',
        "left": None,
        "right": {
            "value": '🦌',
            "left": None,
            "right": None
        }
    }
}

print(treeHeight(tree))
print(treeHeight(None))
