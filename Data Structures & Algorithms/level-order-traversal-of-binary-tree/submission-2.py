# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        queue = deque()
        queue.append(root)
        # print(len(queue))

        # level = 0
        final_list = []
        while len(queue) > 0:
            sub_list = []
            # print('***')
            for i in range(len(queue)):
                curr = queue.popleft()
                # print(curr.val)
                sub_list.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            final_list.append(sub_list)
            # level+=1
        return final_list


        