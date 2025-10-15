class Solution:
    def isRotated(self,s1,s2):
        #code here
        if len(s1) != len(s2):
            return False
        return s2 == s1[2:] + s1[:2] or s2 == s1[-2:] + s1[:-2] 