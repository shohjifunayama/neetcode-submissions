# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p) or (not q):
            if (not p) and (not q):
                return True
            else: return False

        if p.val != q.val:
            return False
        if (p.left == None) ^ (q.left == None) or (p.right ==None) ^ (q.right == None):
            return False

        is_sameL = self.isSameTree(p.left, q.left) if p.left else True
        is_sameR = self.isSameTree(p.right, q.right) if p.right else True

        return is_sameL and is_sameR