# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # in every recursion, figure out the number of coins that are extra
        # you have
        # number of moves is equal to the number of extra coins that they return
        # can be negative

        global moves
        moves = 0

        def dfs(root) -> [int, int]:
            global moves
            if root == None:
                return 0
            
            lCoins = dfs(root.left)
            rCoins = dfs(root.right)

            coins = root.val - 1 + lCoins + rCoins
            moves += abs(lCoins) + abs(rCoins)

            return coins

        dfs(root)

        return moves
        