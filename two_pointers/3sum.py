# Given an input integer array nums, write a function to find all unique triplets [nums[i], nums[j], nums[k]] such that i, j, and k are distinct indices, and the sum of nums[i], nums[j], and nums[k] equals zero. Ensure that the resulting list does not contain any duplicate triplets.

# Input:

# nums = [-1,0,1,2,-1,-1]
# Output:

# [[-1,-1,2],[-1,0,1]]
# Explanation: Both nums[0], nums[1], nums[2] and nums[1], nums[2], nums[4] both include [-1, 0, 1] and sum to 0. nums[0], nums[3], nums[4] ([-1,-1,2]) also sum to 0.

# Since we are looking for unique triplets, we can ignore the duplicate [-1, 0, 1] triplet and return [[-1, -1, 2], [-1, 0, 1]].

# # The order of the triplets and the order of the elements within the triplets do not matter.


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        sortednums = sorted(nums)
        first = 0
        final = []
        # [-1, -1, -1, 0, 1, 2]
        for first in range(len(sortednums) - 2):
            if sortednums[first] > 0 or (first > 0 and sortednums[first] == sortednums[first - 1]):
                continue
            results = self.two_sum(sortednums[first + 1:], 0-sortednums[first])
            final.extend(results)
        return final



    def two_sum(self, sortednums: list[int], target) -> list[list[int]]:
        left = 0
        right = len(sortednums) - 1
        results = []
        while left < right:
            sum = sortednums[left] + sortednums[right]
            if sum == target:
                results.append([0-target, sortednums[left], sortednums[right]])
                left += 1
            elif sum < target:
                left += 1
            else:
                right -= 1
        return results

# print(Solution().threeSum([-1,0,1,2,-1,-1]))
# print(Solution().threeSum([-2, -1, -1, -1, -1, 0, 0, 0, 0]))
# print(Solution().threeSum([-2, 1, 1]))