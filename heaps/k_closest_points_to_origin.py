# Given a list of points in the form [[x1, y1], [x2, y2], ... [xn, yn]] and an integer k, find the k closest points to the origin (0, 0) on the 2D plane.

# The distance between two points (x, y) and (a, b) is calculated using the formula:

# √(x1 - a2)2 + (y1 - b2)2
# Return the k closest points in any order.

# Example 1:

# Inputs:

# points = [[3,4],[2,2],[1,1],[0,0],[5,5]]
# k = 3
# Output:

# [[2,2],[1,1],[0,0]]
# Also valid:

# [[2,2],[0,0],[1,1]]
# [[1,1],[0,0],[2,2]]
# [[1,1],[2,2],[0,0]]
# ...
# [[0,0],[1,1],[2,2]]


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        # Your code goes here
        import heapq
        heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            if len(heap) < k:
                heapq.heappush(heap, (-distance, point))
            elif distance < -heap[0][0]:
                # heap root has the largest distance, chuck it and place new smaller distance in
                heapq.heappop(heap)
                heapq.heappush(heap, (-distance, point))

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result

