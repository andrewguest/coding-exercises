# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def merge_two_lists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        elif not l2:
            return l1

        if l1.val < l2.val:
            l1.next = self.merge_two_lists(l1.next, l2)

            return l1
        else:
            l2.next = self.merge_two_lists(l1, l2.next)

            return l2
