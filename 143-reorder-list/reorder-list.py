# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:


    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        # count the number of nodes in the list
        temp = head
        count = 0
        while temp:
            count += 1
            # print(temp.val, end=" ")
            temp = temp.next

        hasRemainder = False
        if count % 2 != 0:
            hasRemainder = True

        # get the middle node and the middle's previous node
        temp = head
        count = count // 2
        mid = None
        prevMid = None
        nextMid = None
        while count > 0:
            prevMid = temp
            temp = temp.next
            mid = temp
            count -= 1

        prevMid.next = None
        nextMid = mid.next

        # print("\nprevMid:", prevMid.val)
        # print("mid:", mid.val)
        # print("temp:", temp.val)

        # Reversing the linked list from the middle node to the tail node
        # 1, 2, 3, 4, 5
        node = mid
        new_head = None
        while node:
            nextNode = node.next
            node.next = new_head
            new_head = node
            node = nextNode

        mid = new_head

        # Now we have 2 list. 1st is the 1st half starting with "head" and
        # 2nd is the 2nd half starting with "mid"

        nodeX = head
        nodeY = mid
        nodeYnext = None

        # 1, 2, 3 | 5, 4

        # print("List:")
        while nodeX:
            # print(nodeX.val, end=" ")
            nodeXnext = nodeX.next
            nodeYnext = nodeY.next

            # nodeX's next is nodeY
            nodeX.next = nodeY
            # nodeY's next is nodeXnext
            nodeY.next = nodeXnext
            # nodeX is nodeXnext
            nodeX = nodeXnext
            # nodeY is nodeYnext
            nodeY = nodeYnext

        if nodeYnext and hasRemainder:
            nextMid.next = nodeYnext
            # print("nodeYnext:", nodeYnext.val)
            # print("count:", count)
            # print("count%2", count % 2)

