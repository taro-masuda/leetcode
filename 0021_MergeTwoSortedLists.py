# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if(l1 == None and l2 == None):
            return None
        elif l1 == None:
            return l2
        elif l2 == None:
            return l1
        
        l = []
        
        while not (l1 == None and l2 == None):
            if l1 == None:
                l.append(l2.val)
                l2 = l2.next
                continue
            if l2 == None:
                l.append(l1.val)
                l1 = l1.next
                continue
            if l1.val == l2.val:
                l.append(l1.val)
                l1 = l1.next
                l.append(l2.val)
                l2 = l2.next
            elif l1.val < l2.val:
                l.append(l1.val)
                l1 = l1.next                
            else:
                l.append(l2.val)
                l2 = l2.next
        
        tmp_tree = ListNode(l[-1])
        for c in l[-2:-len(l)-1:-1]:
            out = ListNode(c)
            out.next = tmp_tree
            tmp_tree = out
        
        return out
