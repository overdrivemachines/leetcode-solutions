# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = head
        right = head

        if head.next is None:
            # we only have a single node
            if n > 0:
                return None
            else:
                return head

        # move right pointer forward by n nodes
        for _ in range(n):
            right = right.next

        if right is None:
            # we have moved to the end of the list
            # we need to remove the head node and return the list
            head = head.next
            return head

        # move both left and right pointers forward until the right pointer reaches the end
        while right and right.next:
            left = left.next
            right = right.next

        # print("left: ", left.val)
        # print("right: ", right.val)

        if left and left.next:
            left.next = left.next.next

        # while head:
        #     print(head.val, end=" ")
        #     head = head.next

        return head