def reverse_string(s: str, k: int) -> str:
    s = list(s)
    for i in range(0, len(s), 2 * k):
        s[i:i+k] = reversed(s[i:i+k])
    return "".join(s)

>>> s = "abcdefg"
>>> k = 2
>>> reverse_string(s, k)
"bacdfeg"