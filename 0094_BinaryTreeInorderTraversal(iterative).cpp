/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */


class Solution {
public:
    vector<int> DFS(TreeNode* root) {
        vector<int> out;
        if (root == NULL) return out;
        set<TreeNode*> visited;
        stack<TreeNode*> s;
        s.push(root);
        while (!s.empty()) {
            TreeNode* cur = s.top();
            if (cur->left != NULL && visited.find(cur->left) == visited.end()) {s.push(cur->left); continue;}
            else {out.push_back(cur->val); visited.insert(cur); s.pop();}
            if (cur->right != NULL) s.push(cur->right);
        }
        return out;
    }
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> out = DFS(root);
        return out;
    }
};
