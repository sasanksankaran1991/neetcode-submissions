from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append(root)

        level_list = []
        final_results = []
        level = 0
        while len(queue) > 0:
            for x in range(len(queue)): 
                curr = queue.popleft()
                if level not in level_list:
                    final_results.append(curr.val)
                    level_list.append(level)
                    # print(curr.val)

                if curr.right:
                    queue.append(curr.right)
                if curr.left:
                    queue.append(curr.left)
            level+=1

        return final_results

        
        
        