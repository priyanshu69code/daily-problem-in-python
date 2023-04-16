def can_concatenate(s):
    n = len(s)
    lps = [0] * n
    i, j = 1, 0
    while i < n:
        if s[i] == s[j]:
            j += 1
            lps[i] = j
            i += 1
        elif j > 0:
            j = lps[j-1]
        else:
            lps[i] = 0
            i += 1
    l = lps[-1]
    return l > 0 and n % (n - l) == 0

# Example usage:
print(can_concatenate("abcabcabc"))  # True
print(can_concatenate("abcdabcd"))  # False