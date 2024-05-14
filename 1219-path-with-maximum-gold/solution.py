class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        paths = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        m = len(grid)
        n = len(grid[0])
        def dfs(x, y, seen):
            currentGold = grid[y][x]
            maxGold = 0
            seen[y][x] = 1
            for p in paths:
                newX = x+p[0]
                newY = y+p[1]
                if 0 <= newX < n and 0<= newY < m and grid[newY][newX] > 0 and seen[newY][newX] == 0:
                    maxGold = max(maxGold, dfs(newX, newY, seen))
            seen[y][x] = 0
            return currentGold + maxGold
        seen = [[0 for i in range(len(grid[0]))] for a in range(len(grid))]
        ans = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 0:
                    ans = max(dfs(x, y, seen), ans)
        return ans
        