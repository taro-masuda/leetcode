# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        ans = 0
        if root is None:
            return ans
        if root.val >= L and root.val <= R:
            ans += root.val
        if not root.right is None and root.val <= R:
            ans += self.rangeSumBST(root.right, L, R)
        if not root.left is None and root.val >= L:
            ans += self.rangeSumBST(root.left, L, R)
        return ans
