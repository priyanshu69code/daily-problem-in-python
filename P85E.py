import re

def is_capitalized_correctly(word: str) -> bool:
    return bool(re.match(r'^([A-Z]+|[a-z]+|[A-Z][a-z]+)$', word))

word1 = "USA"
word2 = "leetcode"
word3 = "Google"
word4 = "gOOgle"
word5 = "12345"

print(is_capitalized_correctly(word1)) # True
print(is_capitalized_correctly(word2)) # True
print(is_capitalized_correctly(word3)) # True
print(is_capitalized_correctly(word4)) # False
print(is_capitalized_correctly(word5)) # False