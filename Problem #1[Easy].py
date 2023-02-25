# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether 
# any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, 
# return true since 10 + 7 is 17

def numChecker(list,sum):
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if list[i] + list[j] == sum:
                return True
    return False

# Hash set Approch..............
def check_sum(numbers, k):
    seen = set()
    for num in numbers:
        if k - num in seen:
            return True
        seen.add(num)
    return False


list = [4,8,6,7,2,3,9]
sum = 17
print(check_sum(list,sum))
print(numChecker(list,sum))