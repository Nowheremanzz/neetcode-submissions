class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False
        row_count, col_count, block_count = [0]*9, [0]*9, [0]*9
        for row in board:
            for col in row:
                if not col.isdigit() and col != ".":
                    return False
                if col.isdigit():
                    col_count[int(col)-1] += 1
            for num in col_count:
                if num > 1:
                    return False
            col_count = [0] * 9
        for i in range(9):
            for row in board:
                if row[i].isdigit():
                    row_count[int(row[i])-1] += 1
            for num in row_count:
                if num > 1:
                    return False
            row_count = [0] * 9
        for i in range(0,9,3):
            for j in range(0,9,3):
                for x in range(i, i+3):
                    for y in range(j, j+3):
                        if board[x][y].isdigit():
                            block_count[int(board[x][y])-1] += 1
                for num in block_count:
                    if num > 1:
                        return False
                block_count = [0] * 9
        return True
                
