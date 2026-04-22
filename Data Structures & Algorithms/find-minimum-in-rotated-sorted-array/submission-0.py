class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        return nums[left]
        
'''
sorted but rotated, so there is 2 parts sorted
find mid pos = left + right //2

check if mid is higher than the right most side
    means min value in right hand side
    so left/lower = mid + 1
otherwise (mid is not higher than right)
    means min value in left hand side 
    so right/upper = mid 


'''