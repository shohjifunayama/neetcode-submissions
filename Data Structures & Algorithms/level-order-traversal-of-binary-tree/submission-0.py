# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        que = deque([root]) if root else None
        res = []

        while que:
            level = []
            for _ in range(len(que)):
                node = que.popleft()
                if node.left: que.append(node.left) 
                if node.right: que.append(node.right)
                level.append(node.val)

            res.append(level)
        
        return res


