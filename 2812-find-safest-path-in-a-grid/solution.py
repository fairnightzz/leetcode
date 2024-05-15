import heapq
from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        # feels like dijkstra
        n = len(grid)
        thieves = deque()
        direction = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        for x in range(n):
            for y in range(n):
                if grid[x][y] == 1:
                    thieves.append([x, y])
                    grid[x][y] = 0
                else:
                    grid[x][y] = -1

        while len(thieves):
            x, y = thieves.popleft()
            for d in direction:
                newX = x+d[0]
                newY = y+d[1]

                if 0<= newX < n and 0<= newY < n and grid[newX][newY] == -1:
                    grid[newX][newY] = grid[x][y] + 1
                    thieves.append([newX, newY])

        bestAns = float("-inf")
        queue = [[-grid[0][0], 0, 0]]

        seen = set()
        seen.add((0, 0))

        # direction = [[1, 0], [0, 1]]
        while len(queue):
            safeness, x, y = heapq.heappop(queue)
            if x == n-1 and y == n-1:
                bestAns = max(bestAns, -safeness)
            for d in direction:
                newX = d[0] + x
                newY = d[1] + y
                if 0<= newX < n and 0<= newY < n and (newX, newY) not in seen:
                    seen.add((newX, newY))
                    newSafeness = grid[newX][newY]
                    heapq.heappush(queue, [-min(newSafeness, -safeness), newX, newY])
        return bestAns







