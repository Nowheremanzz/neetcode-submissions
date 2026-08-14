# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_d = [0]
        def height(root: TreeNode) -> int:
            if not root:
                return 0
            h_l = height(root.left)
            h_r = height(root.right)
            max_d[0] = max((h_l + h_r), max_d[0])
            return max(h_l, h_r) + 1
        height(root)
        return max_d[0]