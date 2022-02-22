def solve(nums, div):
    length = len(nums)
    for i in range(length):
        nums[i] = nums[i] + (nums[i] % div)
    return nums
    