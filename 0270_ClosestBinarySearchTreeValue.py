# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.closest_val = 2**64
    def closestValue(self, root: TreeNode, target: float) -> int:
        if abs(root.val - target) < abs(self.closest_val - target):
            self.closest_val = root.val
        if root.right:
            if abs(self.closestValue(root.right, target) - target) < abs(self.closest_val - target):
                self.closest_val = root.right.val
        if root.left:
            if abs(self.closestValue(root.left, target) - target) < abs(self.closest_val - target):
                self.closest_val = root.left.val
        return self.closest_val
