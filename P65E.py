def can_construct_ransom_note(ransomNote: str, magazine: str) -> bool:
    # Step 1
    frequency = {}
    for c in magazine:
        if c in frequency:
            frequency[c] += 1
        else:
            frequency[c] = 1

    # Step 2
    for c in ransomNote:
        if c not in frequency or frequency[c] == 0:
            return False
        frequency[c] -= 1

    return True
