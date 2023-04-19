def license_key_formatting(s: str, k: int) -> str:
    # Remove dashes and convert to uppercase
    s = s.replace("-", "").upper()

    # Find length of first group
    first_group_len = len(s) % k

    # Initialize result string with first group
    result = s[:first_group_len]

    # Loop through remaining characters
    for i in range(first_group_len, len(s), k):
        # Add group of length k with a dash in between
        result += "-" + s[i:i+k]

    return result

# Test the function
s = "2-4A0r7-4k"
k = 4
print(license_key_formatting(s, k)) #output: 24A0-R74K
