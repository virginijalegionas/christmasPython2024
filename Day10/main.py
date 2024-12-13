import re


def compile(instructions):
    registers = {}
    i = 0
    while i < len(instructions):
        instruction = instructions[i].split(" ")
        # will be checking if every instruction has a correct set of parameters
        parameters = [instruction[0], len(instruction)]
        match parameters:
            case [p1, p2] if p1 == "MOV" and p2 == 3:
                pattern = r"[\d*]"
                isNumber = re.search(pattern, instruction[1])
                if isNumber:  # if number
                    registers[instruction[2]] = {"value": int(instruction[1])}
                else:  # if register
                    registerFrom = instruction[1]
                    registerTo = instruction[2]
                    registers[registerTo] = {
                        "value": registers[registerFrom]["value"]}
                    # not sure it just copies or moves, MOV sounds more like moves
                    registers[registerFrom] = {"value": 0}
                i += 1
            case [p1, p2] if p1 == "INC" and p2 == 2:
                # register is not yet initialized, value set to 0
                if not instruction[1] in registers.keys():
                    registers[instruction[1]] = {"value": 0}
                registers[instruction[1]]["value"] += 1
                i += 1
            case [p1, p2] if p1 == "DEC" and p2 == 2:
                # register is not yet initialized, value set to 0
                if not instruction[1] in registers.keys():
                    registers[instruction[1]] = {"value": 0}
                registers[instruction[1]]["value"] -= 1
                i += 1
            case [p1, p2] if p1 == "JMP" and p2 == 3:                
                if not instruction[1] in registers.keys() or registers[instruction[1]]["value"] == 0:
                    i = int(instruction[2])
                else:
                    i += 1
    if "A" in registers.keys():
        return registers["A"]["value"]
    else:
        return 0


instructions = [
    'MOV -1 C',  # // copies -1 to register 'C',
    'INC C',  # // increments the value of register 'C'
    'JMP C 1',  # // jumps to the instruction at index 1 if 'C' is 0
    'MOV C B',  # // copies register 'C' to register 'A',
    'MOV B C'  # // increments the value of register 'A'
]

print(f"register A value: {compile(instructions)}")
