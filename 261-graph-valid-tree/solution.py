class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # just check if there is a cycle
        graph = [[] for a in range(n)]

        for edge in edges:
            a, b = edge
            graph[a].append(b)
            graph[b].append(a)
        
        queue = [[0, 0]]

        visited = [False for i in range(n)]
        visited[0] = True

        while queue:
            prev, current = queue.pop()
            for new_node in graph[current]:
                if new_node == prev:
                    continue
                if visited[new_node]:
                    return False
                visited[new_node] = True
                queue.append([current, new_node])
                
        # also check if there are components we haven't checked
        if False in visited:
            return False
        return True




