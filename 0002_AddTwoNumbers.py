# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        updigit = 0
        ans_cur = ListNode(0, None)
        ans = ans_cur
        while l1 or l2:
            cur_sum = updigit
            if l1:
                cur_sum += l1.val
                l1 = l1.next
            if l2:
                cur_sum += l2.val
                l2 = l2.next
            updigit = cur_sum // 10
            ans_cur.val = cur_sum % 10
            if l1 or l2 or updigit > 0:
                ans_cur.next = ListNode(0, None)
                ans_cur = ans_cur.next
        if updigit > 0:
            ans_cur.val = updigit
        return ans
