# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        if root.val == sum and root.left is None and root.right is None:
            return True
        if not root.left is None:
            if self.hasPathSum(root.left, sum-root.val):
                return True
        if not root.right is None:
            if self.hasPathSum(root.right, sum-root.val):
                return True
        return False
