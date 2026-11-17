# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def find(root: Optional[TreeNode], res: list) -> int:
            L = find(root.left, res) + 1 if root.left else 0
            R = find(root.right, res) + 1 if root.right else 0
            res.append(L+R)
            return max(L, R) if root.left or root.right else 0

        res = []
        a = find(root, res)
        res.append(a)
        return max(res)

