# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def eachlevelOrder(self, root: TreeNode, depth: int, l: List[List[int]]) -> List[List[int]]:
        while depth >= len(l):
            l.append([])
        l[depth].append(root.val)
        if root.left != None:
            l = self.eachlevelOrder(root.left, depth+1, l)
        if root.right != None:
            l = self.eachlevelOrder(root.right, depth+1, l)
        return l
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        l = []
        if root == None:
            return l
        out = self.eachlevelOrder(root, 0, l)
        return out
