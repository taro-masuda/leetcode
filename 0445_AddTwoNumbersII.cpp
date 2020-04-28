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
        if (l1 == NULL && l2 == NULL) return l1;
        stack<int> s1, s2;
        int N1 = 0, N2 = 0;
        ListNode* l = l1;
        while (l != NULL) {
            s1.push(l->val);
            N1++;
            l = l->next;
        }
        l = l2;
        while (l != NULL) {
            s2.push(l->val);
            N2++;
            l = l->next;
        }
        stack<int> s_ans;
        int countup = 0;
        ListNode* ans = new ListNode(0);
        while (!s1.empty() || !s2.empty()) {
            int sum;
            if (s1.empty()) {
                sum = s2.top() + countup;
                countup = sum/10;
                s_ans.push(sum%10);
                s2.pop();
            } else if (s2.empty()) {
                sum = s1.top() + countup;
                countup = sum/10;
                s_ans.push(sum%10);
                s1.pop();
            } else {
                sum = s1.top() + s2.top() + countup;
                countup = sum/10;
                s_ans.push(sum%10);
                s1.pop(); s2.pop();
            }
            ans->val = sum%10;
            if (s1.empty() && s2.empty()) {
                if (countup > 0) {
                    ListNode* l_new = new ListNode(0);
                    l_new->next = ans;
                    l_new->val = 1;
                    ans = l_new;
                }
            } else {
                ListNode* l_new = new ListNode(0);
                l_new->next = ans;
                ans = l_new;
            }
        }
        return ans;
    }
};
