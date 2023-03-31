def reverse_vowels(s):
    vowels = set('aeiouAEIOU')
    lst = list(s)
    left, right = 0, len(lst) - 1
    while left < right:
        if lst[left] in vowels and lst[right] in vowels:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
            right -= 1
        elif lst[left] in vowels:
            right -= 1
        else:
            left += 1
    return ''.join(lst)
