class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        subbox = collections.defaultdict(set) # key = ( r/3, c/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r] or 
                    board[r][c] in col[c] or
                    board[r][c] in subbox[(r // 3, c // 3)]):
                    return False
                col[c].add(board[r][c])
                row[r].add(board[r][c])
                subbox[(r // 3, c // 3)].add(board[r][c])
        return True