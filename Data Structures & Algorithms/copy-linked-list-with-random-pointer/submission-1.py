"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':        

        if not head:
            return None

        curr_node = head
        # new_node = Node(curr_node.val)
        old_to_new = {}
        # new_node_dummy = new_node
        # old_to_new[curr_node] = new_node_dummy
        # curr_node = curr_node.next


        while curr_node:
            old_to_new[curr_node] = Node(curr_node.val)
            # print(curr_node.val, new_node_dummy.val)
            curr_node = curr_node.next
            # new_node_dummy = new_node_dummy.next

        for key, values in old_to_new.items():
            # key is orginal
            # values are clone
            if key.next is None:
                values.next = None
            else:
                values.next = old_to_new[key.next]

            if key.random is None:
                values.random = None
            else:
                values.random = old_to_new[key.random]

        return old_to_new[head]

