/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* out = new ListNode(NULL);
        ListNode* out_copy = out;
        int countup = 0;
        while ((l1 != NULL || l2 != NULL) || countup == 1){
            if(l1 != NULL && l2 != NULL) {
                out_copy->val = (l1->val + l2->val + countup) % 10;
                countup = (l1->val + l2->val + countup)/10 % 10;
            } else if (l1 == NULL && l2 != NULL) {
                out_copy->val = (l2->val + countup) % 10;
                countup = (l2->val + countup)/10 % 10;
            } else if (l1 != NULL && l2 == NULL) {
                out_copy->val = (l1->val + countup) % 10;
                countup = (l1->val + countup)/10 % 10;
            } else {
                out_copy->val = countup;
                countup = 0;
            }

            if (l1 != NULL) l1 = l1->next;
            if (l2 != NULL) l2 = l2->next;
            if((l1 != NULL || l2 != NULL) || countup == 1) {
                ListNode* next = new ListNode(NULL);
                out_copy->next = next;
                out_copy = out_copy->next;
            }   
        }
        return out;
    }
};
