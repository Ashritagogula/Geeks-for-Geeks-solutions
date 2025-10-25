class Solution:
    def nthRowOfPascalTriangle(self, n):
        if n == 1:
            return [1]
        prev = [1]
        for r in range(1, n):
            curr = [1]
            for i in range(1, r):
                curr.append(prev[i-1] + prev[i])
            curr.append(1)
            prev = curr
        return prev
