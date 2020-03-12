
nums = [1, 2, 3, 4]
# 24 12 8 6


def funcname(nums):
    result = [1]*len(nums)
    resultback = [1]*len(nums)
    prev = 1
    
    for i in range(len(nums)):
        result[i] = prev
        prev *= nums[i]
    print(result)

    prev = 1
    for i in range(len(nums)-1, -1, -1):
        result[i] *= prev
        prev *= nums[i]

    print(result)
    return resultback


funcname(nums)
