def searchInsert(nums, target):
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)


list = [1, 3, 5, 6]

print(searchInsert(list, 2))
