# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ancestor = None
        self.depth = -1
        self.parentq = set()
        self.parentp = set()
        
    def found(self, root: 'TreeNode', p: 'TreeNode', depth: int, isP: bool) -> bool:
        if isP:
            parentset = self.parentp
        else:
            parentset = self.parentq
        if root in parentset:
            return True
        found = False
        if root is None:
            return False
        if root == p:
            parentset.add(root)
            return True
        if root.right:
            if self.found(root.right, p, depth+1, isP):
                parentset.add(root)
                parentset.add(root.right)
                return True
        if root.left:
            if self.found(root.left, p, depth+1, isP):
                parentset.add(root)
                parentset.add(root.left)
                return True
        return False
    
    def commonAncestorAndDepth(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode', depth: int) -> None:
        if root is None:
            return
        if self.found(root, p, depth, True) and self.found(root, q, depth, False):
            if depth > self.depth:
                self.depth = depth
                self.ancestor = root
        if root.left:
            self.commonAncestorAndDepth(root.left, p, q, depth+1)
        if root.right:
            self.commonAncestorAndDepth(root.right, p, q, depth+1)
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.commonAncestorAndDepth(root, p, q, 0)
        return self.ancestor
