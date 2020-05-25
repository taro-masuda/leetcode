# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxVal(self, root: TreeNode):
        max_val = root.val
        if root.left is not None:
            max_val = max(max_val, self.maxVal(root.left))
        if root.right is not None:
            max_val = max(max_val, self.maxVal(root.right))
        return max_val
    def minVal(self, root: TreeNode):
        min_val = root.val
        if root.left is not None:
            min_val = min(min_val, self.maxVal(root.left))
        if root.right is not None:
            min_val = min(min_val, self.maxVal(root.right))
        return min_val
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is not None:
            if not self.maxVal(root.left) < root.val:
                return False
            if not self.isValidBST(root.left):
                return False
        if root.right is not None:
            if not root.val < self.minVal(root.right):
                return False
            if not self.isValidBST(root.right):
                return False
        return True
