# Write a function that takes an array of unsorted integers nums and an integer k, and returns the kth largest element in the array. This function should run in O(n log k) time, where n is the length of the array.

# Example 1:

# Inputs:

# nums = [5, 3, 2, 1, 4]
# k = 2
# Output:

# 4


class Solution:
    def kthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif num > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]
