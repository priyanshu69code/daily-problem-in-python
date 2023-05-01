def reverse_str(s: str, k: int) -> str:
    # convert string to list of characters for easy manipulation
    chars = list(s)
    n = len(chars)
    
    # iterate over the string and reverse every 2k characters
    for i in range(0, n, 2*k):
        left = i
        right = min(i + k - 1, n - 1)
        
        # reverse the first k characters
        while left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1
    
    return "".join(chars)