def longest_palindrome(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    palindrome_len = 0
    has_odd_count = False
    for count in char_count.values():
        if count % 2 == 0:
            palindrome_len += count
        else:
            palindrome_len += count - 1
            has_odd_count = True

    if has_odd_count:
        palindrome_len += 1

    return palindrome_len


print(longest_palindrome("abccccdd"))  # Output: 7
print(longest_palindrome("a"))  # Output: 1
print(longest_palindrome("abcde"))  # Output: 1