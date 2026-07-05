class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        new_list = dummy
        curr1 = list1
        curr2 = list2
        while curr1 and curr2:
            if curr1.val <= curr2.val:
                new_list.next = curr1
                curr1 = curr1.next
            else:
                new_list.next = curr2
                curr2 = curr2.next
            new_list = new_list.next
        
        new_list.next = curr1 if curr1 else curr2
        return dummy.next