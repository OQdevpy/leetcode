import itertools

class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        for i, j in itertools.product(range(9), range(9)):
            num = board[i][j]
            if num == '.':
                continue
            rows[i].add(num)
            cols[j].add(num)
            boxes[(i//3)*3+j//3].add(num)
        self.helper(board, rows, cols, boxes)
    
    def helper(self, board, rows, cols, boxes):
        for i, j in itertools.product(range(9), range(9)):
            if board[i][j] == '.':
                for num in '123456789':
                    if num not in rows[i] and num not in cols[j] and num not in boxes[(i//3)*3+j//3]:
                        board[i][j] = num
                        rows[i].add(num)
                        cols[j].add(num)
                        boxes[(i//3)*3+j//3].add(num)
                        if self.helper(board, rows, cols, boxes):
                            return True
                        board[i][j] = '.'
                        rows[i].remove(num)
                        cols[j].remove(num)
                        boxes[(i//3)*3+j//3].remove(num)
                return False
        return True