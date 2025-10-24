class Solution:
    def getMaxOccurringChar(self, s):
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        
        max_freq = max(freq.values())
        candidates = [ch for ch, count in freq.items() if count == max_freq]
        
        return min(candidates)
