# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        level = 0
        queue = deque([root])
        while queue:
            #remove the current values in quue, add children
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level+=1
        
        return level

'''
R dfs
    if no node =>0
    if 1 node -> 1
    1 + max(l, r)

I DFS

BFS
- usually has a queue
- add root, remove and at childs
  - remove left, none toreplat
  - remove right, add 15, 7- level 3
  - remove 15 left, non, remove 7, non - none in queue left

'''