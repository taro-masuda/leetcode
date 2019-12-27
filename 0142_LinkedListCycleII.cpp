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
    ListNode *detectCycle(ListNode *head) {
        unordered_map<ListNode*,int> mp;
        ListNode* head_copy = head;
        int idx = 0;
        if (head_copy == NULL) return NULL;
        while (true){
            if (head_copy->next == NULL) return NULL;
            auto i = mp.find(head_copy);
            if(i == mp.end()){
                mp[head_copy] = idx;
            } else {
                break;
            }
            head_copy = head_copy->next;
            idx++;
        }
        return head_copy;
    }
};
