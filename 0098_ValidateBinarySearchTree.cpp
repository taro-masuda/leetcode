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
    bool isValidBSTFirst(TreeNode* root){
        if(root == NULL) return true;
        //TreeNode* root_copy = root;
        if (root->left != NULL) {
            if (root->right != NULL){
                if (root->left->val >= root->val || root->val >= root->right->val) return false;
            } else if (root->left->val >= root->val) return false;
            if (!isValidBSTSub(root->left)) return false;
        } else if (root->right != NULL) return (root->right->val > root->val);
        if (root->right != NULL) {
            if (root->left != NULL){
                if (root->left->val >= root->val || root->val >= root->right->val) return false;
            } else if (root->val >= root->right->val) return false;
            if(!isValidBSTSub(root->right)) return false;
        } else if (root->left != NULL) return (root->left->val < root->val);
        return true;
    }
    
    bool isValidBSTSub(TreeNode* root) {
        if(root == NULL) return true;
        //TreeNode* root_copy = root;
        if (root->left != NULL) {
            if (root->right != NULL){
                if (root->left->val >= root->val || root->val >= root->right->val) return false;
            } else if (root->left->val >= root->val) return false;
            if (!isValidBST(root->left)) return false;
        } else if (root->right != NULL) return (root->right->val > root->val);
        if (root->right != NULL) {
            if (root->left != NULL){
                if (root->left->val >= root->val || root->val >= root->right->val) return false;
            } else if (root->val >= root->right->val) return false;
            if(!isValidBST(root->right)) return false;
        } else if (root->left != NULL) return (root->left->val < root->val);
        return false;
    }
    
    bool isValidBST(TreeNode* root) {
        return isValidBSTFirst(root);
    }
};
