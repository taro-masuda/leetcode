/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/
class Solution {
public:
    void connectLeft(Node* root) {
        if (root->left != NULL && root->right != NULL) {
            root->left->next = root->right;
        }
        if (root->left != NULL) connectLeft(root->left);
        if (root->right != NULL) connectLeft(root->right);
    }
    void connectRight(Node* root) {
        if (root->right != NULL && root->next != NULL) {
            root->right->next = root->next->left;
        }
        if (root->left != NULL) connectRight(root->left);
        if (root->right != NULL) connectRight(root->right);
    }
    
    Node* connect(Node* root) {
        if (root == NULL) return NULL;
        connectLeft(root);
        connectRight(root);
        return root;
    }
};
