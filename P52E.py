def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    mapping = {}
    for i, char in enumerate(pattern):
        if char not in mapping:
            if words[i] in mapping.values():
                return False
            mapping[char] = words[i]
        else:
            if mapping[char] != words[i]:
                return False
    return True
