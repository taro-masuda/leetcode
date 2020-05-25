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
    bool isSameTree(TreeNode* s, TreeNode* t) {
        if (s == NULL) {
            if (t == NULL) return true;
            else return false;
        } else if (t == NULL) return false;

        bool result = true;
        if (s->left != NULL || t->left != NULL) {
            result = result && isSameTree(s->left, t->left);
        }
        if (s->right != NULL || t->right != NULL) {
            result = result && isSameTree(s->right, t->right);
        }
        result = result && s->val == t->val;
        return result;
    }
    bool isSubtree(TreeNode* s, TreeNode* t) {
        if (isSameTree(s,t)) return true;
        if (s->right != NULL) {
            if (isSubtree(s->right, t)) return true;
        }
        if (s->left != NULL) {
            if (isSubtree(s->left, t)) return true;
        }
        return false;
    }
};
