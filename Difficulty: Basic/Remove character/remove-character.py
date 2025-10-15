#User function Template for python3

class Solution:
    def removeChars(self, str1, str2):
        remove_set = set(str2)
        result = ''
        for c in str1:
            if c not in remove_set:
                result += c
        return result
