# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = [True]
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            l = height(root.left)
            r = height(root.right)
            if abs(l - r) > 1: 
                res[0] = False
            return max(l, r) + 1
        height(root)
        return res[0]