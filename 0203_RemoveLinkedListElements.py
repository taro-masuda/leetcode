# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return head
        while head.val == val:
            head = head.next
            if head is None:
                return head
        node = head
        while node is not None:
            if node.next is None:
                break
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return head
