# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        L = self.maxDepth(root.left) + 1 if root.left else 1
        R = self.maxDepth(root.right) + 1 if root.right else 1
        
        return max(L, R)