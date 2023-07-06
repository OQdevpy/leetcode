url ="https://leetcode.com/problems/word-search/"

class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        return False
    
    def helper(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = "#"
        res = self.helper(board, i+1, j, word[1:]) or self.helper(board, i-1, j, word[1:]) or self.helper(board, i, j+1, word[1:]) or self.helper(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res