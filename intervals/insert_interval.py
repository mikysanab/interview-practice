# Given a list of intervals intervals and an interval newInterval, write a function to insert newInterval into a list of existing, non-overlapping, and sorted intervals based on their starting points. The function should ensure that after the new interval is added, the list remains sorted without any overlapping intervals, merging them if needed.

# Two intervals are considered overlapping if they share any common time, including if one ends exactly when another begins (e.g., [1,4] and [4,7] overlap and should be merged into [1,7]).

# Input:

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# Output:

# [[1,5],[6,9]]
# Explanation: The new interval [2,5] overlaps with [1,3], so they are merged into [1,5].

# Input:

# intervals = [[1,2],[3,5],[6,7],[8,10]]
# newInterval = [5,6]
# Output:

# [[1,2],[3,7],[8,10]]
# Explanation: The new interval [5,6] touches [3,5] and [6,7], so all three are merged into [3,7].


class Solution:
    def insertIntervals(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        result = []
        n = len(intervals)
        i = 0

        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][1], newInterval[1])
            i+= 1
        
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i+=1
    
        return result
        


print(Solution().insertIntervals([[1,2],[3,5],[6,7],[8,10]], [5,6]))
# newInterval = [5,6]))