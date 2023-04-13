def thirdMax(nums):
    nums = list(set(nums))
    if len(nums) < 3:
        return max(nums)
    nums.sort(reverse=True)
    count = 0
    for i in range(len(nums)):
        if count == 2:
            return nums[i]
        if i > 0 and nums[i] < nums[i-1]:
            count += 1
    return nums[0]