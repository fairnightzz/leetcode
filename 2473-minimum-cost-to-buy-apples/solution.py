import heapq
class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        graph = [[] for x in range(n)]

        for r in roads:
            a, b, cost = r
            graph[a-1].append([b-1, cost])
            graph[b-1].append([a-1, cost])
        
        print(graph)
        
        ans = []
        for city in range(n):
            # dfs to get shortest path
            bestCost = appleCost[city]
            seen = [False for i in range(n)]
            seen[city] = True
            queue = [[0, city]]
            while len(queue) > 0:
                pathcost, city = heapq.heappop(queue)
                seen[city] = True
                for path in graph[city]:
                    nextCity, cityCost = path
                    if seen[nextCity]:
                        continue
                    actualCost = appleCost[nextCity] + (cityCost + pathcost) * (k+1)
                    bestCost = min(actualCost, bestCost)
                    heapq.heappush(queue, [cityCost + pathcost, nextCity])

            ans.append(bestCost)
        return ans



        