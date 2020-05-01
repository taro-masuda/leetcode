/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* cur = head;
        while (cur != NULL) {
            if (cur->next == NULL) break;
            ListNode* next = cur->next;
            while (cur->val == cur->next->val) {
                cur->next = cur->next->next;
                if (cur->next == NULL) break;
            }
            cur = cur->next;
        }
        return head;
    }
};
