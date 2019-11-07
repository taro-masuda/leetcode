# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        else:
            pointer = head.next
            l = [head.val]
            while pointer != None:
                l.append(pointer.val)
                pointer = pointer.next
            out = ListNode(l[-1])
            nextPointer = out
            for i in l[-2:-len(l)-1:-1]:
                nextPointer.next = ListNode(i)
                nextPointer = nextPointer.next

            return out
