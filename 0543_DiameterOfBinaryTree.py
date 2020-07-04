# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.maxlen = 0
        self.isRoot = True
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        isRoot = self.isRoot
        self.isRoot = False
        if root == None:
            return 0
        if root.right == None and root.left == None:
            return 0
        else:
            r = self.diameterOfBinaryTree(root.right)
            l = self.diameterOfBinaryTree(root.left) 
            if r > 0 or not root.right is None:
                r += 1
            if l > 0 or not root.left is None:
                l += 1
            self.maxlen = max(self.maxlen, r+l)
        if isRoot:
            return max(r+l, self.maxlen)
        else:
            return max(r,l)
