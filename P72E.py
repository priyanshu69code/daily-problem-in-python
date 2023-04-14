def addStrings(num1: str, num2: str) -> str:
    result = ""
    carry = 0
    i, j = len(num1) - 1, len(num2) - 1

    while i >= 0 or j >= 0:
        n1 = int(num1[i]) if i >= 0 else 0
        n2 = int(num2[j]) if j >= 0 else 0
        total = n1 + n2 + carry
        carry = total // 10
        result += str(total % 10)
        i -= 1
        j -= 1

    if carry:
        result += str(carry)

    return result[::-1]


print(addStrings("123", "456"))
# Output: "579"
