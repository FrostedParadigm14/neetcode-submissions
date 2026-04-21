class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int num: nums){
            if (set.contains(num))
                return true;
            set.add(num);
        }
        return false;
    }
}

/*
hash set to efficiently keep track of the 
values we have already encountered.
check whether the current value is already present in the set.

hash set allows constant-time lookups, 
*/