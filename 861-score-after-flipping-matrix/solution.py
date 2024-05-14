class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def invert_row(row):
            for i in range(n):
                grid[row][i] = 1-grid[row][i]
        def invert_col(col):
            for i in range(m):
                grid[i][col] = 1-grid[i][col]
        for row in range(m):
            if grid[row][0] == 0:
                invert_row(row)
        for col in range(1, n):
            count = 0
            for row in range(m):
                if grid[row][col] == 1:
                    count +=1
                if count > m/2:
                    break
            if count < m/2:
                invert_col(col)
        ans = 0
        for row in range(m):
            num = 0
            for col in range(n):
                num += grid[row][col]*(2**(n-col-1))
            ans+=num
        return ans