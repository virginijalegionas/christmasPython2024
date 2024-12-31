import re


def execute(code):
    resultCount = 0
    # replace anything in the brackets [], with 0
    zeroPattern = r"\[[\-\+\>\}\{]+\]"
    zeroCode = re.sub(zeroPattern, "0", code)
    i = 0
    while i < len(zeroCode):
        match zeroCode[i]:
            case "+":
                resultCount += 1
                i += 1
            case "-":
                resultCount -= 1
                i += 1
            case "0":
                resultCount = 0
                i += 1
            case "{":
                if resultCount == 0:
                    while zeroCode[i] != "}":
                        i += 1
                else:
                    while zeroCode[i] != "}":
                        match zeroCode[i]:
                            case "+":
                                resultCount += 1
                            case "-":
                                resultCount -= 1
                            case "0":
                                resultCount = 0
                            case _:
                                pass
                        i += 1
            case _:
                i += 1
    print(resultCount)


execute('+++')  # 3
execute('+--')  # -1
execute('>+++[-]')  # 0
execute('>>>+{++}')  # 3
execute('+{[-]+}+')  # 2
execute('{+}{+}{+}')  # 0
execute('------[+]++')  # 2
execute('-[++{-}]+{++++}')  # 5
execute('+-{++[-]--}')  # 0
execute('-{++[-]--}')  # -2
