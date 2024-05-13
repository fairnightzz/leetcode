class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0 for i in range(n-2)] for a in range(n-2)]
        for y in range(n-2):
            for x in range(n-2):
                largest = float("-inf")
                for i in range(3):
                    rowLargest = max(grid[y+i][x:x+3])
                    largest = max(largest, rowLargest)

                ans[y][x] = largest
        return ans

        