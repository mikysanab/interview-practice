# DESCRIPTION
# Given an array of integers nums and an integer k, find the maximum sum of any contiguous subarray of size k.

# Example 1: Input:

# nums = [2, 1, 5, 1, 3, 2]
# k = 3
# Output:

# 9
# Explanation: The subarray with the maximum sum is [5, 1, 3] with a sum of 9.


class Solution:
    def max_sum(self, nums, k):
        if len(nums) < k:
            return
        max_sum = float('-inf')
        start = 0
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            if i - start + 1 == k:
                max_sum = max(current_sum, max_sum)
                current_sum -= nums[start]
                start += 1
        return max_sum

print(Solution().max_sum([2,1,5,1,3,2], 3))