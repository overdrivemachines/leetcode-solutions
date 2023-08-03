# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        result = False
        if head == None or head.next == None:
            return False

        my_set = set()
        node = head
        while node is not None:
            if node in my_set:
                return True
            else:
                # add node to set
                my_set.add(node)
            node = node.next
        return result