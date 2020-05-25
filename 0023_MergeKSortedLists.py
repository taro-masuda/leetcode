# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dic = {}
        minval = 10**9
        maxval = -10**9
        for ln in lists:
            ls = ln
            while ls is not None:
                minval = min(minval, ls.val)
                maxval = max(maxval, ls.val)
                if ls.val not in dic:
                    dic[ls.val] = 1
                else:
                    dic[ls.val] += 1
                ls = ls.next
        if minval == 10**9:
            return None
        out = ListNode()
        out_copy = out
        for i in range(minval,maxval+1):
            if not i in dic:
                continue
            for j in range(dic[i]):
                out_copy.val = i
                if i == maxval and j == dic[i]-1:
                    break
                out_copy.next = ListNode()
                out_copy = out_copy.next
        return out
