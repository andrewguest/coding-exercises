from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        temp_list = head

        while temp_list.next is not None:
            if temp_list.val == temp_list.next.val:
                temp_list.next = temp_list.next.next
            else:
                temp_list = temp_list.next

        return head
