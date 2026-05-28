# Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle.

# For three sides to form a valid triangle, all three of these conditions must hold: (a + b > c), (a + c > b), and (b + c > a), where (a), (b), and (c) are the side lengths. In other words, the sum of every possible pair must exceed the third side.

# Valid triangle requires:
# a + b > c AND a + c > b AND b + c > a
# (every pair must sum to more than the third side)
# The triplets do not need to be unique.

# Example:

# Input:

# nums = [11,4,9,6,15,18]
# Output:

# 10
# Explanation: Valid combinations are...

# 4, 15, 18
# 6, 15, 18
# 9, 15, 18
# 11, 15, 18
# 9, 11, 18
# 6, 11, 15
# 9, 11, 15
# 4, 6, 9 

class Solution:
    def triangleNumber(self, nums:list[int]) -> int:
        sorted_nums = sorted(nums, reverse=True)
        count = 0
        for i in range(len(sorted_nums) - 2):
            largest = sorted_nums[i]
            left = i+1
            right = len(sorted_nums) - 1
            while left < right:
                leftnum = sorted_nums[left]
                rightnum = sorted_nums[right]
                if leftnum + rightnum <= largest:
                    right -= 1
                else:
                    count += right - left
                    left += 1
        return count

print(Solution().triangleNumber([11,4,9,6,15,18]))


class AISolution:
    def triangleNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        for k in range(len(nums) - 1, 1, -1):
            left, right = 0, k - 1
            while left < right:
                if nums[left] + nums[right] > nums[k]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count

print(AISolution().triangleNumber([11,4,9,6,15,18]))