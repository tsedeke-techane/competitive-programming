# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0

        while queue:
            cur_node = []
          
            for _ in range(len(queue)):
                node = queue.popleft()
              
                if level % 2 == 1:
                    cur_node.append(node)
              
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
          
            if cur_node:
                left, right = 0, len(cur_node) - 1
                while left < right:
                    cur_node[left].val, cur_node[right].val = cur_node[right].val, cur_node[left].val
                    left += 1
                    right -= 1
          
            level += 1
      
        return root
