class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hmap.keys(): 
                return [hmap[diff], i]
            hmap[nums[i]] = i
        return []

'''
create a map, flip - we store the value => index

loop though the nums array
    find the difference val between targer and curr value
    check if the difference val is already in map (already processed)
        return the current index ++ mapped index value of difference val
    regardless, add to map - add the value and the index it is in
'''

        