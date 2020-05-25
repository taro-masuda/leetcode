# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import copy

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None:
            return None
        
        l_odd = []
        l_even = []
        i = 1
        while head != None:
            if i % 2 == 1:
                l_odd.append(head.val)
                head = head.next
            else:
                l_even.append(head.val)
                head = head.next
            i += 1
            
        out = None
        
        while len(l_even) > 0:
            tmp = copy.copy(out)
            out = ListNode(l_even[-1])
            l_even.pop(-1)
            out.next = tmp
        while len(l_odd) > 0:
            tmp = copy.copy(out)
            out = ListNode(l_odd[-1])
            l_odd.pop(-1)
            out.next = tmp

        return out
