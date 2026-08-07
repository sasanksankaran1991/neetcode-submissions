# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Find the end of the first half.
        # Using fast = head.next makes the split work cleanly
        # for both even and odd length lists.
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the list into two halves
        second = slow.next
        slow.next = None

        # Reverse the second half
        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # Merge the two halves alternately
        first, second = head, prev

        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next