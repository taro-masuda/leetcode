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
    bool hasCycle(ListNode *head) {
        if (head == NULL) return false;
        std::vector<ListNode*> v;
        while (true) {
            v.push_back(head);
            head = head->next;
            if (head == NULL){
                return false;
            }
            auto p = std::find(v.begin(), v.end(), head);
            if (p != v.end()){
                return true;
            }
        }
    }
};
