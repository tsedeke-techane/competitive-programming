# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, mn, mx):
            if node is None:
                return
                
            nonlocal ans
            curDiff = max(abs(mn - node.val), abs(mx - node.val))
            ans = max(ans, curDiff)

            new_min = min(mn, node.val)
            new_max = max(mx, node.val)
            dfs(node.left, new_min, new_max)
            dfs(node.right, new_min, new_max)

        ans = 0
        dfs(root, root.val, root.val)
        return ans

             