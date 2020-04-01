class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,len(board),3):
            for j in range(0,len(board[0]),3):
                digits = set()
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if board[k][l] in digits:
                            return False
                        if board[k][l] != '.':
                            digits.add(board[k][l])
        
        for row in range(len(board)):
            digits = set()
            for col in range(len(board[0])):
                if board[row][col] in digits:
                    return False
                if board[row][col] != '.':
                    digits.add(board[row][col])
        for col in range(len(board[0])):
            digits = set()
            for row in range(len(board)):
                if board[row][col] in digits:
                    return False
                if board[row][col] != '.':
                    digits.add(board[row][col])
        
        return True
