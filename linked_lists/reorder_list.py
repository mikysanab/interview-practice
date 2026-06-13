# Given a reference head of type ListNode that is the head of a singly linked list, reorder the list in-place such that the nodes are reordered to form the following pattern:

# 1st node -> last node -> 2nd node -> 2nd to last node -> 3rd node ...

# Example 1: input:

# 5
# 4
# 3
# 2
# 1
# head
# output:

# 5
# 1
# 4
# 2
# 3
# head
# Example 2: input:

# 0
# 1
# 2
# head
# output:

# 0
# 2
# 1



class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode' = None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        # copy the original list and store head
        copy = ListNode(head.val)
        copy_head = copy
        prev = None
        current = head

        lencount = 0

        # reverse the list while populating copy
        while current:
            if current.next:
                copy.next = ListNode(current.next.val)
                copy = copy.next  

            temp = current.next

            current.next = prev
            prev = current
            current = temp
            lencount += 1

        # print_list(copy_head, 'copy')
        # print_list(prev, 'reversed')

        # merge the lists into a new copy
        current = ListNode(0)
        result_head = current

        for_current = copy_head
        rev_current = prev
        count = 0
        while count < lencount:
            #print_list(result_head, 'building')
            count += 1
            #alternate
            if count % 2 == 0:
                current.next = ListNode(rev_current.val)
                rev_current = rev_current.next
            else:
                # add the next entry from original list.
                current.next = ListNode(for_current.val)
                for_current = for_current.next
            current = current.next
            
        # print_list(result_head, 'final')
        return result_head.next

def print_list(node, label=""):
    vals = []
    seen = set()
    while node and id(node) not in seen:
        seen.add(id(node))
        vals.append(str(node.val))
        node = node.next
    print(f"{label}: {' -> '.join(vals)}")

testHead = ListNode(1, ListNode(2, ListNode(3, ListNode(4, None))))

Solution().reorderList(testHead)


