class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for i in range(9)]
        rows = [set() for i in range(9)]
        squares = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    square = (r//3 * 3) + c//3
                    val = board[r][c]

                    if (val in rows[r]
                        or val in cols[c]
                        or val  in squares[square]):
                            return False

                    cols[c].add(board[r][c])
                    rows[r].add(board[r][c])
                    squares[square].add(board[r][c])
                
        return True

        