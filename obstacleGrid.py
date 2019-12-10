class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m,n = len(obstacleGrid),len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        if n == 1 and m == 1:
            if obstacleGrid[0][0] == 0:
                return 1
            else:
                return 0
        if n >= 1:
            for i in range(m)[::-1]:
                if obstacleGrid[i][n-1] != 1:
                    dp[i][n-1] = 1
                else:
                    break
        if m >= 1:
            for i in range(n)[::-1]:
                if obstacleGrid[m-1][i] != 1:
                    dp[m-1][i] = 1
                else:
                    break
        if n >= 1 or m >= 1:
            for i in range(m-1)[::-1]:
                for j in range(n-1)[::-1]:
                    print i,j
                    if obstacleGrid[i][j] != 1:
                        dp[i][j] = dp[i][j+1] + dp[i+1][j]
        return dp[0][0]        
        
if __name__ == '__main__':
    a = [
          [0,0,],
          [1,1,],
          [0,0,]
        ]
    solver = Solution()
    print solver.uniquePathsWithObstacles(a)