def find_added_letter(s, t):
    char_count = [0] * 26 
    # assuming only lower case alphabets are present
    for ch in t:
        char_count[ord(ch) - ord('a')] += 1
    for ch in s:
        char_count[ord(ch) - ord('a')] -= 1
    for i in range(26):
        if char_count[i] == 1:
            return chr(i + ord('a'))