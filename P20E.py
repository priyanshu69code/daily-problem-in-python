def getRow(rowIndex: int):
    result = []
    for k in range(rowIndex + 1):
        c = 1
        for i in range(1, k + 1):
            c = c * (rowIndex - k + i) // i
        result.append(c)
    return result
