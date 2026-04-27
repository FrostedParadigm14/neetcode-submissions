class Solution {
    public int lengthOfLongestSubstring(String s) {
        // Set<Character> subSet = new HashSet<>();
        // int l = 0;
        // int ans = 0;

        // for(int r = 0; r < s.length(); r++){
        //     while (subSet.contains(s.charAt(r))){
        //         subSet.remove(s.charAt(l));
        //         l++;
        //     }
        //     subSet.add(s.charAt(r));
        //     ans = Math.max(ans, r-l+1);
        // }
        // return ans;
        Map<Character, Integer> map = new HashMap<>();
        int l = 0;
        int ans = 0;

        for(int r = 0; r < s.length(); r++){
            if(map.containsKey(s.charAt(r)))
                l = Math.max(l, map.get(s.charAt(r))+1);
            map.put(s.charAt(r), r);
            ans = Math.max(ans, r-l+1);
        }
        return ans;
    }
}
