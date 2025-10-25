class Solution:
    def uncommonChars(self, s1, s2):
        return ''.join(sorted(set(s1) ^ set(s2)))
