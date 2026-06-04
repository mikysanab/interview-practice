# Write a function to return the minimum number of intervals that must be removed from a given array intervals, where intervals[i] consists of a starting point starti and an ending point endi, to ensure that the remaining intervals do not overlap.

# Input:

# intervals = [[1,3],[5,8],[4,10],[11,13]]
# Output:

# 1
# Explanation: Removing the interval [4,10] leaves all other intervals non-overlapping.

# [[0,2147483647],[-2147483648,-2147483647],[-2147483647,0]]

class Solution:
    def nonOverlappingIntervals(self, intervals: list[list[int]]) -> int:
        # Your code goes here
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        print(sorted_intervals)
        count = 0
        end = float('-inf')
        i= 0
        while i < len(intervals):
            if sorted_intervals[i][0] < end:
                print('collision', sorted_intervals[i], end)
                # collision, resolve by taking lesser end
                if end <= sorted_intervals[i][1]:
                    # next interval ends later, remove and skip
                    count +=1
                    i += 1
                else:
                    #next interval ends earlier, remove previous and continue
                    end = sorted_intervals[i][1]
                    count += 1
                    i += 1
            else:
                end = sorted_intervals[i][1]
                i += 1
        return count

print(Solution().nonOverlappingIntervals([[0,2147483647],[-2147483648,-2147483647],[-2147483647,0]]))

