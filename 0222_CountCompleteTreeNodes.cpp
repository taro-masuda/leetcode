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
    int countNodes(TreeNode* root) {
        int count = 0;
        if (root == NULL) return count;
        else count++;
        if (root->left != NULL) count += countNodes(root->left);
        if (root->right != NULL) count += countNodes(root->right);
        return count;
    }
};
