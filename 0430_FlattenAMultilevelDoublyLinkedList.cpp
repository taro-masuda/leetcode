#include<stack>
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/
class Solution {
public:
    Node* flatten(Node* head) {
        if (head == NULL) return head;
        Node* current_node = head;
        stack<Node*> next_pointers;
        while (current_node != NULL) {
            if (current_node->child != NULL) {
                next_pointers.push(current_node->next);
                current_node->child->prev = current_node;
                current_node->next = current_node->child;
                current_node->child = NULL;
                continue;
            } else if (current_node->next == NULL) {
                if (!next_pointers.empty()) {
                    current_node->next = next_pointers.top();
                    next_pointers.pop();
                    if (current_node->next != NULL) current_node->next->prev = current_node;
                }
                current_node = current_node->next;
            } else current_node = current_node->next;
        }
        return head;
    }
};
