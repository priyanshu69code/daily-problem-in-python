def findMaxConsecutiveOnes(nums: list[int]) -> int:
    start = 0
    end = 0
    max_len = 0
    
    while end < len(nums):
        if nums[end] == 0:
            max_len = max(max_len, end - start)
            start = end + 1
        end += 1
        
    max_len = max(max_len, end - start)
    
    return max_len

print(findMaxConsecutiveOnes([1,1,0,0,1,1,1])) # Output 3