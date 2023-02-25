def fun(list):
    newlist = []
    for i in range(len(list)):
        num = 1
        for j in range(len(list)):
            if j != i:
                num *= list[j]
        newlist.append(num)
    return newlist


list = [1, 2, 3, 4, 5]

# print(fun(list))


# def product_except_self(nums):
#     n = len(nums)
#     result = [1] * n
#     for i in range(1, n):
#         result[i] = result[i-1] * nums[i-1]
#     right_product = 1
#     for i in range(n-1, -1, -1):
#         result[i] *= right_product
#         right_product *= nums[i]
#     return result


def product_except_self(nums):
    n = len(nums)
    result = 1
    for num in nums:
        result *= num
    result = [result] * n

    for i in range(n-1, -1, -1):
        result[i] = result[i] // nums[i]
    return result


nums = [1, 2, 3, 4, 5]
print(product_except_self(nums))

output:
[120, 60, 40, 30, 24]
