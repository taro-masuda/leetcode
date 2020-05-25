# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        out = []
        
        if root.left != None:
            out.extend(self.inorderTraversal(root.left))
            
        out.append(root.val)
        
        if root.right != None:
            out.extend(self.inorderTraversal(root.right))
                
        return out
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        list_elements = self.inorderTraversal(root)
        return list_elements[k-1]
