# Given an integer array nums, write a function to rearrange the array by moving all zeros to the end while keeping the order of non-zero elements unchanged. Perform this operation in-place without creating a copy of the array.

# Input:

# nums = [2,0,4,0,9]
# Output:

# [2,4,9,0,0]


class Solution:
    def move_zeroes(self, nums):
        parking = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[parking], nums[i] = nums[i], nums[parking]
                parking += 1
        return nums

print(Solution().move_zeroes([2, 0,4,0,9]))


