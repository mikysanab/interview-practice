# Write a function to check if a person can attend all the meetings scheduled without any time conflicts. Given an array intervals, where each element [s1, e1] represents a meeting starting at time s1 and ending at time e1, determine if there are any overlapping meetings. If there is no overlap between any meetings, return true; otherwise, return false.

# Note that meetings ending and starting at the same time, such as (0,5) and (5,10), do not conflict.

# Input:

# intervals = [(1,5),(3,9),(6,8)]
# Output:

# false
# Explanation: The meetings (1,5) and (3,9) overlap.

# Input:

# intervals = [(10,12),(6,9),(13,15)]
# Output:

# true
# Explanation: There are no overlapping meetings, so the person can attend all.

class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        start_sorted = sorted(intervals, key = lambda x: x[0])
        for i in range(len(start_sorted) -1):
            current_end = start_sorted[i][1]
            next_start = start_sorted[i+1][0]
            if next_start < current_end:
                return False
        return True

print(Solution().canAttendMeetings([(1,5),(3,9),(6,8)]))