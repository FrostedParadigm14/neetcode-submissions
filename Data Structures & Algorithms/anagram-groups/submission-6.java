class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> dict = new HashMap<>();

        for(String str : strs){
            int [] freq = new int [26];
            for(Character c : str.toCharArray()){
                freq[c - 'a']++;
            }
            String key = Arrays.toString(freq);
            if(dict.get(key) == null)
                dict.put(key, new ArrayList<>());
            dict.get(key).add(str);
        } 

        return new ArrayList<> (dict.values());
    }
}

/*
intiallu tried  Map<List<Integer>, List<String>> but harder to set [] up
change with arrays,toString for easier key
put new arraylist if empty, add to it
*/