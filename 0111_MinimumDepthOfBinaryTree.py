# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if not root.left is None:
            d_l = self.minDepth(root.left) + 1
        else:
            d_l = 1
        if not root.right is None:
            d_r = self.minDepth(root.right) + 1 
        else:
            d_r = 1
        
        if d_l == 1:
            return d_r
        elif d_r == 1:
            return d_l
        return min(d_l, d_r)
