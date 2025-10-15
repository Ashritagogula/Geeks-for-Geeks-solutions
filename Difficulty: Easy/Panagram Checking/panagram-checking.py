class Solution:
    def checkPangram(self,s):
        #code here
        s = s.lower()
        letters = set()
        for c in s:
            if c.isalpha():
                letters.add(c)
        return len(letters) == 26