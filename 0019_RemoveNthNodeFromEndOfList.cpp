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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* head_copy = head;
        int m = 0;
        while (head != NULL){
            head = head->next;
            m++;
        }
        
        if (m == 1) {
            return NULL;
        }
        
        head = head_copy;
        if (m == n){
            head = head->next;
            return head;
        }
        for (int i = 0; i < m; i++){
            if (i == m-n-1) head->next = head->next->next;
            else head = head->next;
        }
        return head_copy;
    }
};
