class Solution:
    def isSubset(self, a, b):
        from collections import Counter
        ca = Counter(a)
        for x in b:
            if ca[x] == 0:
                return False
            ca[x] -= 1
        return True
