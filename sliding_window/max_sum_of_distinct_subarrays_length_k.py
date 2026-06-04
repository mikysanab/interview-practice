# Given an integer array nums and an integer k, write a function to identify the highest possible sum of a subarray within nums, where the subarray meets the following criteria: its length is k, and all of its elements are unique. If no such subarray exists, return 0.

# Example 1: Input:

# nums = [3, 2, 2, 3, 4, 6, 7, 7, -1]
# k = 4
# Output:

# 20
# Explanation: The subarrays of nums with length 4 are:

# [3, 2, 2, 3] # elements 3 and 2 are repeated.
# [2, 2, 3, 4] # element 2 is repeated.
# [2, 3, 4, 6] # meets the requirements and has a sum of 15.
# [3, 4, 6, 7] # meets the requirements and has a sum of 20.
# [4, 6, 7, 7] # element 7 is repeated.
# [6, 7, 7, -1] # element 7 is repeated.
# We return 20 because it is the maximum subarray sum of all the subarrays that meet the conditions.

# Example 2: Input:

# nums = [5, 5, 5, 5, 5]
# k = 3
# Output:

# 0
# Explanation: Every subarray of length 3 contains duplicate elements, so no valid subarray exists. Return 0.


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        if len(nums) < k:
            return 0
        current = 0
        largest = float('-inf')
        left = 0
        present = {}
        valid = False
        for right in range(len(nums)):
            current += nums[right]
            if right - left +1 >= k:
                #only include result if there are no repeats in the window
                if len(set(nums[left:right+1])) == k:
                    largest = max(current, largest)
                    valid = True
                current -= nums[left]
                left+=1
        if valid:
            return largest
        else:
            return 0

print(Solution().maxSum([3,2,2,3,4,6,7,7,-1], 4))