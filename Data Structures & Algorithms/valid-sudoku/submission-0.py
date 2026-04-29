class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # from 0 to 9
        for i in range(n):
            # WANT a reset in each check section
            row_s, col_s, grid_s = set(), set(), set()
            for j in range(n):
                r = board[i][j]
                c = board[j][i]
                # g = board[i//3][j//3]
                row = 3 * (i // 3) + j // 3
                col = 3 * (i % 3) + j % 3
                g = board[row][col]
                #check across row

                if r in row_s or c in col_s or g in grid_s:
                    return False
                if r != ".": 
                    row_s.add(r) 
                #check across column
                if c != ".":
                    col_s.add(c) 
                #check across grid
                if g != ".":
                    grid_s.add(g) 
        return True