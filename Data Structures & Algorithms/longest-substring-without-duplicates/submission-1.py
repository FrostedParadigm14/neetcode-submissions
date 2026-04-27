class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # subSet = set()
        # left = 0
        # ans = 0

        # for right in range(len(s)):
        #     while s[right] in subSet:
        #         subSet.remove(s[left])
        #         left+=1
        #     subSet.add(s[right])
        #     ans = max(ans, right-left+1)

        # return ans
        map = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            if s[right] in map:
                left = max(left, map[s[right]]+1)
            map[s[right]] = right
            ans = max(ans, right-left+1)
        return ans
        

'''
start with first and keep going till u hit duplicate (check set)
when it hit duplicate, remove from begining/leftmost until duplicate removed
remove from set and also from susbstring...
track the longest value

sliding window - o(n)
set o(n)

----
more optimal
find where right is mapped and take left as that 
use hashmap
'''