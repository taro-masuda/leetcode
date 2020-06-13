# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.dic = {}
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        orderList = []
        self.addOrder(root, 0, 0)
        for _, elem in sorted(self.dic.items()):
            ans = []
            for _, val in sorted(elem.items()):
                ans.extend(val)
            orderList.append(ans)
        return orderList
    def addOrder(self, root, depth, x):
        if root is None:
            return
        if not x in self.dic:
            self.dic[x] = {depth: [root.val]}
        elif not depth in self.dic[x]:
            self.dic[x][depth] = [root.val]
        else:
            self.dic[x][depth].append(root.val)
            self.dic[x][depth].sort()
        if root.left is not None:
            self.addOrder(root.left, depth+1, x-1)
        if root.right is not None:
            self.addOrder(root.right, depth+1, x+1)
