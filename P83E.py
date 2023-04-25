def convertToBase7(num: int) -> str:
    if num == 0:
        return "0"
    is_negative = num < 0
    num = abs(num)
    result = ""
    while num > 0:
        result += str(num % 7)
        num //= 7
    if is_negative:
        result += "-"
    return result[::-1]

assert convertToBase7(100) == "202"
assert convertToBase7(-7) == "-10"
assert convertToBase7(0) == "0"