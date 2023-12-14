// Definition for singly-linked list.
class ListNode {
  int val;
  ListNode? next;
  ListNode([this.val = 0, this.next]);
}

class Solution {
  ListNode? deleteDuplicates(ListNode? head) {
    // checking the value if it's empty or NULL
    if (head == null || head.next == null) return head;

    // first value in the list node
    ListNode? first = head;

    // second value in the list node
    ListNode? second = head.next;

    // assuming that second value is not NULL
    while (second != null) {
      // if the second value is same as first
      if (second.val == first?.val) {
        // then we will assign the second value as the third value -: first.next = second value
        first?.next = second.next;
        // then that third value is same as the second value
        second = second.next;
      } else {
        // if not first will be same as second value
        first = second;
        // second value will be same as third value
        second = second.next;
      }
    }

    return head;
  }
}
