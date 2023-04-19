def findComplement(num: int) -> int:
    binary = bin(num)[2:]  # Remove the '0b' prefix
    complement = ''
    for bit in binary:
        complement += '0' if bit == '1' else '1'
    return int(complement, 2)

# Example usage:
print(findComplement(5))  # Output: 2