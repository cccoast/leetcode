class Solution(object):
    def dfs(self,i,j,s):
        if self.flag is True: return 
        if 0 <= i < self.m and 0 <= j < self.n:
            if self.dp[i][j] is False: 
                return 
            if self.board[i][j] == s[0]:
                if len(s) == 1:
                    self.flag = True
                    return
                self.dp[i][j] = False
                self.dfs(i+1,j,s[1:])
                self.dfs(i,j+1,s[1:])
                self.dfs(i-1,j,s[1:])
                self.dfs(i,j-1,s[1:])
                self.dp[i][j] = True

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """ 
        self.flag = False
        if len(board) == 0 or len(word) == 0: return False
        self.cache = {}
        self.board = board
        self.m,self.n = len(board),len(board[0])
        self.dp = [ [True for i in range(self.n) ] for j in range(self.m) ]
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] in self.cache:
                    self.cache[board[i][j]].append((i,j))
                else:
                    self.cache[board[i][j]] = [(i,j),]
        if word[0] in self.cache.keys():
            if len(word) <= 1: return True
            for (i,j) in self.cache[word[0]]:
                if self.flag is True:
                    return True
                self.dp[i][j] = False
                self.dfs(i+1,j,word[1:])
                self.dfs(i,j+1,word[1:])
                self.dfs(i-1,j,word[1:])
                self.dfs(i,j-1,word[1:])
                self.dp[i][j] = True
        return self.flag
        
if __name__ == '__main__':
    board = \
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
    word = "ABCB"
    solver = Solution()
    print solver.exist(board,word)
    