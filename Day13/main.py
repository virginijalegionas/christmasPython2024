def isRobotBack(moves):
    currentPosition = [0,0]
    completedMoves = {}
    i = 0
    while i < len(moves):
        move = moves[i]
        match move:
            case "R":
                currentPosition[0] += 1
                if "R" not in completedMoves.keys():
                    completedMoves["R"] = {"done" : 1}
                else:
                    completedMoves["R"]["done"] += 1      
                i += 1       
            case "L":
                currentPosition[0] -= 1
                if "L" not in completedMoves.keys():
                    completedMoves["L"] = {"done" : 1}
                else:
                    completedMoves["L"]["done"] += 1  
                i += 1
            case "U":
                currentPosition[1] += 1
                if "U" not in completedMoves.keys():
                    completedMoves["U"] = {"done" : 1}
                else:
                    completedMoves["U"]["done"] += 1  
                i += 1
            case "D":
                currentPosition[1] -= 1
                if "D" not in completedMoves.keys():
                    completedMoves["D"] = {"done" : 1}
                else:
                    completedMoves["D"]["done"] += 1  
                i += 1
            case "*":
                doubleMovement = moves[i+1]
                match doubleMovement:
                    case "R":
                        currentPosition[0] += 2
                        if "R" not in completedMoves.keys():
                            completedMoves["R"] = {"done" : 2}
                        else:
                            completedMoves["R"]["done"] += 2      
                           
                    case "L":
                        currentPosition[0] -= 2
                        if "L" not in completedMoves.keys():
                            completedMoves["L"] = {"done" : 2}
                        else:
                            completedMoves["L"]["done"] += 2  
                      
                    case "U":
                        currentPosition[1] += 2
                        if "U" not in completedMoves.keys():
                            completedMoves["U"] = {"done" : 2}
                        else:
                            completedMoves["U"]["done"] += 2  
                      
                    case "D":
                        currentPosition[1] -= 2
                        if "D" not in completedMoves.keys():
                            completedMoves["D"] = {"done" : 2}
                        else:
                            completedMoves["D"]["done"] += 2                  
                i += 2
            case "!":
                invertedMovement = moves[i+1]
                match invertedMovement:
                    case "R": # R inverted to L
                        currentPosition[0] -= 1
                        if "L" not in completedMoves.keys():
                            completedMoves["L"] = {"done" : 1}
                        else:
                            completedMoves["L"]["done"] += 1      
                           
                    case "L": # L inverted to R
                        currentPosition[0] += 1
                        if "R" not in completedMoves.keys():
                            completedMoves["R"] = {"done" : 1}
                        else:
                            completedMoves["R"]["done"] += 1  
                     
                    case "U": # U inverted to D
                        currentPosition[1] -= 1
                        if "D" not in completedMoves.keys():
                            completedMoves["D"] = {"done" : 1}
                        else:
                            completedMoves["D"]["done"] += 1  
                     
                    case "D": # D inverted to U
                        currentPosition[1] += 1
                        if "U" not in completedMoves.keys():
                            completedMoves["U"] = {"done" : 1}
                        else:
                            completedMoves["U"]["done"] += 1                  
                i +=2
            case "?":
                notDoneMovement = moves[i+1]
                if notDoneMovement not in completedMoves.keys():
                    match notDoneMovement:
                        case "R":
                            currentPosition[0] += 1
                            if "R" not in completedMoves.keys():
                                completedMoves["R"] = {"done" : 1}
                            else:
                                completedMoves["R"]["done"] += 1     
                        case "L":
                            currentPosition[0] -= 1
                            if "L" not in completedMoves.keys():
                                completedMoves["L"] = {"done" : 1}
                            else:
                                completedMoves["L"]["done"] += 1 
                        case "U":
                            currentPosition[1] += 1
                            if "U" not in completedMoves.keys():
                                completedMoves["U"] = {"done" : 1}
                            else:
                                completedMoves["U"]["done"] += 1 
                        case "D":
                            currentPosition[1] -= 1
                            if "D" not in completedMoves.keys():
                                completedMoves["D"] = {"done" : 1}
                            else:
                                completedMoves["D"]["done"] += 1                              
                
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
print(f"{isRobotBack('UU!U?D')}") # [0,1]
