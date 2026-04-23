class Solution {
    public int search(int[] nums, int target) {
        int start = 0;
        int end = nums.length - 1;

        while (start <= end){
            int mid = (start + end) / 2;
            if(target == nums[mid])
                return mid;
            
            if (nums[start] <= nums[mid]){
                // normal so far, increasing order
                if (target > nums[mid] || target < nums[start]){
                    // target is bigger than mid
                    // target is lesser than start, so its in second half/end
                    start = mid + 1;
                } else
                    end = mid - 1;
            } else {
                // weird case, starting is somewhere in second half, mid > end
                if (target < nums[mid] || target > nums[end]){
                    // target is less than mid, even thoug mid bigger than start
                    // target is greater than end, so its in first half/start
                    end = mid - 1;
                } else
                    start = mid + 1;
            }
        }
        return -1;
    }
}
