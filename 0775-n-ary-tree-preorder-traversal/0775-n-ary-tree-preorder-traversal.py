"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def do(Node):
            if not Node: return
            ans.append(Node.val)

            for child in Node.children:
                do(child)

        do(root)
        return ans