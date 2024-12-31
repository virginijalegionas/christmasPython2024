def isTreesSynchronized(tree1, tree2):
    isLeftSynchronized = [True, ""]
    isRightSynchronized = [True, ""]
    if tree1["value"] != tree2["value"]:  # when tree node values does not match return False
        return [False, tree1["value"]]
    # checking if tree has oposite nodes and recursively go down
    if "left" in tree1.keys() and "right" in tree2.keys():
        isLeftSynchronized = isTreesSynchronized(tree1["left"], tree2["right"])
    elif "left" in tree1.keys() or "right" in tree2.keys():  # if one node does not exists return False
        return [False, tree1["value"]]
    # checking other pair of oposite nodes and recursively go down
    if "right" in tree1.keys() and "left" in tree2.keys():
        isRightSynchronized = isTreesSynchronized(
            tree1["right"], tree2["left"])
    elif "right" in tree1.keys() or "left" in tree2.keys():  # if one node does not exists return False
        return [False, tree1["value"]]

    return [isLeftSynchronized[0] and isRightSynchronized[0], tree1["value"]]


tree1 = {
    "value": '🎄',
    "left": {"value": '⭐'},
    "right": {"value": '🎅'}
}

tree2 = {
    "value": '🎄',
    "left": {"value": '🎅'},
    "right": {"value": '⭐'}
}
tree22 = {
    "value": '🎄',
    "left": {"value": '🎅'}
}

tree3 = {
    "value": '🎄',
    "left": {"value": '🎅'},
    "right": {"value": '🎁'}
}

tree4 = {
    "value": '🎄',
    "left": {"value": '⭐'},
    "right": {"value": '🎅'}
}


print(f"tree1 and tree1: {isTreesSynchronized(tree1, tree1)}")
print(f"tree1 and tree22: {isTreesSynchronized(tree1, tree22)}")
print(f"tree1 and tree2: {isTreesSynchronized(tree1, tree2)}")  # [true, '🎄']
print(f"tree2 and tree3: {isTreesSynchronized(tree2, tree3)}")
print(f"tree1 and tree3: {isTreesSynchronized(tree1, tree3)}")  # [false, '🎄']
print(f"tree1 and tree4: {isTreesSynchronized(tree1, tree4)}")  # [false, '🎄']
print(f"only values in trees: {isTreesSynchronized(
    {"value": '🎅'},
    {"value": '🧑‍🎄'}
)}")  # [false, '🎅']
