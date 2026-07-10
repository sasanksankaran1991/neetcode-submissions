# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergingoperation(self, arr1, arr2):
        i = 0
        j = 0
        new_arr = []

        while (i <= len(arr1)) and (j <= len(arr2)):

            if (i == len(arr1)) and (j == len(arr2)):
                return new_arr
            elif i == len(arr1):
                new_arr = new_arr + arr2[j:]
                j = len(arr2)
            elif j == len(arr2):
                new_arr = new_arr + arr1[i:]
                i = len(arr1)
            elif arr1[i] <= arr2[j]:
                new_arr.append(arr1[i])
                i+=1
            else:
                new_arr.append(arr2[j])
                j+=1
        return new_arr


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        new_list = []
        for x in lists:  
            new_dummy_list = []
            while x:
                new_dummy_list.append(x.val)
                x = x.next
            new_list.append(new_dummy_list)
        print(new_list)

        new_arr = []
        new_arr = self.mergingoperation(new_arr, new_list[0])

        for x in range(1, len(new_list)):
            new_arr = self.mergingoperation(new_arr, new_list[x])

        print(new_arr)

        dummy = ListNode(0)
        current = dummy

        for x in new_arr:
            current.next = ListNode(x)
            current = current.next

        return dummy.next



                    


        