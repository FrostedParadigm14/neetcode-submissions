from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for str in strs:
            freq = [0] * 26 
            for char in str:
                freq[ord(char) - ord('a')]+=1
            
            dict[tuple(freq)].append(str)

        #print(dict.values())
        return list(dict.values())


'''
defaultdict to make dict of list, tuple, set, etc...
   - make a new freq list of 0 from 0 to 26....for each word - use that as key
   - if the letter - 'a' is there then +1 to that index
ord is to get unicode/ascii value 
    - use the freq as a tuple to add as key to dict
    - append the word, so multiple values added to one key
    - python normally not allow list/arr as key bc its not immutable, change to tuple
NO add in append, extend will create 'c', 'a', 't'
    - make a list of the values in dictionary
    - return list



'''
        