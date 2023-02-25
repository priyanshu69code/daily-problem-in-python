def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
        print(result)
    return result


print(singleNumber([4, 1, 2, 1, 2]))
