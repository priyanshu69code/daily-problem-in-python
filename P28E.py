def convertToTitle(columnNumber: int) -> str:
    title = ''
    while columnNumber > 0:
        remainder = (columnNumber - 1) % 26
        title += chr(ord('A') + remainder)
        columnNumber = (columnNumber - 1) // 26
    return title[::-1]
