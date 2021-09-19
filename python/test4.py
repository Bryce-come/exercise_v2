def maxProductDifference(nums):
    # write code here
    nums.sort()
    a = nums[0]
    b = nums[1]

    c = nums[-1]
    d = nums[-2]
    ans = (c * d) - (a * b)
    return ans


nums = [5, 6, 2, 7, 4]

print(maxProductDifference(nums))
