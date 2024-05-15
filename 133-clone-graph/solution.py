"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashmap = {}
        if node == None: return None
        queue = [node]
        seen = [0 for i in range(101)]
        seen[node.val] = 1
        while len(queue):
            cur_node = queue.pop()
            if cur_node.val not in hashmap:
                hashmap[cur_node.val] = Node(cur_node.val)
            for n in cur_node.neighbors:
                if n.val not in hashmap:
                    hashmap[n.val] = Node(n.val)
                hashmap[cur_node.val].neighbors.append(hashmap[n.val])
                if seen[n.val] == 0:
                    queue.append(n)
                    seen[n.val] = 1

        return hashmap[node.val]
