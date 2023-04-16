def assignCookies(greedFactors, cookieSizes):
    greedFactors.sort(reverse=True)
    cookieSizes.sort(reverse=True)
    contentChildren = 0
    i = 0
    j = 0
    while i < len(greedFactors) and j < len(cookieSizes):
        if greedFactors[i] <= cookieSizes[j]:
            contentChildren += 1
            i += 1
            j += 1
        else:
            i += 1
    return contentChildren

# greedFactors = [1, 2, 3]
# cookieSizes = [1, 1]
# Output: 1

# greedFactors = [1, 2]
# cookieSizes = [1, 2, 3]
# Output: 2