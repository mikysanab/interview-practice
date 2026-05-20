# DESCRIPTION (inspired by Leetcode.com)
# Given an array heights where each element represents the height of a vertical line, pick two lines to form a container. 
# Return the maximum area (amount of water) the container can hold.

# What is area? Width × height, where width is the distance between walls, and height is the shorter wall 
# (water overflows at the shorter wall).

# Example 1:

# max (21)
# heights = [3, 4, 1, 2, 2, 4, 1, 3, 2]
# Output:

# 21  # walls at indices 0 and 7 (both height 3): width=7, height=3, area=21
# Example 2:

# heights = [1, 2, 1]
# Output:

# 2  # walls at indices 0 and 2: width=2, height=min(1,1)=1, area=2



def max_area(heights: list[int]) -> int:
    left = 0
    right = len(heights) - 1
    best = 0
    while left < right:
        area = min(heights[left], heights[right]) * (right-left)
        best = max(area, best)
        if heights[left] <= heights[right]:
            left += 1
        else:
            right -= 1
    return best

print(max_area([3,4,1,2,2,4,1,3,2]))
print(max_area([1,2,1]))
print(max_area([1,1,2,3,6,8,3,2,1]))