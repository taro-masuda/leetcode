#define rep(i, n) for (int i = 0; i < (n); ++i)

class Solution {
public:
    bool findAdjecent(vector<vector<char>>& board, string word, int r, int c){
        if (word=="") return true;
        int R = board.size();
        int C = board[0].size();
        string nextWord;
        if (word.size() > 1) nextWord = word.substr(1, word.size()-1);
        else nextWord = "";
        if (r > 0) {
            if (board[r-1][c] == word[0]) {
                board[r-1][c] = '\0';
                if (findAdjecent(board, nextWord, r-1, c)) return true;
                else board[r-1][c] = word[0];
            }
        }
        if (r < R-1) {
            if (board[r+1][c] == word[0]) {
                board[r+1][c] = '\0';
                if (findAdjecent(board, nextWord, r+1, c)) return true;
                else board[r+1][c] = word[0];
            }
        }
        if (c > 0) {
            if (board[r][c-1] == word[0]) {
                board[r][c-1] = '\0';
                if (findAdjecent(board, nextWord, r, c-1)) return true;
                else board[r][c-1] = word[0];
            }
        }
        if (c < C-1) {
            if (board[r][c+1] == word[0]) {
                board[r][c+1] = '\0';
                if (findAdjecent(board, nextWord, r, c+1)) return true;
                else board[r][c+1] = word[0];
            }
        }
        return false;
    }
    
    bool exist(vector<vector<char>>& board, string word) {
        int R = board.size();
        if (R == 0) return false;
        int C = board[0].size();
        if (C == 0) return false;
        
        rep(r, R) {
            rep(c, C) {
                if (board[r][c] == word[0]) {
                    board[r][c] = '\0';
                    string nextWord = word.substr(1, word.size()-1);
                    if (findAdjecent(board, nextWord, r, c)) return true;
                    else board[r][c] = word[0];
                }
            }
        }
        return false;
    }
};
