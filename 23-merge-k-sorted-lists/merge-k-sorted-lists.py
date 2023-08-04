# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # merge 2 linked lists list1 and list2
    def mergeList(self, list1, list2):
        head = ListNode()
        node = head
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        else:
            node.next = list2

        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if lists is None or len(lists) == 0:
            return None

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                # merge 2 linked lists together
                # eg. merge lists[0] and lists[1], in the next loop merge lists[2] and lists[3]
                if i + 1 < len(lists):
                    li = self.mergeList(lists[i], lists[i + 1])
                else:
                    li = self.mergeList(lists[i], None)

                # print the merged linked list
                # print("merged linked list:", end=" ")
                # self.print_linked_list(li)

                # add the merged linked list to mergedLists list
                mergedLists.append(li)

            lists = mergedLists

        return lists[0]