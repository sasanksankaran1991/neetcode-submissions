# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        
        if not root.left and not root.right:
            return root
        print(root.val)
        curr_left = root.left
        root.left = root.right
        root.right = curr_left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root




        