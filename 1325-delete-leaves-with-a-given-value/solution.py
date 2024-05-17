# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return root

        left = self.removeLeafNodes(root.left, target)
        right = self.removeLeafNodes(root.right, target)
        if root.val == target and left == None and right == None:
            return None
                
        root.left = left
        root.right = right

        return root
        