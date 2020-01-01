class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        if (board.size() == 0) return;
        
        vector<vector<int>> v(board.size(), vector<int>(board[0].size(), -1));
        
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                int num_alive = 0;
                if (row != 0) {
                    num_alive += board[row - 1][col];
                    if (col != 0) num_alive += board[row - 1][col - 1];
                    if (col != board[0].size() - 1) num_alive += board[row - 1][col + 1];
                }
                if (col != 0) {
                    num_alive += board[row][col - 1];
                    if (row != board.size() - 1) num_alive += board[row + 1][col - 1];
                }
                if (col != board[0].size() - 1) {
                    num_alive += board[row][col + 1];
                    if (row != board.size() - 1) num_alive += board[row + 1][col + 1];
                }
                if (row != board.size() - 1) num_alive += board[row + 1][col];
                
                v[row][col] = num_alive;
            }
        }
        
        for (int row = 0; row < board.size(); row++) {
            for (int col = 0; col < board[0].size(); col++) {
                if (v[row][col] == 3 && board[row][col] == 0) board[row][col] = 1;
                else if ((v[row][col] == 2 || v[row][col] == 3) && board[row][col] == 1) ;
                else if ((v[row][col]  > 3 || v[row][col] <  2) && board[row][col] == 1) board[row][col] = 0;
            }
        }
        
        return;
    }
};
