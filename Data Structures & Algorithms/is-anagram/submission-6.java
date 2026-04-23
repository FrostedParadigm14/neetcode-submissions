class Solution {
    public boolean isAnagram(String s, String t) {
        int[] arr = new int [26];

        for (Character c: s.toCharArray()){
            arr[c - 'a']++;
        }

        for (Character c: t.toCharArray()){
            arr[c - 'a']--;
        }

        for (int c : arr)
            if (c != 0)
                return false;

        return true;
    }
}

/*
int a = 'a';  -- find ascii


*/