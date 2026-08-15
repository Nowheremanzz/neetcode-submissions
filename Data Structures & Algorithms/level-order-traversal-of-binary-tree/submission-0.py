# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        level = 1
        res = []
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if len(res) == level:
                    res[level - 1].append(node.val)
                else:
                    res.append([node.val])
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return res
