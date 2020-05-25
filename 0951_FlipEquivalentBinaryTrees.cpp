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
    bool checkTwoNodes(TreeNode* node1, TreeNode* node2) {
        if (node1->val != node2->val) return false;
        else if (!flippedEquiv(node1, node2) && !sameEquiv(node1, node2)) return false;
        return true;
    }
    
    bool sameEquiv(TreeNode* root1, TreeNode* root2) {
        //cout << "same: " <<  root1->val << ", " << root2->val << endl;
        if (root1->right != NULL)
            if (root2->right != NULL) {
                if (!checkTwoNodes(root1->right, root2->right)) return false;
            } else return false;
        if (root1->left != NULL) {
            if (root2->left != NULL) {
                if (!checkTwoNodes(root1->left, root2->left)) return false;
            } else return false;
        }
        if (root2->left != NULL) {
            if (root1->left == NULL) return false;
        }
        if (root2->right != NULL) {
            if (root1->right == NULL) return false;
        }
        return true;
    }
    
    bool flippedEquiv(TreeNode* root1, TreeNode* root2) {
        //cout << "flipped: " <<  root1->val << ", " << root2->val << endl;
        if (root1->right != NULL)
            if (root2->left != NULL) {
                if (!checkTwoNodes(root1->right, root2->left)) return false;
            } else return false;
        if (root1->left != NULL) {
            if (root2->right != NULL) {
                if (!checkTwoNodes(root1->left, root2->right)) return false;
            } else return false;
        }
        if (root2->left != NULL) {
            if (root1->right == NULL) return false;
        }
        if (root2->right != NULL) {
            if (root1->left == NULL) return false;
        }
        return true;
    }
    
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if (root1 == NULL) {
            if (root2 == NULL) return true;
            else return false;
        } else if (root2 == NULL) return false;
        //cout << "flip: " << root1->val << ", " << root2->val << endl;
        return flippedEquiv(root1, root2) || sameEquiv(root1, root2);
    }
};
