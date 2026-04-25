class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        ans = 0

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            ans = max(ans, area)

            if heights[left] < heights[right]:
                left+=1
            else:
                right-=1
        
        return ans



'''
min of considrerd side will be the side to cpmare size of l and r
    which is lesser of two increment thar
find the max of size

calculate thr size, store the higest

'''
        