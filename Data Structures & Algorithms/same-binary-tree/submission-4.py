# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 = [p]
        stack2 = [q]
        while stack1 and stack2:
            l = stack1.pop()
            r = stack2.pop()
            if l == r == None:
                continue
            if l and r and l.val == r.val:
                stack1.append(l.left)
                stack1.append(l.right)
                stack2.append(r.left)
                stack2.append(r.right)
            else:
                return False
        return True
            
