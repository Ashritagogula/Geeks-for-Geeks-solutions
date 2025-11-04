class Solution:
    def minCost(self, height):
        n = len(height)
        if n == 1:
            return 0
        prev2 = 0
        prev1 = abs(height[1] - height[0])
        
        for i in range(2, n):
            jump1 = prev1 + abs(height[i] - height[i - 1])
            jump2 = prev2 + abs(height[i] - height[i - 2])
            curr = min(jump1, jump2)
            prev2, prev1 = prev1, curr
        
        return prev1
