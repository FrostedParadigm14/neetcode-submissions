class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')]+=1
        for c in t:
            count[ord(c) - ord('a')]-=1

        for c in count:
            if c != 0:
                return False
        return True
            
'''
arr = [0] * 26
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

print(ord('a')) - find ascii of 'a'

create empty array of 26, abc lowercase rep
iterate through first word, where there is that char, do +1
iterate through second word, where there is that char, do -1

check if all in arr is back to 0, otherwise not anagram
'''      