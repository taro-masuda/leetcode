class Solution {
public:
    struct Node {
        char character;
        vector<Node*> adj; /*pointer to adjacent nodes*/
        bool visited;
    };
    struct Graph {
        vector<Node*> nodes;
    };
    Graph g;
    
    void init(vector<vector<char>>& board, string word) {
        g.nodes = {};
        int nrow = board.size(), ncol = board[0].size();
        for (int r = 0; r < nrow; r++) {
            for (int c = 0; c < ncol; c++) {
                Node* n = new Node;
                n->character = board[r][c];
                n->visited = false;
                n->adj = {};
                g.nodes.push_back(n);        
            }
        }
        int nodeidx = 0;
        for (int r = 0; r < board.size(); r++) {
            for (int c = 0; c < board[0].size(); c++) {
                if (r > 0) g.nodes[nodeidx]->adj.push_back(g.nodes[nodeidx-ncol]);
                if (c > 0) g.nodes[nodeidx]->adj.push_back(g.nodes[nodeidx-1]);
                if (r < nrow-1) g.nodes[nodeidx]->adj.push_back(g.nodes[nodeidx+ncol]);
                if (c < ncol-1) g.nodes[nodeidx]->adj.push_back(g.nodes[nodeidx+1]);
                nodeidx++;
            }
        }
    }
    bool search(Node* root, string word, int idxWord) {
        if (root == NULL) return false;
        if (root->visited) return false;
        if (root->character == word[idxWord]) {
            if (idxWord+1 == word.size()) {
                root->visited = true;
                return true;
            }
            for (int i = 0; i < root->adj.size(); i++) {
                if (!root->adj[i]->visited) {
                    root->visited = true;
                    if (search(root->adj[i], word, idxWord+1)) {
                        return true;
                    } else root->visited = false;
                }
            }
        }
        return false;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        if (board.size() == 0) return false;
        if (word.size() == 0) return true;
        
        init(board, word);

        for (int i = 0; i < g.nodes.size(); i++) {
            if (search(g.nodes[i], word, 0)) return true;
            init(board, word);
        };
        return false;
    }
};
