def hamming_distance(x: int, y: int) -> int:
    xor_result = x ^ y
    hamming_distance = 0
    while xor_result:
        hamming_distance += 1
        xor_result &= xor_result - 1
    return hamming_distance

x = 1
y = 4
print(hamming_distance(x, y)) # Output: 2