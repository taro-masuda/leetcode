# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        out = [root.val]
        if root.right is not None:
            out.extend(self.rightSideView(root.right))
        if root.left is not None:
            left_view = self.rightSideView(root.left)
            if len(left_view) > len(out)-1:
                out.extend(left_view[len(out)-1:])
        return out
