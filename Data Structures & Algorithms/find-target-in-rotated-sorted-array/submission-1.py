class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid

            if nums[start] <= nums[mid]: #normal
                if target > nums[mid] or target < nums[start]:
                    # target > mid but increasing order still okay
                    # OR target is even lesser than start, so its in second half
                    start = mid + 1
                else:
                    end = mid - 1
            else: #not normal, mid > end
                if target < nums[mid] or target > nums[end]:
                    # target < mid even though the order mess up
                    # OR target is greater than end, so its in first half
                    end = mid - 1
                else:
                    start = mid + 1


        return -1


'''
set the start and end pointers

while start < end
    set mid value = (start + end ) //2
    if mid == value -> return!

    // 4 cases
    if start <= mid (usually normal but check)
        if target > mid OR target < start
        //means target above mid, or target smaller than start so its on other end even if first 1/2 increasing
        //move the start up 
            start = mid + 1
        else:
        //anything else, move the end down 
            end = mid - 1
        
    else: //mid > end (weird, its rotated so starting is in second half)
        if target < mid OR target > end
        //means target is less than mid even though mid is greater than end
        //OR target is greater than end, meaning bigger part is rotated to first part
        //move the end down
            end = mid - 1
        else
        //anything else, move the end down 
            start = mid + 1

    return -1 if not mid/not found
'''
        