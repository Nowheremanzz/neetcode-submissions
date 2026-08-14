# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSametree(self, a: TreeNode, b: TreeNode) -> bool:
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.isSametree(a.left, b.left) and self.isSametree(a.right, b.right)
        return False 

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return self.isSametree(root, subRoot)
        return self.isSametree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)