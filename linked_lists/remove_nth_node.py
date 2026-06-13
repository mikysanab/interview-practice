# Given a reference head of type ListNode that is the head node of a singly linked list and an integer n, write a function that removes the n-th node from the end of the list and returns the head of the modified list.

# Note: n is guaranteed to be between 1 and the length of the list. If n is the length of the list, the head of the list should be removed.

# Example 1:

# Input: n = 2

# 5
# 4
# 3
# 2
# 1
# head
# Output:

# 5
# 4
# 3
# 1
# head
# Explanation: The 2nd to last node is removed from the list.

# Example 2:

# Input: n = 5

# 5
# 4
# 3
# 2
# 1
# head
# Output:

# 4
# 3
# 2
# 1
# head
# Explanation: The 5th to last node is the head node, so it is removed.


class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return []
        # Your code goes here
        fast = slow = head
        for i in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        