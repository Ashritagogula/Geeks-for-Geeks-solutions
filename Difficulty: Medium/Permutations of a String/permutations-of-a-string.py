class Solution:
    def findPermutation(self, s):
        s = sorted(s)
        res = []
        u = [False] * len(s)
        def f(p):
            if len(p) == len(s):
                res.append("".join(p))
                return
            for i in range(len(s)):
                if u[i]: continue
                if i > 0 and s[i] == s[i-1] and not u[i-1]: continue
                u[i] = True
                p.append(s[i])
                f(p)
                p.pop()
                u[i] = False
        f([])
        return res
