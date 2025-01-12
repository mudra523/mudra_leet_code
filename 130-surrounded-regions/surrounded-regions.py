class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        
        def edge(r, c):
            if ( r < 0 or c < 0 or r == ROWS or c == COLS or board[r][c] != "O"):
                return 
            board[r][c] = "T"
            edge(r + 1, c)
            edge(r - 1, c)
            edge(r, c + 1)
            edge(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if ((r in [0, ROWS - 1] or c in [0, COLS - 1]) and board[r][c] == "O"):
                    edge(r, c)
                
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"
        