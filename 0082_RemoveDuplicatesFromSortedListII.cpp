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
        ListNode* ln = head;
        ListNode* out = head;
        ListNode* prev = head;
        while (ln != NULL && ln->next != NULL) {
            if (ln->val == ln->next->val) {
                while (ln->val == ln->next->val) {
                    ln->next = ln->next->next;
                    if (ln->next == NULL) {
                        if (out == ln) return NULL;
                        ln = NULL;
                        prev->next = NULL;
                        return out;
                    }
                }
                ln->val = ln->next->val;
                ln->next = ln->next->next;
            } else {
                prev = ln;
                ln = ln->next;
            }
        }
        return out;
    }
};
