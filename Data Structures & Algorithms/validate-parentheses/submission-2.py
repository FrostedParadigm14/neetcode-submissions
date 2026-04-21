class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictionary = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            if char in dictionary:
                if stack and stack[-1] == dictionary[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        if not stack:
            return True
        return False

'''
create stack to track 
dictionary to match closed with open
if closed found in string, 
    check that the last added in stack matches
    otherwise not valid
add other opens in stack ...until closed is found again

if stack is empty at end - all accounted for
not empty - not closed properly
'''
            

        

        