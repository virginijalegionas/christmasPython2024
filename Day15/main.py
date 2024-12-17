def drawTable(data):
    table = ""
    firstLine = ""
    headerLine = ""
    valuesLine = ""
    # get the length of the column headers
    headerNames = list(data[0].keys())
    maxColumnWidth = [len(headerNames[i]) for i in range(0, len(headerNames))]
    # check maybe values in the columns have bigger length
    for i in range(0, len(maxColumnWidth)):
        widestIRow = max(data, key=lambda d: len(str(d[headerNames[i]])))
        widestIRowLength = len(str(widestIRow[headerNames[i]]))
        if widestIRowLength > maxColumnWidth[i]:
            maxColumnWidth[i] = widestIRowLength
    # construct table header
    for a in range(0, len(maxColumnWidth)):
        columnWidth = maxColumnWidth[a] + 2
        if a != len(maxColumnWidth) - 1:
            firstLine += f"+{'-' * columnWidth}"
            headerLine += f"| {headerNames[a].capitalize()}{' ' * (
                columnWidth - len(str(headerNames[a])) - 1)}"
        else:
            firstLine += f"+{'-' * columnWidth}+\n"
            headerLine += f"| {headerNames[a].capitalize()}{' ' * (
                columnWidth - len(str(headerNames[a])) - 1)}|\n"

    # construct table values
    for b in range(0, len(data)):
        for c in range(0, len(headerNames)):
            columnWidth = maxColumnWidth[c] + 2
            if c == len(headerNames) - 1:
                valuesLine += f"| {data[b][headerNames[c]]}{' ' *
                                                            (columnWidth - len(str(data[b][headerNames[c]])) - 1)}|\n"
            else:
                valuesLine += f"| {data[b][headerNames[c]]}{' ' *
                                                            (columnWidth - len(str(data[b][headerNames[c]])) - 1)}"

    table = firstLine + headerLine + firstLine + valuesLine + firstLine
    return table


data1 = [
    {"name": 'Alice', "city": 'London'},
    {"name": 'Bob', "city": 'Paris'},
    {"name": 'Charlie', "city": 'New York'}
]

data2 = [
    {"gift": 'Doll', "quantity": 10},
    {"gift": 'Book', "quantity": 5},
    {"gift": 'Music CD', "quantity": 1}
]

table1 = drawTable(data1)
table2 = drawTable(data2)
with open("./Day15/output.txt", "w") as f:
    f.write(f"{table1}\n\n{table2}")
