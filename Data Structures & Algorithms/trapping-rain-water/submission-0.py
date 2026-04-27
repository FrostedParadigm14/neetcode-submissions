class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        l = 0
        r = len(height)-1
        maxL = height[l]
        maxR = height[r]
        water = 0

        while l < r:
            if maxL < maxR:
                l+=1
                if maxL - height[l] > 0: 
                    water += (maxL - height[l])
                maxL = max(maxL, height[l])
            else:
                r-=1
                if maxR - height[r] > 0:
                    water += (maxR - height[r])
                maxR = max(maxR, height[r]) 

        return water

'''
find min of heights l and right...then - current, if less than 0 -> 0
update the m
'''