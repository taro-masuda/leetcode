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
    void reorderList(ListNode* head) {
        ListNode* cur = head;
        stack<int> s;
        queue<int> q;
        int size = 0;
        while (cur != NULL) {
            s.push(cur->val);
            q.push(cur->val);
            cur = cur->next;
            size++;
        }
        cur = head;
        while (cur != NULL) {
            cur->val = q.front(); q.pop();
            cur = cur->next;
            if (cur == NULL) break;
            cur->val = s.top(); s.pop();
            cur = cur->next;
        }
    }
};
