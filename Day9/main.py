def moveTrain(board, mov):
    # first get coordinates, where the train is
    i = 0
    isEtaFound = True
    while isEtaFound and i < len(board):
        if "@" in board[i]:
            trainStart = [i, board[i].rfind("@")]
            isEtaFound = False
        i += 1
    # calculate the coordinates where to go
    trainToGo = []
    match mov:
        case "U":
            trainToGo = [trainStart[0] - 1, trainStart[1]]
        case "D":
            trainToGo = [trainStart[0] + 1, trainStart[1]]
        case "L":
            trainToGo = [trainStart[0], trainStart[1] - 1]
        case "R":
            trainToGo = [trainStart[0], trainStart[1] + 1]
        case _:
            return print("Wrong Command was added")
    # try to move tain by given command
    if 0 <= trainToGo[0] < len(board) and 0 <= trainToGo[1] < len(board):
        element = board[trainToGo[0]][trainToGo[1]]
        match element:
            case ".": return "none"
            case "o": return "crash"
            case "*": return "eat"
            case _: print("I do not recognize this element in my path")
    else:
        return "crash"


board = [
    '.....',
    '*....',
    '@....',
    'o....',
    'o....'
]
print(f"Train Moves Up: {moveTrain(board, "U")}")
print(f"Train Moves Down: {moveTrain(board, "D")}")
print(f"Train Moves Left: {moveTrain(board, "L")}")
print(f"Train Moves Right: {moveTrain(board, "R")}")


board2 = [
    '......',
    '.oo...',
    '*@o...',
    '.*o...',
    '.oo...'
]
print(f"Train Moves Up: {moveTrain(board2, "U")}")
print(f"Train Moves Down: {moveTrain(board2, "D")}")
print(f"Train Moves Left: {moveTrain(board2, "L")}")
print(f"Train Moves Right: {moveTrain(board2, "R")}")
