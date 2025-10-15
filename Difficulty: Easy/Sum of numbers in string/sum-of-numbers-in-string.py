class Solution:
    def findSum(self, s):
        total = 0
        num = ''
        for c in s:
            if c.isdigit():
                num += c
            else:
                total += int(num) if num else 0
                num = ''
        total += int(num) if num else 0
        return total
