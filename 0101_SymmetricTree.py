# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode, depth: List[int]) -> (List[int], List[int]):
        if root == None:
            return [],[]
        out = []
        depths = []
        
        if root.left != None:
            ext, d = self.inorderTraversal(root.left, depth+1)
            out.extend(ext)
            depths.extend(d)
        elif root.right != None:
            out.append(None)
            depths.append(depth+1)
            
        out.append(root.val)
        depths.append(depth)
        
        if root.right != None:
            ext, d = self.inorderTraversal(root.right, depth+1)
            out.extend(ext)
            depths.extend(d)
        elif root.left != None:
            out.append(None)
            depths.append(depth+1)
                
        return out, depths

    def isSymmetric(self, root: TreeNode) -> bool:
        l_root, depths = self.inorderTraversal(root, 0)
        for i, _ in enumerate(l_root):
            if l_root[i] != l_root[len(l_root)-i-1] or depths[i] != depths[len(l_root)-i-1]:
                return False
        return True
