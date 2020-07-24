# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.q = [root]
        if not root:
            self.largestcalled = True
            return 
        node = root
        while node.left:
            node = node.left
            self.q.append(node) 
        self.smallest = node
        node = root
        while node.right:
            node = node.right
        self.largest = node
        self.smallestcalled = False
        self.largestcalled = False

    def next(self) -> int:
        """
        @return the next smallest number
        """
        cur = self.q[-1]
        if not self.smallestcalled:
            self.smallestcalled = True
            if self.smallest == self.largest:
                self.largestcalled = True
            return self.smallest.val
        elif cur.right:
            self.q.append(cur.right)
            while self.q[-1].left:
                self.q.append(self.q[-1].left)
            if self.q[-1] == self.largest:
                self.largestcalled = True
            return self.q[-1].val
        else:
            curval = cur.val
            self.q.pop(-1)
            while self.q[-1].val < curval:
                if len(self.q) == 1:
                    self.q.append(self.q[0].right)
                    break
                self.q.pop(-1)
            if self.q[-1] == self.largest:
                self.largestcalled = True
            return self.q[-1].val
        
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return not self.largestcalled
        

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
