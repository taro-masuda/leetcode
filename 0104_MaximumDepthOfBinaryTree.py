# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        else:
            if root.left != None:
                left = self.maxDepth(root.left)
            else:
                left = 0
            if root.right != None:
                right = self.maxDepth(root.right)
            else:
                right = 0
        
        return max(left, right) + 1
