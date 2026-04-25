# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        aque = deque([p])
        bque = deque([q])

        while aque and bque:
            for i in range(len(aque)):
                a = aque.popleft()
                b = bque.popleft()

                if a is None and b is None:
                    continue
                if a is None or b is None or a.val != b.val:
                    return False

                aque.append(a.left)
                aque.append(a.right)
                bque.append(b.left)
                bque.append(b.right)

        return True

'''
DFS
o(n), o(n)

if both node null, match
if both node exist and same - match
    check the leave nodes as well, recursivley call
other cases - not match

BFS
2 queus 1 for each tree, 
add the root for both trees
check with curr leng in queue, bfs
    if both null, no problem , continue
    if one is null or the other or they dont match, return false 
    otherwise add the children 
do until queue empty
return true if nothing blcoked
'''

        