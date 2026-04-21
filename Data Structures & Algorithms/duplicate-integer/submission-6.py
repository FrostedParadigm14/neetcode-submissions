class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

'''
set only stores unique values, 
so duplicates are automatically removed.
compare the length of the set to the length of the original array
'''