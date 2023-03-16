def is_anagram(s, t):
    if len(s) != len(t):
        return False

    s_counts = {}
    t_counts = {}

    for c in s:
        if c in s_counts:
            s_counts[c] += 1
        else:
            s_counts[c] = 1

    for c in t:
        if c in t_counts:
            t_counts[c] += 1
        else:
            t_counts[c] = 1

    for c in s:
        if s_counts[c] != t_counts.get(c, 0):
            return False

    return True