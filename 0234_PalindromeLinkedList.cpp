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
    bool isPalindrome(ListNode* head) {
        vector<int> v;
        while (head != NULL){
            v.push_back(head->val);
            head = head->next;
        }
        int i = 0;
        int N = v.size();
        bool isPalindrome = true;
        while (i < N / 2){
            if (v[i] != v[N-i-1]) isPalindrome = false;
            i++;
        }
        return isPalindrome;
    }
};
