def addDigits(num: int) -> int:
    while num > 9:
        num = sum(int(digit) for digit in str(num))
    return num