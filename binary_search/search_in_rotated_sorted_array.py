# You are given a sorted array that has been rotated at an unknown pivot point, along with a target value. Develop an algorithm to locate the index of the target value in the array. If the target is not present, return -1. The algorithm should have a time complexity of O(log n).

# Note:

# The array was originally sorted in ascending order before being rotated.
# The rotation could be at any index, including 0 (no rotation).
# You may assume there are no duplicate elements in the array.
# Example 1:
# Input:

# nums = [4,5,6,7,0,1,2], target = 0
# Output: 4 (The index of 0 in the array)

# Example 2:

# Input:

# nums = [4,5,6,7,0,1,2], target = 3
# Output: -1 (3 is not in the array)

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # Your code goes here
        if len(nums) == 0:
            return -1
        rotation_index = self.find_rotation_index(nums)
        search_list = nums[rotation_index:] + nums[:rotation_index]
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right + left) // 2

            if search_list[mid] == target:
                return (mid + rotation_index) % len(nums)
            if search_list[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1 

    
    def find_rotation_index(self, nums:list[int]) -> int:
        left = 0
        right = len(nums) - 1
        last = nums[right]
        first = nums[left]
        if nums[left] < nums[right]:
            return 0
        if len(nums) == 1:
            return 0
        while left <= right:
            mid = ((right + left )//2)

            if nums[mid] <= last:
                if nums[mid] < nums[mid-1]:
                    return mid
                else:
                    right = mid - 1
            else:
                left = mid + 1
        return -1


print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([4,5,6,7,0,1,2], 5))
print(Solution().search([2,1], 1))
print(Solution().search([1], 1))