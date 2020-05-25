struct Player {
    vector<int> rows;
    vector<int> cols;
    int diag;
    int diag_cr;
};

class TicTacToe {
public:
    struct Player p1;
    struct Player p2;
    int N;
    /** Initialize your data structure here. */
    void Initialize(struct Player& p) {
        p.rows.push_back(0);
        p.cols.push_back(0);
    }
    TicTacToe(int n) {
        for (int i = 0; i < n; i++) {
            Initialize(p1);
            Initialize(p2);        
        }
        p1.diag = 0;
        p2.diag = 0;
        p1.diag_cr = 0;
        p2.diag_cr = 0;
        N = n;
    }
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int playerStateChange(int row, int col, int player, struct Player& p) {
        int result = ++p.rows[row];
        if (result == N) return player;
        result = ++p.cols[col];
        if (result == N) return player;
        if (row == col) result = ++p.diag;
        if (result == N) return player;
        if (row + col == N-1) result = ++p.diag_cr;
        if (result == N) return player;
        return 0;
    }
    
    int move(int row, int col, int player) {
        int retVal;
        if (player == 1) {
            retVal = playerStateChange(row, col, player, p1);
        } else {
            retVal = playerStateChange(row, col, player, p2);
        }
        return retVal;
    }
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe* obj = new TicTacToe(n);
 * int param_1 = obj->move(row,col,player);
 */
