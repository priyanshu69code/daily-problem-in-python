def titleToNumber(columnTitle: str) -> int:
    result = 0
    for c in columnTitle:
        value = ord(c) - ord('A') + 1
        result = result * 26 + value
    return result


print(titleToNumber("A"))    # Output: 1
print(titleToNumber("AB"))   # Output: 28
print(titleToNumber("ZY"))   # Output: 701
print(titleToNumber("FXSHRXW"))  # Output: 2147483647
