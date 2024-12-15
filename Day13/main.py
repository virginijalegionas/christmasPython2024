def isRobotBack(moves):
    currentPosition = [0, 0]
    completedMoves = set()
    i = 0
    while i < len(moves):
        move = moves[i]
        match move:
            case "R":
                currentPosition[0] += 1
                completedMoves.add("R")
                i += 1
            case "L":
                currentPosition[0] -= 1
                completedMoves.add("L")
                i += 1
            case "U":
                currentPosition[1] += 1
                completedMoves.add("U")
                i += 1
            case "D":
                currentPosition[1] -= 1
                completedMoves.add("D")
                i += 1
            case "*":
                doubleMovement = moves[i+1]
                match doubleMovement:
                    case "R":
                        currentPosition[0] += 2
                        completedMoves.add("R")
                    case "L":
                        currentPosition[0] -= 2
                        completedMoves.add("L")
                    case "U":
                        currentPosition[1] += 2
                        completedMoves.add("U")
                    case "D":
                        currentPosition[1] -= 2
                        completedMoves.add("D")
                i += 2
            case "!":
                invertedMovement = moves[i+1]
                match invertedMovement:
                    case "R":  # R inverted to L
                        currentPosition[0] -= 1
                        completedMoves.add("L")
                    case "L":  # L inverted to R
                        currentPosition[0] += 1
                        completedMoves.add("R")
                    case "U":  # U inverted to D
                        currentPosition[1] -= 1
                        completedMoves.add("D")
                    case "D":  # D inverted to U
                        currentPosition[1] += 1
                        completedMoves.add("U")
                i += 2
            case "?":
                notDoneMovement = moves[i+1]
                if notDoneMovement not in completedMoves:
                    match notDoneMovement:
                        case "R":
                            currentPosition[0] += 1
                            completedMoves.add("R")
                        case "L":
                            currentPosition[0] -= 1
                            completedMoves.add("L")
                        case "U":
                            currentPosition[1] += 1
                            completedMoves.add("U")
                        case "D":
                            currentPosition[1] -= 1
                            completedMoves.add("D")
                i += 2
    if currentPosition[0] == 0 and currentPosition[1] == 0:
        return True
    else:
        return currentPosition


print(f"{isRobotBack('R')}")      # [1, 0]
print(f"{isRobotBack('RL')}")     # true
print(f"{isRobotBack('RLUD')}")   # true
print(f"{isRobotBack('*RU')}")    # [2, 1]
print(f"{isRobotBack('R*U')}")    # [1, 2]
print(f"{isRobotBack('LLL!R')}")  # [-4, 0]
print(f"{isRobotBack('R?R')}")    # [1, 0]
print(f"{isRobotBack('U?D')}")    # true
print(f"{isRobotBack('R!L')}")    # [2,0]
print(f"{isRobotBack('U!D')}")    # [0,2]
print(f"{isRobotBack('R?L')}")    # true
print(f"{isRobotBack('U?U')}")    # [0,1]
print(f"{isRobotBack('*U?U')}")   # [0,2]
print(f"{isRobotBack('U?D?U')}")  # true
print(f"{isRobotBack('R!U?U')}")  # [1,0]
print(f"{isRobotBack('UU!U?D')}")  # [0,1]
