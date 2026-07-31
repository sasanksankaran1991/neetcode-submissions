# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def sum_calculation(root, targetSum, path_sum):
            if not root:
                return False

            if not root.left and not root.right:
                path_sum += root.val
                if path_sum == targetSum:
                    print('final true')
                    return True
                else:
                    print('final false')
                    return False

            path_sum += root.val
            
            
            if sum_calculation(root.left, targetSum, path_sum):
                return True
            if sum_calculation(root.right, targetSum, path_sum):
                return True

            path_sum -= root.val
            return False

        if sum_calculation(root, targetSum, 0):
            print('v final, true')
            return True
        else:
            print('v final, false')
            return False

        