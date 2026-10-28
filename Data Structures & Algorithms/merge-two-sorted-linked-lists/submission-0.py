# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        p1 = list1
        p2 = list2

        res = ListNode()
        tail = res

        while p1 and p2:
            if p1.val <= p2.val:
                tail.next = p1
                p1 = p1.next
            else:
                tail.next = p2
                p2 = p2.next

            tail = tail.next

        # Attach whichever list still has nodes
        tail.next = p1 if p1 else p2

        return res.next