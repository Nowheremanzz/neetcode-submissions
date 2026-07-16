class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False
        row_check, col_check, block_check = [], [], []
        for i in range(9):
            row_check.append(set())
            col_check.append(set())
            block_check.append(set())
        for i in range(9):
            for j in range(9):
                if not board[i][j].isdigit() and board[i][j] != ".":
                    return False
                if board[i][j].isdigit():
                    n = int(board[i][j])
                    if n > 9 or n < 1:
                        return False
                    block = i//3 * 3 + j//3 
                    if n in row_check[i] or n in col_check[j] or n in block_check[block]:
                        return False
                    else:
                        row_check[i].add(n)
                        col_check[j].add(n)
                        block_check[block].add(n)
        return True
                
