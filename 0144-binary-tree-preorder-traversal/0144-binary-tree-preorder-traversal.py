# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
        def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            ans = []
            if not root:
                return []
            ans.append(root.val)
            left = self.preorderTraversal(root.left)
            right = self.preorderTraversal(root.right)

            ans.extend(left)
            ans.extend(right)
            return ans