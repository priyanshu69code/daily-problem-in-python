def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 0
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:
            nums[slow] = nums[fast]
        slow += 1
    return nums


list = [1, 1, 2, 2, 3, 4, 4, 5, 5, 5]

print(removeDuplicates(list))
